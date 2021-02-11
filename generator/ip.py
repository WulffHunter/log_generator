from faker import Faker
import random
import parameters

from utils import chance_choose

def gen_ip(test_mode=False):
    # There is a 10% chance that the generator will create an IPv6 address
    # to ensure it's accounted for.
    return chance_choose(Faker().ipv6(), Faker().ipv4(), parameters.frequency['ipv6'])
