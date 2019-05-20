#!/usr/bin/python
##   adapted to Python3 for ITC - 17/10/18
##       - also added pep8 and naming convention compliance
##
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request
import urllib.parse, urllib.error
import requests

FIRST_ARG = 1
LAST_ARG = 2
URL_FORMAT = 'http://%s%s'
IMAGE_TAG_FORMAT = '<img src="%s/img%d">'

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def sort_by_end_of_url(url):
    match = re.search(r'-([^-]*)$', url)
    return match.group(1)

def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    unique_paths = {}
    urls = []

    match = re.search(r'_(.*$)', filename)
    if match:
        hostname = match.group(1)
    else:
        print('something is wrong with the filename')
        return

    if os.path.isfile(filename):
        f = open(filename, 'r')
        f_content = f.read()
    else:
        print("File not found")
        return

    matches = re.findall(r'\s*(\S*puzzle\S*)\s*HTTP', f_content)
    for match in matches:
        if unique_paths.get(match) is None:
            unique_paths[match] = True
            urls.append(URL_FORMAT % (hostname, match))

    return sorted(urls, key=sort_by_end_of_url)


def generate_page(dest_dir, img_urls):
    imgs_tags = [IMAGE_TAG_FORMAT % (dest_dir, i) for i in range(len(img_urls))]
    img_html = "".join(imgs_tags)
    hmtl = '<verbatim>\n<html>\n<body>\n%s</body>\n</html>' % img_html
    f = open('index.html', 'w')
    f.write(hmtl)
    f.close()

def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
       each image into the given directory.
       Gives the images local filenames img0, img1, and so on.
       Creates an index.html in the directory
       with an img tag to show each local image file.
       Creates the directory if necessary.
    """
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    i = 0
    if img_urls is None:
        raise TypeError("We didn't get the urls because you probably provided a non existing file")

    for url in img_urls:
        print('Requesting : ' + url)
        file_path = os.path.join(dest_dir, 'img' + str(i))
        with open(file_path, 'wb') as f:
            resp = requests.get(url, verify=False)
            f.write(resp.content)
        # urllib.request.urlretrieve(url, file_path) was not working because ssl certification problem
        i += 1

    generate_page(dest_dir, img_urls)



def main():
    """ draw the logpuzzle pictures """
    try:
        args = sys.argv[FIRST_ARG:]

        if not args:
            print("usage: [--todir dir] logfile ")
            sys.exit(1)

        todir = ""
        if args[0] == "--todir":
            todir = args[FIRST_ARG]
            del args[0:LAST_ARG]

        img_urls = read_urls(args[0])

        if todir:
            download_images(img_urls, todir)
        else:
            print("\n".join(img_urls))
    except FileNotFoundError:
        print("Please provide an existing file")
    except TypeError as error:
        print(error)



if __name__ == "__main__":
    main()
