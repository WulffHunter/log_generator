frequency = {
    # Controls how often `ip.py` will output an IPv6 address
    # instead of IPv4
    'ipv6': 10,
    # Controls how often a request string in a randomized template
    # will be wrapped in quotes (i.e. how often a random template
    # will include `\"%r\"` instead of just `%r`)
    'request_in_quotes': 70,
    # Controls how often other, non-request fields in a randomized template
    # will be wrapped in quotes (i.e. how often a random template
    # will include some field `%f` as `\"%f\"` instead of just `%f`)
    'other_field_in_quotes': 10,
    # Controls how often extra whitespace will be added after a field in
    # a randomized template (e.g. `%f   ` or `%f`)
    'extra_whitespace': 0,
    # 'extra_whitespace': 25,
    # Controls how often `request.py` will use a common HTTP
    # request (GET, PUT, POST, DELETE) rather than ANY HTTP
    # request (GET, POST, CONNECT, HEAD... etc.)
    'common_http': 90,
    # Controls how often an HTTP status number will be a common
    # status number (200, 204, 404, 401, 400, 500, 501... etc.)
    # rather than ANY status number (508, 599, 426, 300, 304... etc.)
    'common_status': 80,
    # Controls how often a row in a file from `file.py` will use
    # the CLF template string instead of a random template string
    'CLF_template': 40,
    # Controls how often a template is in Combined Log Format
    'combined_log_format_template': 40,
    # Controls how often the query string is non-existant
    'empty_querystring': 80,
    # Controls how often the URI generator will use a 'printable'
    # character (e.g. "" or ' or ~, but may still be a letter)
    # rather than a lowercase letter
    'uri_use_printable_char': 10,
    # Controls how often an ISO datetime string is used instead of
    # an Apache-formatted string in non-CLF templates
    'use_iso_string': 30,
    # Controls how often the remote user will be empty (`-`)
    'empty_remote_user': 80,
    # Controls how often a servername will start with 'www.'
    'servername_use_www': 40,
    # Controls how often a hostname character will be a lowercase
    # letter
    'hostname_lc_letter': 80,
    # Controls how often the servername ends with '.com'
    'serverame_dot_com': 60,
    # Controls how often a servername ends with a common TLD (if not '.com')
    'servername_common_tld': 70,
    # Controls how often a servername has more than 1 label
    # (e.g. in 'help.jared.rand.com', 'help', 'jared', and 'rand'
    # would all be labels)
    'servername_multiple_labels': 40,
    # Controls how often a field will be wrapped in square brackets
    'other_field_in_brackets': 5,
    # Controls how often a datetime field will be wrapped in sqaure
    # brackets
    'datetime_in_brackets': 40,
    # Controls how often a template is wrapped in quotations
    'template_in_quotes': 30,
    # Controls how often a referer field is empty
    'referer_empty': 40,
}

max_val = {
    # The maximum amount of bytes `bytes_transferred.py` will output
    'bytes': 116000,
    # The maximum amount of whitespace that will be added between
    # characters in a randomized template
    'extra_whitespace': 7,
    # The maximum depth a uri path can be (e.g. 'foo/bar/baz'
    # has a depth of 3)
    'uri_path_depth': 7,
    # The maximum character length of some folder name in a URI
    # (e.g. '/foo/' is 3 characters long)
    'uri_folder_length': 15,
    # The maximum amount of query elements that can be present in a
    # querystring
    'querystring_elements': 20,
    # The maximum length of a hostname, according to the Linux docs
    'hostname_length': 63,
    # The maximum amount of labels a servername can have
    'servername_labels': 4,
}
