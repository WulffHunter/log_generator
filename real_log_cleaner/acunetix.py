from utils import convert_file

ESCAPED_QUOTE_STRING = '^^log_parser_escaped_quote'


def gen_line(line):
    # Example line:
    # "192.168.4.25 - - [22/Dec/2016:16:36:26 +0300] "GET /index.php/component/search/?ordering=newest&searchphrase=any&searchword=%f0''%f0\"\" HTTP/1.1" 200 3148 "http://192.168.4.161/DVWA" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21""

    # Since there may be the characters `\"` (an escaped quote)
    # in the string, we replace the escaped quote with
    # `%log_parser_escaped_quote`, to be turned back after
    # splitting by quotes
    line = line.replace('\\"', ESCAPED_QUOTE_STRING)
    split_by_quotes = line.split('"')
    split_by_quotes = list(map(
        lambda section: section.replace(ESCAPED_QUOTE_STRING, '\\"'),
        split_by_quotes))

    # Results in:
    # [
    #   '',
    #   '192.168.4.25 - - [22/Dec/2016:16:30:52 +0300] ',
    #   'POST /administrator/index.php HTTP/1.1',
    #   ' 303 382 ',
    #   'http://192.168.4.161/DVWA',
    #   ' ',
    #   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21',
    #   '',
    #   ''
    # ]

    request = split_by_quotes[2]
    referer = split_by_quotes[4]
    user_agent = split_by_quotes[6]

    # '192.168.4.25 - - [22/Dec/2016:16:30:52 +0300] '
    split_by_bracket = split_by_quotes[1].split('[')
    # Results in:
    # [
    #     '192.168.4.25 - - ',
    #     '22/Dec/2016:16:30:52 +0300] '
    # ]

    # Remove the last bracket from the datetime
    dtime = split_by_bracket[1].replace('] ', '')

    ip_logname_user = split_by_bracket[0].split()
    # Results in:
    # [
    #     '192.168.4.25',
    #     '-',
    #     '-'
    # ]
    ip = ip_logname_user[0]
    logname = ip_logname_user[1]
    user = ip_logname_user[2]

    status_bytes_sent = split_by_quotes[3].split()
    # Results in:
    # [
    #     '200',
    #     '203023'
    # ]

    status = status_bytes_sent[0]
    bytes_sent = status_bytes_sent[1]

    orig_line = '"{} {} {} [{}] "{}" {} {} "{}" "{}""'.format(
        ip,
        logname,
        user,
        dtime,
        request,
        status,
        bytes_sent,
        referer,
        user_agent)
    truth_line = '"{}_{}_{}_[{}]_"{}"_{}_{}_"{}"_"{}""'.format(
        'h' * len(ip),
        'l' * len(logname),
        'u' * len(user),
        't' * len(dtime),
        'r' * len(request),
        's' * len(status),
        'b' * len(bytes_sent),
        'R' * len(referer),
        'i' * len(user_agent))

    return orig_line, truth_line


def main(input_file_name: "Input file name",
         output_file_name: "Output file name"):
    convert_file(gen_line, input_file_name, output_file_name)


if __name__ == "__main__":
    import plac

    plac.call(main)
