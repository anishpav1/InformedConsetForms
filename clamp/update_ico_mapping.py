#!/usr/bin/env python

import argparse
import os
import xml.dom.minidom
import lxml.etree as etree

def clean_up(input):

    print_list = []

    tree = etree.parse(input)

    for node in tree.iter():

        line = str(node.tag) + ": " + str(node.attrib)
        print_list.append(line)

    with open('ico_mappings.txt', mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(print_list))


if __name__ == "__main__":

    # # parse command-line args
    parser = argparse.ArgumentParser(description='file')
    parser.add_argument("--input", help="Choose the xml file to process.")
    args = parser.parse_args()

    # # run puppy, run
    clean_up(args.input)
