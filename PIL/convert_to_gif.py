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
from PIL import Image

def get_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-i", "--infile", required=True, help="The image file to convert.")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    infile = args.infile
    pic = Image.open(infile)
    outfile_name = os.path.splitext(infile)[0] + ".gif"
    print(outfile_name)
    pic.save(outfile_name)
    print("Created {}.".format(outfile_name))

if __name__ == "__main__":
    main()
