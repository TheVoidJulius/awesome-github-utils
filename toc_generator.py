"""Generate a Table of Contents from a Markdown file."""
import re
import argparse


def generate_toc(filepath: str) -> str:
    toc_lines = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"^(#{1,6})\s+(.+)", line)
            if match:
                level = len(match.group(1)) - 1
                title = match.group(2).strip()
                anchor = re.sub(r"[^\w\s-]", "", title).lower().replace(" ", "-")
                toc_lines.append(f"{'  ' * level}- [{title}](#{anchor})")
    return "\n".join(toc_lines)


def main():
    parser = argparse.ArgumentParser(description="Generate a Markdown TOC.")
    parser.add_argument("file", help="Markdown file")
    args = parser.parse_args()
    print(generate_toc(args.file))


if __name__ == "__main__":
    main()
