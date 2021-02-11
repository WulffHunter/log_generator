import random
import string
import parameters

def gen_bytes(test_mode=False):
    # The maximum is 116 kilobytes (based off the uncompressed size of Bootstrap)
    b = random.randint(0, parameters.max_val['bytes'])

    # This is per the `%b` field in Apache logs
    return '-' if b == 0 else b
