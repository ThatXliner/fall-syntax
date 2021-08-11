"""It sure is a sunny day! \N{SUN}"""
import re as _re  # I don't want others to get this!
import sys as _sys


def hello_world(name: str) -> None:
    """Hello there."""
    print(f"Hello, {name}")


class Greeter(object):
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        """The name of this class."""
        return self._name

    @name.setter
    def name(self, new_value: str) -> None:
        self._name = new_value

    def greet(self) -> None:
        hello_world(name=self._name)


SOME_RE = _re.compile(r"T[hat]{3}Xliner")

if __name__ == "__main__":
    if not SOME_RE.match(_sys.argv[1]):
        hello_world(_sys.argv[1])
    else:
        print("You are cool!")  # Haha, vanity
        # NOTE: Reduce the vanity
