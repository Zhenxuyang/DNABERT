import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import os
import argparse

"""
split train valid test dataset
"""

def process(args):
    data_file_path = args.input_file
    data_dir =args.output_dir

    print("processing {}".format(data_file_path))
    data = pd.read_csv(data_file_path, delimiter='\t')
    data = data.values
    seqs, label = data[:, 0], data[:, 1]

    train_data, val_test_data, train_label, val_test_label = train_test_split(seqs, label, train_size=0.7, random_state=0, stratify=label) 
    print(train_data.shape, val_test_data.shape, train_label.shape, val_test_label.shape)

    val_data, test_data, val_label, test_label = train_test_split(val_test_data, val_test_label, test_size=0.5, random_state=0, stratify=val_test_label)
    print(val_data.shape, val_label.shape, test_data.shape, test_label.shape)

    train_dataset = np.column_stack((train_data, train_label))
    val_dataset = np.column_stack((val_data, val_label))
    test_dataset = np.column_stack((test_data, test_label))

    train_dataset = np.insert(train_dataset, 0, ['sequence', 'label'], axis=0)
    val_dataset = np.insert(val_dataset, 0, ['sequence', 'label'], axis=0)
    test_dataset = np.insert(test_dataset, 0, ['sequence', 'label'], axis=0)


    train_dir = os.path.join(data_dir, 'train')
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)


    np.savetxt(os.path.join(train_dir, 'train.tsv'), train_dataset, delimiter='\t', fmt='%s')
    np.savetxt(os.path.join(train_dir, 'dev.tsv'), val_dataset, delimiter='\t', fmt='%s')

    test_dir = os.path.join(data_dir, 'test')
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    np.savetxt(os.path.join(test_dir, 'dev.tsv'), test_dataset, delimiter='\t', fmt='%s')

def main():

    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument(
        "--input_file",
        default=None,
        type=str,
        required=True,
        help="The input data dir which contains the kmers and labels of the sequences",
    )

    parser.add_argument(
       "--output_dir",
       default=None,
       type=str,
       required=True,
       help="The output dir where the train, valid and test dataset are stored" 
    )

    args = parser.parse_args()

    process(args)

if __name__ == "__main__":
    main()