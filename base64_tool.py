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
