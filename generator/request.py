from faker import Faker
import random
import parameters

from utils import chance_choose, chance

from uri_generator import gen_path, uri_extensions, gen_uri_useable

# TODO: Continue to expand this list with the proper formats for other application
# layer protocols (e.g. FTP, SSH, SMTP...)
protocols = ['HTTP/1.0', 'HTTP/1.1', 'HTTP/2']

common_methods = ['GET', 'PUT', 'POST', 'DELETE']

# Faker is passed in as an argument to prevent unnecessary re-decleration,
# but is not needed to make this method run.


def gen_req_method(test_mode=False, faker=None):
    if faker is None:
        faker = Faker()

    return chance_choose(
        random.choice(common_methods),
        faker.http_method(),
        parameters.frequency['common_http'] / 100)


def gen_uri_path(test_mode=False):
    # TODO: Continue extending the possible URI paths and file
    # extension types

    # TODO: Add in querystrings

    # This format allows for choice of a URI path or a document
    path_options = [
        gen_path(test_mode),

        '{}{}'.format(
            gen_path(test_mode),
            random.choice(uri_extensions)
        )
    ]

    return random.choice(path_options)


def gen_querystring(test_mode=False):
    # There's an 80% chance that a querystring will be non-existant
    if chance(parameters.frequency['empty_querystring']):
        return ''

    queries = []

    for _ in range(
        random.randint(
            1,
            parameters.max_val['querystring_elements'])):
        queries.append(
            '{}={}'.format(
                gen_uri_useable(),
                gen_uri_useable()))

    querystring = '&'.join(queries)

    return '?{}'.format(querystring)


def gen_req_protocol(test_mode=False):
    return random.choice(protocols)


def gen_request(test_mode=False):
    fake = Faker()

    # 90% chance of being a common method
    method = gen_req_method(fake)

    path = gen_uri_path(test_mode)

    querystring = gen_querystring()

    protocol = gen_req_protocol()

    return '{} {}{} {}'.format(method, path, querystring, protocol)
