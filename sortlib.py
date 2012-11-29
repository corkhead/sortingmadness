from sortfunctions import *

def insertionsort(*args):
    return insertionSort.InsertionSort(*args)

def mergesort(*args):
    return mergeSort.MergeSort(*args)

def quicksort(*args):
    return quickSort.QuickSort(*args)

def bucketsort(*args):
    return bucketSort.BucketSort(*args)

def selectionsort_alphabetical(*args):
    return alphabeticalSelectionSort.AlphabeticalSelectionSort(*args)

def radixsort_alphabetical(*args):
    return alphabeticalRadixSort.AlphabeticalRadixSort(*args)

def mergesort_alphabetical(*args):
    return alphabeticalMergeSort.AlphabeticalMergeSort(*args)

def heapsort_alphabetical(*args):
    return alphabeticalHeapSort.AlphabeticalHeapSort(*args)