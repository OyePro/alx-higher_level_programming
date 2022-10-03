#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C)
prints those statistics since the beginning
"""


def get_stats(size, status_codes):
    """
    computing metrics
    Args:
        size - size of the read files
        status_codes - count of status codes
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    from sys import stdin

    size = 0
    status_codes = {}
    pos_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in stdin:
            if count == 10:
                get_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in pos_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        get_stats(size, status_codes)

    except KeyboardInterrupt:
        get_stats(size, status_codes)
        raise
