import argparse
from pathlib import Path
from typing import cast, Protocol

import card_generator

DEFAULT_CONFIG_PATH = "card_config.toml"


class Arguments(Protocol):
    output_file: Path
    configuration: Path


parser = argparse.ArgumentParser()
parser.add_argument("--output_file", "-o", default="output.csv", type=Path)
parser.add_argument("--configuration", "-c", default=DEFAULT_CONFIG_PATH, type=Path)


def run_cli():
    args: Arguments = cast(Arguments, parser.parse_args())
    card_generator.main(args.output_file, args.configuration)
