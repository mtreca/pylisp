def READ(x: str) -> str:
    return x


def EVAL(x: str) -> str:
    return x


def PRINT(x: str) -> str:
    return x


def REP(x: str) -> str:
    return PRINT(EVAL(READ(x)))


def main() -> int:
    while True:
        match input("user> "):
            case "exit":
                return 0
            case data:
                print(REP(data))


if __name__ == "__main__":
    main()
