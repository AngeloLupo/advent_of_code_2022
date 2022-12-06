def detect_start(signal: str, size: int) -> int:
    for i in range(size, len(signal)):
        if len(set(signal[i - size:i])) == size:
            return i


if __name__ == "__main__":

    incoming_signal = open("src/day6/input").read()

    print(detect_start(incoming_signal, 4))
    print(detect_start(incoming_signal, 14))

