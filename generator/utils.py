import random

# Replaces an imput string with its field ID.
#
# e.g. for a date: `"Jan 1 2020, 1:00AM"`, the ID of this field
# is `d`, thus the output would be `dddddddddddddddddd` (one `d`
# per character of the input string)
def string_to_field(in_string, field_id):
    return field_id * len(str(in_string))

def load_file(filename):
    # rt = read text mode
    file = open(filename, mode='rt', encoding='utf-8')
    text = file.read()
    file.close()
    print('Read: %s' % filename)
    return text

def write_file(filename, text):
    # wt = write text mode (overwrites all text existing in the file)
    file = open(filename, mode='wt', encoding='utf-8')
    file.write(text)
    file.close()
    print('Wrote: %s' % filename)

# 'percent' percent chance it will return true
# Similar to above, yet returns a boolean value
def chance(percent):
    return random.random() <= (percent / 100)

# 'percent' percent chance it will return a, otherwise return b
# e.g. 75% chance it will be 'a': chance(a, b, 75)
def chance_choose(a, b, percent):
    return a if chance(percent) else b
