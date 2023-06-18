"""Command Line Interface"""
import argparse

parser = argparse.ArgumentParser(
    prog="Bunch Video Recode", description="Automatic video recoding."
)

parser.add_argument("-i", "--init", action="store_true", help="Init the application")


def get_cli_parser():
    """Get command line interface

    Returns:
        The CLI parser
    """
    return parser
