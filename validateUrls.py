#! /usr/bin/python

import sys
import argparse
from sortfunctions.comparators import alpha, length
from urltools import validator, normalizer

# Returns whether a url is unique in the given list using given comparator
def is_unique(url, list, cmp):
    occurrences = filter(lambda x: cmp(url, x)==0, list)
    return len(occurrences) == 1

"""
Main

Parse command line arguments and run validation and normalization.
"""
if __name__ == "__main__":
    comparators = { 'alpha': alpha, 'length': length }
    
    parser = argparse.ArgumentParser(description=
        """Validation Madness!
        Given an input file containing one URL per line, prints validation
        and normalization results for each URL to the terminal.""")
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-c', '--comparator', choices=comparators.keys(),
                        help='comparison function to define URL uniqueness (DEFAULT=alpha)')
    args = parser.parse_args()
    
    # read URLs from file
    urls = None
    try:
        urls = open(args.input).readlines()
        urls = [x.strip() for x in urls]
    except IOError:
        print "Error: File \"%s\" not found." % args.input
        sys.exit()

    # default comparator is alpha
    cmp = comparators['alpha']
    if args.comparator is not None:
        cmp = comparators[args.comparator]
        
    # set of urls, normalized
    normUrls = normalizer.normalize_list(urls)
    
    # print results
    for i, url in enumerate(urls):
        normUrl = normUrls[i]
        print 'Source:               ', url
        print 'Valid:                ', validator.is_valid(url)
        print 'Canonicalized:        ', normUrl
        print 'Source unique:        ', is_unique(url, urls, cmp)
        print 'Canonicalized unique: ', is_unique(normUrl, normUrls, cmp)
        print
        