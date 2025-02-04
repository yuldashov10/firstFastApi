import sys

import pandas as pd


def read_pandas(filename: str, sep: str = "|") -> pd.DataFrame:
    return pd.read_csv(filename, sep=sep)


if __name__ == "__main__":
    data = read_pandas(sys.argv[1])
    print(data.head(5))
