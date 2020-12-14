"""It sure is a sunny day! \N{SUN}"""
import re as _re  # I don't want others to get this!
import sys as _sys


def hello_world(name: str) -> None:
    """Hello there."""
    print(f"Hello, {name}")


SOME_RE = re.compile(r"T[hat]{3}Xliner\n")

if __name__ == "__main__":
    if not SOME_RE.match(sys.argv[1]):
        hello_world(sys.argv[1])
    else:
        print("You are cool!")  # Haha, vanity
        # NOTE: Reduce the vanity
