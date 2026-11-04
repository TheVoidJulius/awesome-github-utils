# Script to create multiple feature branches, commits, PRs, and issues
# for GitHub achievement hunting

$repoDir = "c:\Users\pawan\broke\awesome-github-utils"

# ============================================
# FEATURE 2: Password Generator
# ============================================
Set-Location $repoDir
git checkout main
git pull origin main
git checkout -b feature/add-password-generator

@"
"""Generate random secure passwords."""
import argparse
import secrets
import string


def generate_password(length: int = 16, use_special: bool = True) -> str:
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation
    return "".join(secrets.choice(chars) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument("--length", type=int, default=16, help="Password length")
    parser.add_argument("--no-special", action="store_true", help="Exclude special chars")
    args = parser.parse_args()
    print(generate_password(args.length, not args.no_special))


if __name__ == "__main__":
    main()
"@ | Set-Content -Path "$repoDir\password_generator.py" -Encoding UTF8

git add -A
git commit -m "feat: add password_generator.py"
git push -u origin feature/add-password-generator

# ============================================
# FEATURE 3: CSV to JSON converter
# ============================================
git checkout main
git checkout -b feature/add-csv-to-json

@"
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
"@ | Set-Content -Path "$repoDir\csv_to_json.py" -Encoding UTF8

git add -A
git commit -m "feat: add csv_to_json.py converter"
git push -u origin feature/add-csv-to-json

# ============================================
# FEATURE 4: Markdown TOC generator
# ============================================
git checkout main
git checkout -b feature/add-toc-generator

@"
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
"@ | Set-Content -Path "$repoDir\toc_generator.py" -Encoding UTF8

git add -A
git commit -m "feat: add toc_generator.py for Markdown files"
git push -u origin feature/add-toc-generator

Write-Output "=== All feature branches pushed ==="
