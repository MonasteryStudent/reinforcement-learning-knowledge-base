# Reinforcement Learning Knowledge Base

A personal reinforcement learning knowledge base designed for use with [Obsidian](https://obsidian.md/) and [Anki](https://apps.ankiweb.net/).

The vault documents my learning progress in reinforcement learning and currently focuses on its mathematical foundations.

The knowledge base is organized by chapter, with separate notes for concepts and flashcards.

Open the repository folder as an Obsidian vault to browse the concept notes. The flashcards are maintained as Markdown files and can be converted for import into Anki.

> **Note:** Some LaTeX expressions and Obsidian-specific syntax may not render correctly in GitHub's Markdown preview.

## Flashcards

Each chapter contains a `Flashcards.md` file with questions about definitions, mathematical formulations, and conceptual understanding.

The script `scripts/convert_flashcards.py` converts these Markdown files into tab-separated files for import into Anki.

### Conversion

The converter requires Python 3.10 or newer.

Run the following command from the repository root:

```bash
python scripts/convert_flashcards.py "01-Basics/Flashcards.md"
```

This creates or overwrites `Flashcards.tsv` in the same chapter directory.

### Anki setup

Create a deck named `Reinforcement Learning` and a note type named `RL Basic`, based on Anki's `Basic` note type.

The note type must contain these fields in this order:

1. `ID`
2. `Front`
3. `Back`

Import the generated TSV file into Anki and verify the field mapping.

Maintain the cards in the Markdown files and regenerate the TSV files after making changes. When adding new cards, follow the card template and use an ID consisting of the chapter number and a consecutive card number, such as `02-001`.

Card numbering starts at `001` in each chapter. The chapter prefix ensures that the complete ID remains unique across the knowledge base.

When importing revised cards, select `Update` for existing notes and `Note Type` as the match scope.

Card IDs must remain stable so that subsequent imports update existing notes without creating duplicates. Do not renumber existing cards or reuse deleted IDs.

## References

- *Mathematical Foundations of Reinforcement Learning* by Shiyu Zhao