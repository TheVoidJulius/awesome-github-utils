"""Count words, lines, and characters in a text file."""
import argparse


def count_stats(filepath: str) -> dict:
    """Return word, line, and character counts for a file."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return {
        "lines": text.count("\n") + (1 if text and not text.endswith("\n") else 0),
        "words": len(text.split()),
        "characters": len(text),
    }


def main():
    parser = argparse.ArgumentParser(description="Count words, lines, and characters.")
    parser.add_argument("file", help="Path to the text file")
    args = parser.parse_args()
    stats = count_stats(args.file)
    print(f"  Lines:      {stats['lines']}")
    print(f"  Words:      {stats['words']}")
    print(f"  Characters: {stats['characters']}")


if __name__ == "__main__":
    main()
