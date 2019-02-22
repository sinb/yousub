import argparse


def parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="YouTube video url")
    parser.add_argument("-d", "--directory",
                        help="specify the output directory, if not exists then create automatically")
    parser.add_argument("-s", "--show",
                        help="only show available languages of subtitle, not downloading files",
                        action="store_true")
    parser.add_argument("-l", "--lang",
                        help="specify the language code")
    args = parser.parse_args()
    return parser, args
