#echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    s = ""
    l = len(text)
    for i in range(repetitions):
        num = repetitions - i
        s = s + text[l-num:l] + "\n"
    s = s + "."
    return s


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))