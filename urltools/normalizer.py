##################################################
# URL Normalization methods                      #
##################################################
import re
import posixpath
from urllib import unquote
from urlparse import urlparse, urlunparse

# normalizations that preserve semantics

def _lowercase(url):
    """Convert the scheme and host to lowercase"""
    res = urlparse(url)
    norm = (res.scheme.lower(), res.netloc.lower(), res.path, res.params, res.query, res.fragment)
    return urlunparse(norm)

def _capitalize_escapes(url):
    # find and replace left-to-right
    escapes = re.findall("%[0-9A-Fa-f]{2}", url)
    for escape in escapes:
        url = re.sub(escape, escape.upper(), url)
    return url

# Helper function for detecting unreserved characters
def _is_unreserved(val):
    is_alpha = (val >= 0x41 and val <= 0x5a) or (val >= 0x61 and val <= 0x7a)
    is_digit = val >= 0x30 and val <= 0x39
    return is_alpha or is_digit or \
           val==0x2d or val==0x2e or val==0x5f or val==0x7e

def _decode_unreserved(url):
    escapes = re.findall("%[0-9A-Fa-f]{2}", url)
    for escape in escapes:
        hex_val = int(escape[1:], 16)
        if _is_unreserved(hex_val):
            url = re.sub(escape, unquote(escape), url)
    return url

# Default port mappings for supported schemes
scheme_to_port = { 'http': 80,
                   'https': 443,
                   'ftp': 21,
                   'ftps': 990 }

def _remove_default_port(url):
    res = urlparse(url)
    
    # remove if the port number matches the default
    if (res.scheme in scheme_to_port.keys() and scheme_to_port[res.scheme] == res.port):
        return re.sub(r'(?::\d+)?', '', url)
    else:
        return url

# normalizations that usually preserve semantics

def _remove_dot_segments(url):
    # Note: add trailing slash must be called after this method, since this method
    # will remove trailing slashes.
    # Also, urlparse only gives us a good path element for urls whose scheme is specified
    # this is fine for now since scheme-less urls will fail validation anyway
    res = urlparse(url)
    path = res.path

    if res.scheme != '' and res.path != '':
        path = posixpath.abspath(path)

    norm = (res.scheme, res.netloc, path, res.params, res.query, res.fragment)
    return urlunparse(norm)

def _add_trailing_slash(url):
    # no way to be sure if url path ends in a directory. Here we treat as a directory
    # anything that doesn't contain a .
    if re.search(r'/\w*\.\w*$', url):
        return url   # it's a file, probably

    res = urlparse(url)
    if res.params != '' or res.query != '' or res.fragment != '':
        return url  # it has stuff after the path

    if url[len(url) - 1] != '/':
        url = url + '/'

    return url

# normalizations that change semantics

def _remove_empty_querystring(url):
    if len(url) == 0:
        return url

    if url[len(url) - 1] == r'?':
        url = url[:-1]
    return url

# Order of normalization execution
normalizations = [_lowercase,
                  _capitalize_escapes,
                  _decode_unreserved,
                  _remove_default_port,
                  _remove_dot_segments,
                  _add_trailing_slash,
                  _remove_empty_querystring]

# Given a single URL, returns the normalized form of the URL
def normalize(url):
    result = url
    for norm_fn in normalizations:
        result = norm_fn(result)
    return result

# Given a list of URLs, returns a list of normalized URLs
def normalize_list(urls):
    result = []
    for url in urls:
        result.append(normalize(url))
    return result
