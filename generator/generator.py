import re
import random

from bytes_transferred import gen_bytes
from connection import gen_connection
from ip import gen_ip
from remote_logname import gen_remote_logname
from remote_user import gen_remote_user
from request import gen_request, gen_req_method, gen_uri_path, gen_req_protocol, gen_querystring
from status import gen_status
from datetime_of_req import gen_datetime
from servername import gen_servername
from user_agent import gen_user_agent
from referer import gen_referer

from utils import string_to_field, chance
import parameters

clf_string = 'h l u t "r" s b'
combined_log_format_string = 'h l u t "r" s b "R" "i"'

fields = {
    'h': gen_ip,
    'l': gen_remote_logname,
    'u': gen_remote_user,
    't': gen_datetime,
    'r': gen_request,
    's': gen_status,
    'b': gen_bytes,
    'm': gen_req_method,
    'U': gen_uri_path,
    'H': gen_req_protocol,
    'q': gen_querystring,
    'v': gen_servername,
    'V': gen_servername,
    'i': gen_user_agent, # While technincally `i` can relate to any
    # request header value, we're using it for user agent since it's
    # most often used for user agent and both `u` and `U` are taken
    'R': gen_referer, # Referer also comes from the `i` field, but
    # `R` wasn't taken
}


def gen_random_template():
    keys = fields.keys()
    # Number of elements: 3 to max_fields_available
    elements = random.sample(keys, k=random.randint(3, len(keys)))
    pretty_elements = []
    for el in elements:
        pretty = el
        # There is a 70% chance that a `request` string is wrapped in quotes.
        # Otherwise, there is a 10% chance that it's wrapped in quotes.
        #
        # The idea is that, since in CLF format the request string `%r` is
        # wrapped in quotes, it has a 70% chance of being wrapped in quotes
        # in whatever random template is used. However, if the current character
        # is not the request string, say `%s` or `%h`, it only has a 10% chance
        # of being wrapped in quotes.
        wrap_in_quotes = chance(
            parameters.frequency['other_field_in_quotes'])

        # Using the logic in the comment above, we overwrite the chance that
        # the value is wrapped in quotes if it's a request string
        if el == 'r':
            wrap_in_quotes = chance(
                parameters.frequency['request_in_quotes'])

        if wrap_in_quotes:
            pretty = '"{}"'.format(pretty)

        # Like with quotations and the `request` string, there is a
        # 40% chance that a `datetime` string is wrapped in brackets.
        # Otherwise, there is a 5% chance that it's wrapped in brackets.
        #
        # This is based off of the sample logs from Ocatak on GitHub,
        # which has all datetime strings wrapped in square brackets.
        wrap_in_brackets = chance(
            parameters.frequency['other_field_in_brackets'])

        # Using the logic in the comment above, we overwrite the chance that
        # the value is wrapped in brackets if it's a datetime string
        if el == 't':
            wrap_in_brackets = chance(
                parameters.frequency['datetime_in_brackets'])

        if wrap_in_brackets:
            pretty = '[{}]'.format(pretty)

        # Randomly add extra whitespace 0% of the time
        if chance(parameters.frequency['extra_whitespace']):
            pretty = '{}{}'.format(
                pretty,
                ' ' *
                random.randint(
                    0,
                    parameters.max_val['extra_whitespace']))

        pretty_elements.append(pretty)

    # There's a 30% chance that the entire template will be
    # wrapped in quotation marks
    if chance(parameters.frequency['template_in_quotes']):
        return '"{}"'.format(' '.join(pretty_elements))

    return ' '.join(pretty_elements)


# Default template string is CLF (Common Log Format)
def generator(template=clf_string, test_mode=False):

    # These will be the final output strings.
    # We copy them instead of using joined lists to preserve
    # whitespace.
    generated, final_truth = [], []

    # Split into a list of characters
    elements = list(template)
    for char in elements:
        replaced = char
        # If this section of the template string could not be replaced,
        # it will appear as question marks in the final ground
        # truth
        truth = string_to_field(replaced, '?')

        if char in fields:
            # Replace the field with its generated equivalent
            replaced = replaced.replace(
                char, str(fields[char](test_mode=test_mode)))

            # If the current character is a datetime, and the
            # format is not CLF
            if char == 't' and template != clf_string:
                # Reset replaced
                replaced = char

                # There's a 30% chance that the datetime will be
                # in ISO format
                replaced = replaced.replace(
                    char, str(
                        fields[char](
                            test_mode=test_mode, use_iso=(
                                chance(
                                    parameters.frequency['use_iso_string'])))))

            truth = string_to_field(replaced, char)
        # It's valid for the current element to be whitespace only
        elif char == ' ':
            truth = string_to_field(replaced, '_')
        elif char == '[' or char == ']' or char == '"':
            truth = char
        else:
            print(
                "Failed to replace token %s. Please fix this part of your template string: %s." %
                (char, char))

        # Place the generated string and the truth string into their
        # respective outputs
        generated.append(replaced)
        final_truth.append(truth)

    # Return the generated string and the final truth, with all whitespace
    # replaced with underscores.
    return [
        ''.join(generated),
        ''.join(final_truth)
    ]


if __name__ == "__main__":
    print("CLF log:")
    print(generator())
    template = gen_random_template()
    print("Random template log:")
    print("Random template: %s" % template)
    print(generator(template=template))
