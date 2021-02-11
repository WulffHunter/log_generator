import random

import parameters
from utils import chance, chance_choose
from hostname import gen_hostname
from tld import common_tlds, all_tlds

# Per https://qr.ae/pNKo1B, ensure that the number of
# characters does not exceed 110 (to leave room for the TLD).
#
# This could be 127, but we're leaving room for the TLD
MAX_SERVER_CHARS = 110


def gen_servername(test_mode=False):
    server_labels = []

    if chance(parameters.frequency['servername_use_www']):
        server_labels.append('www')

    # Append at least one hostname
    server_labels.append(gen_hostname())

    if chance(parameters.frequency['servername_multiple_labels']):
        for _ in range(
            random.randint(
                0,
                parameters.max_val['servername_labels'])):
            # Keeping track of how long the servername currently is
            server_len = len(''.join(server_labels))

            if server_len < MAX_SERVER_CHARS:
                label = gen_hostname()

                # If there's room for this label, append it
                if server_len + len(label) < MAX_SERVER_CHARS:
                    server_labels.append(label)

    server_labels.append(
        chance_choose(
            'com',
            chance_choose(
                random.choice(common_tlds),
                random.choice(all_tlds),
                parameters.frequency['servername_common_tld']),
            parameters.frequency['serverame_dot_com']))

    return '.'.join(server_labels)
