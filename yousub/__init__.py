import sys
from urllib.error import HTTPError, URLError

from .models import YouSub, NoSubtitleException
from .options import parse_options
from .models import logger


def main():
    try:
        parser, args = parse_options()
        YouSub.run(url=args.url, dir=args.directory, show=args.show, lang=args.lang, filetype=args.filetype)
        logger.info("Done")
    except (HTTPError, URLError) as error:
        sys.exit('ERROR: No response, can you open this url in browser?')
    except NoSubtitleException as error:
        sys.exit(error.msg)
    except KeyboardInterrupt:
        sys.exit('ERROR: Interrupted by user')


__all__ = ['main', ]
