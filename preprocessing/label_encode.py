"""
=============================================
Title: label encode

Author(s): Alexandre Adam

Last modified: January 17, 2020

Description: Give unique label (integers) to synsets.
=============================================
"""
import numpy as np
import pandas as pd
import os

def main(datapath):
    pass

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, required=True, default="../../data/tiny-imagenet-200")
    args = parser.parse_args()
    
    main(args.datapath)
