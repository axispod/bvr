"""Banch video recoder"""
from cli import get_cli_parser
from config import config


def main():
    args = get_cli_parser().parse_args()
    if args.init:
        config_path = config.make_default()
        print("The default config is written to: " + config_path)

    print(args)


if __name__ == "__main__":
    main()
