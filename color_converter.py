"""Convert colors between HEX, RGB, and HSL formats."""
import argparse
import colorsys


def hex_to_rgb(hex_color: str) -> tuple:
    """Convert HEX color to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert RGB values to HEX string."""
    return f"#{r:02x}{g:02x}{b:02x}"


def rgb_to_hsl(r: int, g: int, b: int) -> tuple:
    """Convert RGB to HSL."""
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    return round(h * 360), round(s * 100), round(l * 100)


def hex_to_hsl(hex_color: str) -> tuple:
    """Convert HEX to HSL."""
    return rgb_to_hsl(*hex_to_rgb(hex_color))


def main():
    parser = argparse.ArgumentParser(description="Convert colors.")
    parser.add_argument("color", help="Color value (e.g., #ff5733 or 255,87,51)")
    parser.add_argument("--to", choices=["hex", "rgb", "hsl"], default="rgb")
    args = parser.parse_args()

    if args.color.startswith("#"):
        r, g, b = hex_to_rgb(args.color)
        if args.to == "rgb":
            print(f"RGB({r}, {g}, {b})")
        elif args.to == "hsl":
            h, s, l = hex_to_hsl(args.color)
            print(f"HSL({h}, {s}%, {l}%)")
        else:
            print(args.color)
    else:
        r, g, b = map(int, args.color.split(","))
        if args.to == "hex":
            print(rgb_to_hex(r, g, b))
        elif args.to == "hsl":
            h, s, l = rgb_to_hsl(r, g, b)
            print(f"HSL({h}, {s}%, {l}%)")
        else:
            print(f"RGB({r}, {g}, {b})")


if __name__ == "__main__":
    main()
