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
    df_merged_label = pd.merge(df,df_tiny,on='wnind')
    df_merged_label.insert(0, "id", df_merged_label.index)

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, default="/media/julia/Seagate/Data/tiny-imagenet-200")
    args = parser.parse_args()

    main(args.datapath)
