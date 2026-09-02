from __future__ import annotations

import argparse
import csv
import html
import re
from pathlib import Path


CARD_HEADING = re.compile(r"^## Card ([0-9]+)\s*$", re.MULTILINE)


def extract_field(block: str, field: str, next_field: str | None = None) -> str:
    if next_field is None:
        end = r"\Z"
    else:
        end = rf"(?=\n+\*\*{re.escape(next_field)}\*\*)"

    pattern = re.compile(
        rf"\*\*{re.escape(field)}\*\*\s*\n+(.*?){end}",
        re.DOTALL,
    )
    match = pattern.search(block)
    if match is None:
        raise ValueError(f"Missing or malformed **{field}** section")
    return match.group(1).strip()


def convert_content(markdown: str) -> str:
    """Convert the limited Markdown used in cards to Anki-compatible HTML."""

    def display_math(match: re.Match[str]) -> str:
        formula = " ".join(line.strip() for line in match.group(1).strip().splitlines())
        return rf"\[{formula}\]"

    converted = re.sub(r"\$\$(.*?)\$\$", display_math, markdown, flags=re.DOTALL)
    converted = re.sub(
        r"(?<!\\)\$(.+?)(?<!\\)\$",
        lambda match: rf"\({match.group(1)}\)",
        converted,
    )

    converted = html.escape(converted, quote=False)
    converted = re.sub(r"\n[ \t]*\n+", "<br><br>", converted)
    converted = converted.replace("\n", "<br>")
    return converted


def parse_cards(markdown: str) -> list[tuple[str, str, str, str]]:
    sections = CARD_HEADING.split(markdown)
    cards: list[tuple[str, str, str, str]] = []
    seen_ids: set[str] = set()

    for index in range(1, len(sections), 2):
        card_id = sections[index]
        block = sections[index + 1]

        if card_id in seen_ids:
            raise ValueError(f"Duplicate card ID: {card_id}")
        seen_ids.add(card_id)

        front = extract_field(block, "Front", "Back")
        back = extract_field(block, "Back", "Tags")
        tags = extract_field(block, "Tags")

        cards.append(
            (
                card_id,
                convert_content(front),
                convert_content(back),
                " ".join(tags.split()),
            )
        )

    if not cards:
        raise ValueError("No cards found. Expected headings such as '## Card 001'.")

    return cards


def write_tsv(cards: list[tuple[str, str, str, str]], output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        output_file.write("#separator:Tab\n")
        output_file.write("#html:true\n")
        output_file.write("#notetype:RL Basic\n")
        output_file.write("#deck:Reinforcement Learning\n")
        output_file.write("#columns:ID\tFront\tBack\tTags\n")
        output_file.write("#tags column:4\n")

        writer = csv.writer(output_file, delimiter="\t", lineterminator="\n")
        writer.writerows(cards)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Obsidian flashcards to an Anki-compatible TSV file."
    )
    parser.add_argument("input", type=Path, help="Markdown flashcard file")
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        help="Output TSV file (defaults to the input filename with .tsv)",
    )
    args = parser.parse_args()

    output_path = args.output or args.input.with_suffix(".tsv")
    markdown = args.input.read_text(encoding="utf-8")
    cards = parse_cards(markdown)
    write_tsv(cards, output_path)
    print(f"Converted {len(cards)} card(s) to {output_path}")


if __name__ == "__main__":
    main()