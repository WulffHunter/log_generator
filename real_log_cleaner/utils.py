def convert_file(conversion_fn, input_file_name, output_file_name, debug_mode=False):
    out_lines = []

    with open(input_file_name, "r") as f:
        line_cnt = 0
        for line in f:
            line = line.replace('\n', '')
            orig, truth = conversion_fn(line)

            # If debugging, raise an exception if one of the lines converts incorrectly
            # Can be turned off because sometimes the logs are incorrect
            if debug_mode and line != orig:
                print('Conversion function is incorrect for line {}: {} => {}'.format(line_cnt, line, orig))

            out_lines.append('{}\t{}'.format(orig, truth))

            line_cnt += 1
    
    out_file = open(output_file_name, 'w')
    out_file.write('\n'.join(out_lines))
    out_file.close()
    print(f"Converted  {line_cnt} lines from {input_file_name} to {output_file_name}")
