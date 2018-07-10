#!/usr/bin/env python3                                                                                 
# -*- coding: utf-8 -*-                                                                                
                                                                                                       
###                                                                                                    
# © 2018 The Board of Trustees of the Leland Stanford Junior University                                
# Nathaniel Watson                                                                                     
# nathankw@stanford.edu                                                                                
###

"""
Creates a thumbnail for an image. The aspect ration will be preserved. 
"""

import argparse
import os
from PIL import Image # For making thumbnails

def get_parser():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-i", "--images", required=True, nargs="+", help="""
    One or more images to convert to thumbnails.""")
    parser.add_argument("-s", "--size", type=int, default=100, help="""
    The desired size for the thumbnail in pixels for the width and the height.""")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    size = args.size
    images = args.images
    for i in images:
        make_thumb(i, size)


def make_thumb(image, size):
    image_name, image_ext = os.path.splitext(image)
    thumbnail_name = "{}_thumb_{}{}".format(image_name, size, image_ext)
    imgobj = Image.open(image)
    # This method calculates an appropriate thumbnail size to preserve the aspect ratio.
    # See https://pillow.readthedocs.io/en/3.1.x/reference/Image.html. 
    imgobj.thumbnail((size,size), Image.ANTIALIAS) # best downsize filter
    imgobj.save(thumbnail_name)

if __name__ == "__main__":
    main()
