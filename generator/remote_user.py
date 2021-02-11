import random
import parameters
import string

from utils import chance
from hostname import gen_hostname

def gen_remote_user(test_mode=False):
    # There's an 80% chance that the hostname will be empty
    if chance(parameters.frequency['empty_remote_user']):
        return '-'

    return gen_hostname()
