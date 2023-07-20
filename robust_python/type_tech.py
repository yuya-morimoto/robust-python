from typing import Final, Optional, Self


class Bun():
    name: str

    def __init__(self, name: str) -> None:
        self.name = name


def create_bun(name: str) -> Optional[Bun]:
    if name != "":
        return Bun(name=name)

    return None


def main() -> None:
    print("start!!")

    bun = create_bun("")

    print(bun)

    print("finish!!")


if __name__ == "__main__":
    main()
