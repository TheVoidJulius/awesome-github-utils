"""Organize files in a directory by their extension."""
import os
import shutil
import argparse


def organize(directory: str) -> dict:
    """Move files into sub-folders named after their extension."""
    moved = {}
    for fname in os.listdir(directory):
        fpath = os.path.join(directory, fname)
        if os.path.isfile(fpath):
            ext = os.path.splitext(fname)[1].lstrip(".") or "no_extension"
            dest_dir = os.path.join(directory, ext)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(fpath, os.path.join(dest_dir, fname))
            moved.setdefault(ext, []).append(fname)
    return moved


def main():
    parser = argparse.ArgumentParser(description="Organize files by extension.")
    parser.add_argument("directory", help="Directory to organize")
    args = parser.parse_args()
    result = organize(args.directory)
    for ext, files in result.items():
        print(f"  .{ext}: {len(files)} file(s)")


if __name__ == "__main__":
    main()
