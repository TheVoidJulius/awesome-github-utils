# Script to create more features, close issues, and star repos

$repoDir = "c:\Users\pawan\broke\awesome-github-utils"
Set-Location $repoDir

# ============================================
# FEATURE 5: Add requirements.txt (closes #6)
# ============================================
git checkout main
git checkout -b fix/add-requirements

@"
# No external dependencies required yet.
# This file is included for best practices.
"@ | Set-Content -Path "$repoDir\requirements.txt" -Encoding UTF8

git add -A
git commit -m "chore: add requirements.txt - Closes #6"
git push -u origin fix/add-requirements

# ============================================
# FEATURE 6: Add .gitignore (closes #8)
# ============================================
git checkout main
git checkout -b fix/add-gitignore

@"
__pycache__/
*.py[cod]
*`$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec
pip-log.txt
pip-delete-this-directory.txt
.env
.venv
env/
venv/
ENV/
.idea/
.vscode/
*.swp
*.swo
*~
.DS_Store
Thumbs.db
"@ | Set-Content -Path "$repoDir\.gitignore" -Encoding UTF8

git add -A
git commit -m "chore: add Python .gitignore - Closes #8"
git push -u origin fix/add-gitignore

# ============================================
# FEATURE 7: Add hash_file.py utility
# ============================================
git checkout main
git checkout -b feature/add-hash-file

@"
"""Calculate file hashes (MD5, SHA1, SHA256)."""
import hashlib
import argparse


def hash_file(filepath: str, algorithm: str = "sha256") -> str:
    h = hashlib.new(algorithm)
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Calculate file hash.")
    parser.add_argument("file", help="File to hash")
    parser.add_argument("--algo", default="sha256", choices=["md5", "sha1", "sha256", "sha512"])
    args = parser.parse_args()
    print(f"{args.algo}: {hash_file(args.file, args.algo)}")


if __name__ == "__main__":
    main()
"@ | Set-Content -Path "$repoDir\hash_file.py" -Encoding UTF8

git add -A
git commit -m "feat: add hash_file.py for file checksums"
git push -u origin feature/add-hash-file

# ============================================
# FEATURE 8: Add base64_tool.py
# ============================================
git checkout main
git checkout -b feature/add-base64-tool

@"
"""Encode and decode Base64 strings."""
import base64
import argparse


def encode(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


def decode(text: str) -> str:
    return base64.b64decode(text.encode()).decode()


def main():
    parser = argparse.ArgumentParser(description="Base64 encode/decode.")
    parser.add_argument("action", choices=["encode", "decode"])
    parser.add_argument("text", help="Text to encode/decode")
    args = parser.parse_args()
    if args.action == "encode":
        print(encode(args.text))
    else:
        print(decode(args.text))


if __name__ == "__main__":
    main()
"@ | Set-Content -Path "$repoDir\base64_tool.py" -Encoding UTF8

git add -A
git commit -m "feat: add base64_tool.py encoder/decoder"
git push -u origin feature/add-base64-tool

Write-Output "=== Round 2 branches pushed ==="
