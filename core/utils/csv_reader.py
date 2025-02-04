import csv
import sys


def read_csv(filename: str) -> list[tuple]:
    with open(filename, mode="r", encoding="UTF-8") as file:
        data = [tuple(row) for row in csv.reader(file, delimiter="|")]

    return data


if __name__ == "__main__":
    data = read_csv(sys.argv[1])
    for row in data[0:5]:
        print(row)
