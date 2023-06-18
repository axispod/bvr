"""Banch video recoder"""
from cli import get_cli_parser
from config import config


def main():
    args = get_cli_parser().parse_args()
    if args.init:
        config.make_default()

    print(args)


if __name__ == "__main__":
    main()
