# ///
# requires-python = ">=3.11"
# dependencies = [
#    "jinjax",
#    "pyppeteer",
#    "dykes"
# ]
# ///

import asyncio
import sys
from csv import DictReader
from dataclasses import dataclass
from enum import StrEnum, auto
from pathlib import Path
from typing import Annotated, Self

import jinjax
import dykes  # type:ignore
from pyppeteer import launch  # type:ignore

catalog = jinjax.Catalog(
    filters={
        "len": len
    }
)

catalog.add_folder("./templates")


class CardType(StrEnum):
    ATTACK = auto()
    LESSON = auto()


@dataclass
class Card:
    name: str
    card_type: CardType
    cost: int | None = None
    attack: int | None = None
    defense: int | None = None
    charge: int | None = None
    see: int | None = None
    keep: int | None = None

    def __repr__(self):
        class_name = type(self).__name__

        match self.card_type:
            case CardType.ATTACK:
                return f"{class_name}(name='{self.name}', card_type='{self.card_type}', cost={self.cost}, attack={self.attack}, defense={self.defense})"
            case CardType.LESSON:
                return f"{class_name}(name='{self.name}', card_type='{self.card_type}', charge={self.charge}, attack={self.see}, keep={self.keep})"

    @classmethod
    def make_attack(cls, name, cost, attack, defense) -> Self:
        return cls(name=name, card_type=CardType.ATTACK, cost=cost, attack=attack, defense=defense)

    @classmethod
    def make_lesson(cls, name, charge, see, keep) -> Self:
        return cls(name=name, card_type=CardType.LESSON, charge=charge, see=see, keep=keep)

    @classmethod
    def make_from_csv_row(cls, row: dict[str, str]) -> Self:
        match row:
            case {"type": CardType.ATTACK}:
                return cls.make_attack(row["name"], int(row["cost"]), int(row["attack"]), int(row["defense"]))
            case {"type": CardType.LESSON}:
                return cls.make_lesson(row["name"], int(row["charge"]), int(row["see"]), int(row["keep"]))
        raise ValueError("Unrecognized card type.")


@dataclass
class Arguments:
    file_path: Path
    output_path: Annotated[Path, dykes.options.NArgs("?")] = Path("output.png")
    debug: bool = False


async def main() -> None:
    args: Arguments = dykes.parse_args(Arguments)

    if not args.file_path.is_file():
        print("File must exist.", file=sys.stderr)
        raise SystemExit(1)

    with args.file_path.open() as file:
        card_rows = list(DictReader(file))

    if not card_rows:
        print("No cards in definition file.", file=sys.stderr)
        raise SystemExit(2)

    cards = [Card.make_from_csv_row(row) for row in card_rows]
    html = catalog.render("Layout", cards=cards)
    if args.debug:
        with open("debug.html", "w") as f:
            f.write(html)

    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({"width": 4096, "height": 4096, "deviceScaleFactor": 1})
    await page.setContent(html)
    await page.screenshot({'path': args.output_path})
    await browser.close()

asyncio.run(main())
