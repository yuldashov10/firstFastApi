import csv
import sys

from tabulate import tabulate


def read_csv(filename: str) -> list[tuple]:
    with open(filename, mode="r", encoding="UTF-8") as file:
        data = [tuple(row) for row in csv.reader(file, delimiter="|")]

    return data


if __name__ == "__main__":
    data = read_csv(sys.argv[1])
    print(tabulate(data[0:8]))
