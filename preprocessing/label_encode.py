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
from pprint import pprint

def main(datapath):
    train_path = os.path.join(datapath, "train")
    val_path = os.path.join(datapath, "val")
    df = pd.read_csv(os.path.join(datapath, "words.txt"), sep="\t", names=["wnind", "synset"])
    df_tiny = pd.read_csv(os.path.join(datapath, "wnids.txt"), names=["wnind"])
    pprint(df_tiny)
    df_tiny["synset"] = df[df["wnind"].isin(df_tiny["wnind"])]
    pprint(df_tiny.head())



if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, default="../../data/tiny-imagenet-200")
    args = parser.parse_args()
    
    main(args.datapath)
