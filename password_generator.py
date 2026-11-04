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
