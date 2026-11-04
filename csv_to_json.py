"""Convert CSV files to JSON."""
import csv
import json
import argparse


def csv_to_json(csv_path: str) -> list:
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def main():
    parser = argparse.ArgumentParser(description="Convert CSV to JSON.")
    parser.add_argument("csv_file", help="Path to CSV file")
    parser.add_argument("-o", "--output", help="Output JSON file (default: stdout)")
    args = parser.parse_args()
    data = csv_to_json(args.csv_file)
    result = json.dumps(data, indent=2)
    if args.output:
        with open(args.output, "w") as f:
            f.write(result)
        print(f"Written to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
