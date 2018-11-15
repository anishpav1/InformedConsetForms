# Tools
This directory is a number of ad hoc tools used for exploratory data analysis. This tools are not robust and not intended to be used on other text corpus. Tools in this directory:

## [`corpus_analysis.py`](corpus_analysis.py)
A python3 command-line tool to generate a `.csv` file containing high-level data for all files in a specified directory. This command requires four positional arguments:
1. `--src` is the root directory for the search.
1. `--file_type` is the file type, specified as a string value corresponding to a valid extension (ex. '.txt').
1. `--keys` is an input `.csv` file containing search phrases, whose occurrences will be counted for each file in (1).
1. `--dest` is the name and destination of the output file. Example below:

```
./corpus_analysis.py --src ../data/ --file_type .txt --keys corpus_analysis_keys.csv --dest ./corpus_analysis_output.csv
```

## [`tf-idf.py`](tf-idf.py)
A python3 command-line tool to generate a `.csv` file containing a list of features computed using TF-IDF for each document in the input directory. This command requires the positional arguments:
1. `--src` is the root directory for the extraction.
1. `--file_type` is the file type, specified as a string value corresponding to a valid extension (ex. '.txt').
1. `--dest` is the name and destination of the output file. Example below:

```
./tf-idf.py --src ../data/ --file_type .txt --dest ./tfidf_output.csv
```

## [`form_classifier.py`](form_classifier.py)
A python3 command-line tool to generate a `.csv` file containing results for a number of `sklearn` models on the input data. This command requires two positional arguments:
1. `--src` the file to perform predictions on. Currently, this tool requires the output of [`corpus_analysis.py`](corpus_analysis.py) as its input.
1. `--dest` is the name and destination of the output file.

```
./form_classifier.py --src ./corpus_analysis_output.csv --dest form_classifier_results.csv
```

## [`n_gram_counter.py`](n_gram_counter.py)
A python3 command-line tool to generate a `.csv` file containing n-gram counts for a single input file. This command requires two positional arguments:
1. `--gram_size` the maximum number of grams to generate. All n-grams from 0 - `gram_size` will be generated.
1. `--input_file` is the file to process.

```
./n_gram_counter.py --gram_size 5 --input_file [input file]
```

## [`named_entity_extractor.py`](named_entity_extractor.py)
A python3 command-line tool to print untrained named entities from an input file using the python module `spaCy`. This command requires one positional argument:
1. `--input` the file to extract named entities from.

```
./named_entity_extractor --input [text file]
```
