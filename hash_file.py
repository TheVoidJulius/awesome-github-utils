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
