"""Pretty-print JSON from the command line."""
import json
import sys
import argparse


def format_json(data: str, indent: int = 2) -> str:
    """Parse and pretty-print a JSON string."""
    parsed = json.loads(data)
    return json.dumps(parsed, indent=indent, sort_keys=True)


def main():
    parser = argparse.ArgumentParser(description="Pretty-print JSON.")
    parser.add_argument("file", nargs="?", help="JSON file (reads stdin if omitted)")
    parser.add_argument("--indent", type=int, default=2, help="Indentation level")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r") as f:
            raw = f.read()
    else:
        raw = sys.stdin.read()

    print(format_json(raw, args.indent))


if __name__ == "__main__":
    main()
