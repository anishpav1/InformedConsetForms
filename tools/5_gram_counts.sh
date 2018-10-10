#!/usr/bin/env bash

FILE_DIR='../ALL_TEXT'
OUTPUT_DIR='../OUT'

# envoke word counts for each file in dir
for FILE in ${FILE_DIR}/*.txt
  do
    BASE="${FILE##*/}"
    OUTPUT="${BASE%.*}_output.csv"

    python3 n_gram_counter.py 5 ${FILE} > ${OUTPUT_DIR}/${OUTPUT}
  done
