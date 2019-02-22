import sys
import os

from .models import YouSub
from .options import parse_options


def main():
    try:
        parser, argv = parse_options()
        argv.directory = argv.directory or os.getcwd()
        print(argv)
        codes = YouSub.get_lang_codes_list(argv.url)
        YouSub.get_subtitle_by_lang_code(codes[0], argv.url)
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')


__all__ = ['main', ]
