#!/usr/bin/env python3

import pandas as pd
import argparse


def trainModels(src):

    df = pd.read_csv(src)

    print(df.dtypes)

    # print(df.head(10))


if __name__ == "__main__":

    # parse command-line args
    parser = argparse.ArgumentParser(description='file')
    parser.add_argument("--src", help=".csv file to train a model")
    args = parser.parse_args()

    # run puppy, run
    trainModels(args.src)
