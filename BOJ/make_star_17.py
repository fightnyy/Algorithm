import sys


def main():
    input = sys.stdin.readline
    num = int(input())
    for i in range(num):
        if i == 0:
            print(" " * (num - 1) + "*")
        elif i == (num) - 1:
            print("*" * ((2 * num) - 1))
        else:
            print(" " * (num - i - 1) + "*" + " " * (2 * i - 1) + "*")


if __name__ == "__main__":
    main()
