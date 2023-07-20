from collections import Counter


def main() -> None:
    print("start!!")

    users: list[dict[str, str]] = [
        {
            "id": "1",
            "name": "user-1"
        },
        {
            "id": "2",
            "name": "user-2"
        },
        {
            "id": "3",
            "name": "user-1"
        },
        {
            "id": "4",
            "name": "user-2"
        },
        {
            "id": "5",
            "name": "user-2"
        },
        {
            "id": "6",
            "name": "user-3"
        }
    ]

    count = Counter(user["name"] for user in users)

    print(count)

    print("finish!!")


if __name__ == "__main__":
    main()
