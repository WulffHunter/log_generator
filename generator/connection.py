import random

connection_statuses = [ 'X', '+', '-' ]

def gen_connection():
    return random.choice(connection_statuses)
