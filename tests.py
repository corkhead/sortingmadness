#! /usr/bin/env python
import unittest
import sortUrls
from sortfunctions.comparators import alpha, length
from urltools import validator, normalizer

class TestUrlSorting(unittest.TestCase):

    #Setup for the tests, runs automatically before each test
    def setUp(self):
        #A list of urls to sort
        self.urls = ["www.google.com", "http://www.google.com", "a", "blarg@gmail.com", "facebook.com", "CS.WASHINGTON.EDU", "HTTPS://WWW.YAHOO.COM/"]
        #Expected output of validator
        self.validUrls = ["http://www.google.com", "HTTPS://WWW.YAHOO.COM/"]
        #Expected output of the sort-by-length functions
        self.sortedByLength = ["a", "facebook.com", "www.google.com", "blarg@gmail.com", "CS.WASHINGTON.EDU", "http://www.google.com", "HTTPS://WWW.YAHOO.COM/"]
        #Expected output of the sort-by-alphabetical functions
        self.sortedByAlphabetical = ["CS.WASHINGTON.EDU", "HTTPS://WWW.YAHOO.COM/", "a", "blarg@gmail.com", "facebook.com", "http://www.google.com", "www.google.com"]
        #Edge case where list is empty
        self.emptyUrls = []
        #Edge case where list has a single url
        self.singleUrl = ["google.com"]

    #Insertion Sort (by alpha, length) tests
    def test_insertionsort(self):
        sortedList = sortUrls.insertionsort(self.urls, length).sort()
        self.assertEquals(sortedList, self.sortedByLength)
        
        sortedList = sortUrls.insertionsort(self.urls, alpha).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)

    def test_insertionsort_empty(self):
        sortedList = sortUrls.insertionsort(self.emptyUrls, length).sort()
        self.assertEquals(sortedList, self.emptyUrls)
        
        sortedList = sortUrls.insertionsort(self.emptyUrls, alpha).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_insertionsort_single(self):
        sortedList = sortUrls.insertionsort(self.singleUrl, length).sort()
        self.assertEquals(sortedList, self.singleUrl)
        
        sortedList = sortUrls.insertionsort(self.singleUrl, alpha).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Merge Sort (by alpha, length) tests
    def test_mergesort(self):
        sortedList = sortUrls.mergesort(self.urls, length).sort()
        self.assertEquals(sortedList, self.sortedByLength)
        
        sortedList = sortUrls.mergesort(self.urls, alpha).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)

    def test_mergesort_empty(self):
        sortedList = sortUrls.mergesort(self.emptyUrls, length).sort()
        self.assertEquals(sortedList, self.emptyUrls)
        
        sortedList = sortUrls.mergesort(self.emptyUrls, alpha).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_mergesort_single(self):
        sortedList = sortUrls.mergesort(self.singleUrl, length).sort()
        self.assertEquals(sortedList, self.singleUrl)
        
        sortedList = sortUrls.mergesort(self.singleUrl, alpha).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Quick Sort (by alpha, length) tests
    def test_quicksort(self):
        sortedList = sortUrls.quicksort(self.urls, length).sort()
        self.assertEquals(sortedList, self.sortedByLength)
        
        sortedList = sortUrls.quicksort(self.urls, alpha).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)

    def test_quicksort_empty(self):
        sortedList = sortUrls.quicksort(self.emptyUrls, length).sort()
        self.assertEquals(sortedList, self.emptyUrls)
        
        sortedList = sortUrls.quicksort(self.emptyUrls, alpha).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_quicksort_single(self):
        sortedList = sortUrls.quicksort(self.singleUrl, length).sort()
        self.assertEquals(sortedList, self.singleUrl)
        
        sortedList = sortUrls.quicksort(self.singleUrl, alpha).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Bucket Sort (by length) tests
    def test_bucketsort(self):
        sortedList = sortUrls.bucketsort(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByLength)

    def test_bucketsort_empty(self):
        sortedList = sortUrls.bucketsort(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_bucketsort_single(self):
        sortedList = sortUrls.bucketsort(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Selection Sort (alphabetical) tests
    def test_selectionsort_alphabetical(self):
        sortedList = sortUrls.selectionsort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)

    def test_selectionsort_alphabetical_empty(self):
        sortedList = sortUrls.selectionsort_alphabetical(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_selectionsort_alphabetical_single(self):
        sortedList = sortUrls.selectionsort_alphabetical(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Radix Sort (alphabetical) tests
    def test_radixsort_alphabetical(self):
        sortedList = sortUrls.radixsort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)

    def test_radixsort_alphabetical_empty(self):
        sortedList = sortUrls.radixsort_alphabetical(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_radixsort_alphabetical_single(self):
        sortedList = sortUrls.radixsort_alphabetical(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Merge Sort (alphabetical) tests
    def test_mergesort_alphabetical(self):
        sortedList = sortUrls.mergesort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)

    def test_mergesort_alphabetical_empty(self):
        sortedList = sortUrls.mergesort_alphabetical(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_mergesort_alphabetical_single(self):
        sortedList = sortUrls.mergesort_alphabetical(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

    #Heap Sort (alphabetical) tests
    def test_heapsort_alphabetical(self):
        sortedList = sortUrls.heapsort_alphabetical(self.urls).sort()
        self.assertEquals(sortedList, self.sortedByAlphabetical)

    def test_heapsort_alphabetical_empty(self):
        sortedList = sortUrls.heapsort_alphabetical(self.emptyUrls).sort()
        self.assertEquals(sortedList, self.emptyUrls)

    def test_heapsort_alphabetical_single(self):
        sortedList = sortUrls.heapsort_alphabetical(self.singleUrl).sort()
        self.assertEquals(sortedList, self.singleUrl)

        
class TestUrlsComparators(unittest.TestCase):

    def test_comparator_length(self):
        res = length("asdfasdf", "asdf")
        self.assertEquals(res, 4)
        res = length("", "")
        self.assertEquals(res, 0)
        res = length("","asdf")
        self.assertEquals(res, -4)
        res = length("a", "")
        self.assertEquals(res, 1)
        res = length(".dfk1", "9)-.'")
        self.assertEquals(res, 0)
        res = length("a", "9358")
        self.assertEquals(res, -3)
        
    def test_comparator_alpha(self):
        res = alpha('', '')
        self.assertEquals(res, 0)
        res = alpha('fish', 'fish')
        self.assertEquals(res, 0)
        res = alpha('', '   ')
        self.assertEquals(res, -1)
        res = alpha('a', '')
        self.assertEquals(res, 1)
        res = alpha('a', '9358')
        self.assertEquals(res, 1)
        res = alpha('Aa', 'AA')
        self.assertEquals(res, 1)
        res = alpha('turnip', 'turnipfist')
        self.assertEquals(res, -1)
        res = alpha('turnipfist', 'turnip')
        self.assertEquals(res, 1)
        res = alpha('.dot', '42')
        self.assertEquals(res, -1)

class TestUrlNormalization(unittest.TestCase):

    def test_lowercase(self):
        url = 'HTTP://WWW.fakeurl.COM/testdir'
        exp = 'http://www.fakeurl.com/testdir'
        self.assertEquals(normalizer._lowercase(url), exp)
        self.assertEquals(normalizer._lowercase(exp), exp)
        
        url = 'HTTP://WWW.fakeurl.COM/testdir/fILE.ext'
        exp = 'http://www.fakeurl.com/testdir/fILE.ext'
        self.assertEquals(normalizer._lowercase(url), exp)

    def test_capitalize_escapes(self):
        url = 'http://WWW.example.com/a%c2%b1b'
        exp = 'http://WWW.example.com/a%C2%B1b'
        self.assertEquals(normalizer._capitalize_escapes(url), exp)
        
        url = 'http://WWW.example.com/a%C2%b1b'
        self.assertEquals(normalizer._capitalize_escapes(url), exp)
        
        url = 'http://WWW.example.com/a%z2%b12b'
        exp = 'http://WWW.example.com/a%z2%B12b'
        self.assertEquals(normalizer._capitalize_escapes(url), exp)

    def test_decode_unreserved(self):
        url = 'http://www.example.com/%7Eusername/'
        exp = 'http://www.example.com/~username/'
        self.assertEquals(normalizer._decode_unreserved(url), exp)
        
        url = 'http://www.example.com/%7E%75%73%65%72%6e%61%6d%65/'
        exp = 'http://www.example.com/~username/'
        self.assertEquals(normalizer._decode_unreserved(url), exp)
        
        url = 'http://www.example.com/%7Euser%34%32/'
        exp = 'http://www.example.com/~user42/'
        self.assertEquals(normalizer._decode_unreserved(url), exp)
        
        url = 'http://www.example.com/%40user%2b%21%34%32/'
        exp = 'http://www.example.com/%40user%2b%2142/'
        self.assertEquals(normalizer._decode_unreserved(url), exp)
        
    def test_remove_default_port(self):
        url = 'http://www.google.com:80/'
        exp = 'http://www.google.com/'
        self.assertEquals(normalizer._remove_default_port(url), exp)
        
        url = 'https://www.google.com:443/asdf'
        exp = 'https://www.google.com/asdf'
        self.assertEquals(normalizer._remove_default_port(url), exp)
        
        url = 'ftp://www.google.com:21/asdf21'
        exp = 'ftp://www.google.com/asdf21'
        self.assertEquals(normalizer._remove_default_port(url), exp)
        
        url = 'ftps://www.google.com:990/990.ext'
        exp = 'ftps://www.google.com/990.ext'
        self.assertEquals(normalizer._remove_default_port(url), exp)
        
        url = 'ftps://www.google.com:42/'
        exp = url
        self.assertEquals(normalizer._remove_default_port(url), exp)

    def test_add_trailing_slash(self):
        url1 = 'http://www.fakeurl.com/testfile.html'
        exp1 = url1
        url2 = 'http://www.fakeurl.com/testdir'
        exp2 = 'http://www.fakeurl.com/testdir/'
        self.assertEquals(normalizer._add_trailing_slash(url1), exp1)
        self.assertEquals(normalizer._add_trailing_slash(url2), exp2)

    def test_remove_dot_segments(self):
        url = 'http://www.testsite.com/dir1/dir2a/../dir2b/./file.txt'
        exp = 'http://www.testsite.com/dir1/dir2b/file.txt'
        self.assertEquals(normalizer._remove_dot_segments(url), exp)
        
        url = 'http://stuff.com/path//////'
        exp = 'http://stuff.com/path'
        self.assertEquals(normalizer._remove_dot_segments(url), exp)

    def test_remove_empty_querystring(self):
        url = 'http://www.google.com/?'
        exp = 'http://www.google.com/'
        self.assertEquals(normalizer._remove_empty_querystring(url), exp)
        
        url = 'http://www.google.com/?q'
        exp = url
        self.assertEquals(normalizer._remove_empty_querystring(url), exp)

class TestUrlValidation(unittest.TestCase):

    def test_valid(self):
        urls = ['https://stuff.com', 'http://stuff.com', 'ftp://stuff.com', 'ftps://stuff.com', 'http://stuff.com/path//////', 'http://stuff.com/path.more/file.ext', 'http://stuff.com/path?q=wat+stuff', 'http://stuff.com/path#frag', 'http://stuff.com/path?q#frag', 'ftp://ftp.epcc.ed.ac', 'http://a.bc', 'http://a.bcdefg', 'http://a.bcde-fgh', 'http://a.b.c.ef', 'http://2001.0db8.85a3.0000.0000.8a2e.0370.7334', 'http://zzzz.gggg.eeee.9999.1234.mmmm.aaaa.wwww', 'http://123.1.2.3', 'http://999.999.999.999', 'http://999.999.999.999:99999', 'http://localhost', 'http://123456789012345678901234567890123456789012345678901234567890123.com']
        for url in urls:
            self.assertTrue(validator.is_valid(url))

    def test_invalid(self):
        urls = ['://stuff.com', '//stuff.com', 'stuff.com', 'www.stuff.com', 'http://', 'http:', 'http', 'ftp://username@ftp.example.org', 'ftp://username@ftp.example.org/path?q#frag', 'ftp://ftp.epcc.ed.ac.uk ', 'http://a', 'http://a.', 'http://a.b', 'http://a:a.b', 'http://a/b.c/ef.gh', 'http://999.999.999.999:123ab', 'http://999.999.999.999:-12', 'http://1234567890123456789012345678901234567890123456789012345678901234.com']
        for url in urls:
            self.assertFalse(validator.is_valid(url))
        
    def test_validate_list(self):
        urls = ["www.google.com", "http://www.google.com", "a", "blarg@gmail.com", "facebook.com", "CS.WASHINGTON.EDU", "HTTPS://WWW.YAHOO.COM/"]
        validUrls = ["http://www.google.com", "HTTPS://WWW.YAHOO.COM/"]
        res = validator.valid_list(urls)
        self.assertEquals(res, validUrls)

if __name__ == "__main__":
    unittest.main()
