'''References:
    https://docs.python.org/3/howto/argparse.html
    https://realpython.com/command-line-interfaces-python-argparse/
'''

import argparse
import logging
import sys

DEBUG = True

if DEBUG:
    logging.basicConfig(level=logging.INFO, format='%(filename)s:%(lineno)d:%(levelname)s:%(message)s')
else:
    logging.basicConfig(format='%(filename)s:%(lineno)d:%(levelname)s:%(message)s')

Examples = r"""
Examples
--------
Windows:
    -i input_file.txt
    --input_path c:\users\username\desktop\ 
    -o output_file.txt
    --output_file output_file.txt
Linux:
    --input_path /home/username/
    --ouput_path /home/username
"""


parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, epilog=Examples)
parser.add_argument('-i', '--input-filename',
    required=True,
    help=" REQUIRED")

parser.add_argument('--input-path',
    required=True,
    help="REQUIRED")

parser.add_argument('-o', '--output-filename',
    required=True,
    help="REQUIRED")

parser.add_argument('--output-path',
    required=False,
    default="./",
    help="""Default is current directory""")


def do_something(args):
    logging.info('hello world')
    logging.info(args.input_filename)
    logging.info(args.input_path)
    logging.info(args.output_filename)
    logging.info(args.output_path)

    try:
        with open(f'{args.input_path}{args.input_filename}', 'r') as fh:
            data = fh.readlines()
    except Exception as e:
        logging.error(e)
        raise

    try:
        with open(f'{args.output_path}{args.output_filename}', 'w') as fh:
            fh.write(''.join(data))
    except Exception as e:
        logging.error(e)
        raise

if __name__ == '__main__':
    args = parser.parse_args()

    if DEBUG:
        logging.warning(args)
    else:
        logging.warning(args)

    try: 
        do_something(args)
        print(f"""
        Your output file is
        {args.output_path}{args.output_filename}""")

    except Exception as e:
        logging.error(f"""
        Yikes, there has been a mishap!!
        Here is the error:
        {e}""")

# vim: ai et ts=4 sw=4 sts=4 nu

