from utils import convert_file

def gen_line(line):
    # Example line:
    # 83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET
    # /presentations/logstash-monitorama-2013/images/kibana-search.png
    # HTTP/1.1" 200 203023
    # "http://semicomplete.com/presentations/logstash-monitorama-2013/"
    # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1)
    # AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77
    # Safari/537.36"

    split_by_quotes = line.split('"')

    # Results in:
    # [
    #     '83.149.9.216 - - [17/May/2015:10:05:03 +0000] ',
    #     'GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1',
    #     ' 200 203023 ',
    #     'http://semicomplete.com/presentations/logstash-monitorama-2013/',
    #     ' ',
    #     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36',
    #     ''
    # ]

    request = split_by_quotes[1]
    referer = split_by_quotes[3]
    user_agent = split_by_quotes[5]

    # '83.149.9.216 - - [17/May/2015:10:05:03 +0000] '
    split_by_bracket = split_by_quotes[0].split('[')
    # Results in:
    # [
    #     '83.149.9.216 - - ',
    #     '17/May/2015:10:05:03 +0000] '
    # ]

    # Remove the last bracket from the datetime
    dtime = split_by_bracket[1].replace('] ', '')

    ip_logname_user = split_by_bracket[0].split()
    # Results in:
    # [
    #     '83.149.9.216',
    #     '-',
    #     '-'
    # ]
    ip = ip_logname_user[0]
    logname = ip_logname_user[1]
    user = ip_logname_user[2]

    status_bytes_sent = split_by_quotes[2].split()
    # Results in:
    # [
    #     '200',
    #     '203023'
    # ]

    status = status_bytes_sent[0]
    bytes_sent = status_bytes_sent[1]

    orig_line = '{} {} {} [{}] "{}" {} {} "{}" "{}"'.format(
        ip,
        logname,
        user,
        dtime,
        request,
        status,
        bytes_sent,
        referer,
        user_agent)
    truth_line = '{}_{}_{}_[{}]_"{}"_{}_{}_"{}"_"{}"'.format(
        'h' *len(ip),
        'l' *len(logname),
        'u' *len(user),
        't' *len(dtime),
        'r' *len(request),
        's' *len(status),
        'b' *len(bytes_sent),
        'R' *len(referer),
        'i' *len(user_agent))

    return orig_line, truth_line


def main(input_file_name: "Input file name", output_file_name: "Output file name"):
    convert_file(gen_line, input_file_name, output_file_name)


if __name__ == "__main__":
    import plac

    plac.call(main)
