#!/usr/bin/env python

import argparse
import csv

def main(args: argparse.Namespace) -> None:
    with open(args.input, "r") as source, open (args.col1, "w") as file1, open (args.col2, "w") as file2:
        my_data = csv.reader(source, delimiter="\t")
        for x, y in my_data:
            my_graphemes= " ".join(x)
            print(my_graphemes, file= file1)
            print(y, file= file2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        help="path to TSV file",
    )
    parser.add_argument(
        "col1",  help="path to output1 file"
    )
    parser.add_argument(
        "col2",  help="path to output file"
    )
    main(parser.parse_args())