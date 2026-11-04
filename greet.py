"""A friendly greeting script."""
import argparse


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}! 👋"


def main():
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
