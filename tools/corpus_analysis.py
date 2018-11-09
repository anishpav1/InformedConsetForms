#!/usr/bin/env python3

import sys
import os
import pandas as pd
import argparse

def getCounts(d):

    new_rows = []

    for subdir, dirs, files in os.walk(d):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".txt"):
                try:
                    print('SUCCESS: ', str(filepath))
                    with open(filepath, encoding='utf-8') as f:
                        file_contents = f.read()

                        row = {
                            'filename': file,
                            'word_count':len(file_contents.split()),
                            'period_count':file_contents.count('.'),
                            'permission_mentions':file_contents.count('permission'),
                            'obligation_mentions':file_contents.count('obligation'),
                            'research_mentions':file_contents.count('research'),
                            'consent_mentions':file_contents.count('consent'),
                        }

                        new_rows.append(row)
                except Exception as e:
                    print('\n ERROR PROCESSING: ', str(filepath), '\n', e, '\n')
                    continue

    df = pd.DataFrame(new_rows)
    print(df.head(10))


if __name__ == "__main__":

    # parse command-line args
    parser = argparse.ArgumentParser(description='file')
    parser.add_argument("--d", help="Directory of .txt files")
    args = parser.parse_args()

    # run puppy, run
    getCounts(args.d)
