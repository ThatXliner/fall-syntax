import math
import re
import sys
from pathlib import Path
from typing import Tuple

PROJECT_DIR = Path(__file__).parent.absolute()
assert PROJECT_DIR.name == "fall-syntax", PROJECT_DIR


def get_rel_luminance(R, G, B) -> float:
    _ = (
        lambda x: (x / 255) / 12.92
        if (x / 255) <= 0.03928
        else math.pow((((x / 255) + 0.055) / 1.055), 2.4)
    )
    return 0.2126 * _(R) + 0.7152 * _(G) + 0.0722 * _(B)


def get_contrast_ratio(
    fore: Tuple[float, float, float], back: Tuple[float, float, float]
) -> float:
    """As described in https://www.w3.org/TR/WCAG20-TECHS/G17.html#G17-procedure"""

    return (get_rel_luminance(*back) + 0.05) / (get_rel_luminance(*fore) + 0.05)


def convert_hex_to_rgb(hex_str: str) -> Tuple[int, int, int]:
    R = int(hex_str[0:2], base=16)
    G = int(hex_str[2:4], base=16)
    B = int(hex_str[4:6], base=16)
    return R, G, B


assert convert_hex_to_rgb("112A46") == (17, 42, 70)


TARGET_RATIO = 7
assert round(get_contrast_ratio((17, 42, 70), (172, 200, 229)), 2) == 8.42

COLOR_RE = re.compile(
    r"^@(?P<name>[^:]+):\s*#(?P<hex>[a-zA-Z0-9]{6});", flags=re.MULTILINE
)
FALL_COLORS_RE = re.compile(r".+-color")
BG_RE = re.compile(r"^@syntax-bg:\s*#(?P<hex>[a-zA-Z0-9]{6});", flags=re.MULTILINE)

if __name__ == "__main__":
    print("===TEST SESSION START===")
    print("Validating colors defined in styles/colors.less")
    print()
    print(f"Target ratio: >= {TARGET_RATIO}")
    print("========================")
    print()
    print("READING styles/colors.less")
    colors_less = PROJECT_DIR.joinpath("styles").joinpath("colors.less")
    # assert colors_less.exists() and colors_less.is_file(), (
    #     colors_less,
    #     colors_less.exists(),
    #     colors_less.is_file(),
    # )
    colors_less_contents = colors_less.read_text()

    print("FINDING background color")
    background_color = convert_hex_to_rgb(BG_RE.search(colors_less_contents)["hex"])

    print(f"Background color: rgb{background_color}")
    failing_colors = 0
    for color in COLOR_RE.finditer(colors_less_contents):
        cname, chex = color["name"], color["hex"]
        if not FALL_COLORS_RE.match(cname):
            continue

        print(f"Validating @{cname} (#{chex})...", end=" ", flush=True)

        crgb = convert_hex_to_rgb(chex)
        contrast_ratio = get_contrast_ratio(background_color, crgb)
        if not contrast_ratio >= TARGET_RATIO:
            print(
                f"\N{COLLISION SYMBOL} Failing color:\nName: {cname}\nHex: {chex}\nContrast ratio: {contrast_ratio}"
            )
            failing_colors += 1
            continue
        print("\N{WHITE HEAVY CHECK MARK} Good!")

    if failing_colors > 0:
        print(f"\N{COLLISION SYMBOL} {failing_colors} colors failed")
        print("===TEST SESSION END===")
        sys.exit(1)
    print("\N{WHITE HEAVY CHECK MARK} All done!")
    print("===TEST SESSION END===")
    sys.exit(0)
