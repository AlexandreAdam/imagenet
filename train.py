#!/usr/bin/python3
"""
=============================================
Title: train

Author(s): Alexandre Adam, Julia Potokina

Last modified: January 17, 2021

Description: Training of a model on imagenet
=============================================
"""
import tensorflow as tf
import datetime
import os

IM_HEIGHT = 64
IM_WIDTH = 64

def main():
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            os.path.join(datapath, "train"),
            image_size=(IM_HEIGHT, IM_HEIGHT)
            )


    pass

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-d", "--datapath", type=str, default="../../data/tiny-imagenet-200")
    args = parser.parse_args()

    main(args.datapath)
