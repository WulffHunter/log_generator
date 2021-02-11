import parameters
from utils import chance_choose
from request import gen_uri_path, gen_querystring


def gen_referer(test_mode=False):
    return chance_choose(
        '-',
        '{}{}'.format(
            gen_uri_path(
                test_mode=test_mode),
            gen_querystring()),
        parameters.frequency['referer_empty'])
