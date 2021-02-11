from utils import chance_choose
import parameters
import string
import random


def gen_hostname():
    # We re-declare this value every time the function runs because
    # the first character cannot be a hyphen, so we'll append it after
    # the first run to save time running a `while` statement in the
    # `for` loop below.
    #
    # From https://man7.org/linux/man-pages/man7/hostname.7.html:
    #
    # | Each element of the hostname must be from 1 to 63 characters long and
    # | the entire hostname, including the dots, can be at most 253
    # | characters long.  Valid characters for hostnames are ASCII(7) letters
    # | from a to z, the digits from 0 to 9, and the hyphen (-).  A hostname
    # | may not start with a hyphen.
    useable_chars = string.ascii_lowercase + \
        string.ascii_uppercase + string.digits

    hostname = []

    for i in range(
        random.randint(
            1,
            parameters.max_val['hostname_length'])):
        # Randomly choose either a lowercase letter (80% of the time)
        # or a 'useable character' (see above)
        hostname.append(
            chance_choose(
                random.choice(
                    string.ascii_lowercase),
                random.choice(useable_chars),
                parameters.frequency['hostname_lc_letter']))

        # After the first character, enable use of the hyphen
        if i == 0:
            useable_chars += '-'

    return ''.join(hostname)
