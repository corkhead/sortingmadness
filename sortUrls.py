#! /usr/bin/python

import sys
import argparse
from urltools import validator, normalizer
from sortlib import *


"""
Main

Parse command line arguments and execute sort functions.
"""
if __name__ == "__main__":
    algos = {1: insertionsort, 2: mergesort, 3: quicksort, 4: bucketsort,
             5: selectionsort_alphabetical, 6: radixsort_alphabetical,
             7: mergesort_alphabetical, 8: heapsort_alphabetical}

    parser = argparse.ArgumentParser(description="""Sorting Madness!
        Given an input file containing one url per line, prints the sorted list
        of urls to the output file. The desired sorting algorithm can be supplied as
        a command-line argument. The default is quicksort.

        You may also specify if you wish to only sort valid or invalid urls.
        Note: If one of the validation options is chosen, all output urls will be normalized.""")
    parser.add_argument('-i', '--input', help='the input file', required=True)
    parser.add_argument('-o', '--output', help='the output file', required=True)
    parser.add_argument('-s', '--sort', type=int,
                        choices=list(range(1,len(algos)+1)),
                        help='the sorting algorithm. \
                        Must be an integer. possible values are:\n' +
                        '\n'.join(['%d:%s' % (k, algos[k].__name__) for k in algos.keys()]) )
    parser.add_argument('-f', '--filter', help='filter on which urls to sort',
                        choices=['valid', 'invalid']);
    args = parser.parse_args()

    outfile = None
    urls = None

    try:
        outfile = open(args.output, 'w')
    except IOError:
        print "Error: Unable to open output file \"%s\"." % args.output
        sys.exit()

    try:
        urls = open(args.input).readlines()
    except IOError:
        print "Error: File \"%s\" not found." % args.input
        sys.exit()

    sel = 3  # default selection is quicksort
    if args.sort is not None: # try getting sort selection from command-line args
        sel = args.sort

    # remove leading/trailing whitespace from urls
    urls = [x.strip() for x in urls]

    # normalize and validate urls, if specified
    if args.filter is not None:
        validUrls = validator.valid_list(urls)
        if args.filter == 'valid':
            urls = normalizer.normalize_list(validUrls)
        elif args.filter == 'invalid':
            urls = filter(lambda x: x not in validUrls, urls)

    sorter = algos[sel](urls)
    sortedList = sorter.sort()
    outfile.write("\n".join(sortedList))
