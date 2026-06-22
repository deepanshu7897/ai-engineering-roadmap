import argparse


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main():
    parser = argparse.ArgumentParser(
        description="Simple CLI Greeting App"
    )

    parser.add_argument(
        "--name",
        required=True,
        help="Your name"
    )

    args = parser.parse_args()

    print(greet(args.name))


if __name__ == "__main__":
    main()