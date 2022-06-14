import argparse
import os
import csv

from process_pretrain_data import get_kmer_sentence, get_kmer_sequence

def Process(args):
    path = args.file_path

    output_f = open(args.output_path, "w+")
    output_w = csv.writer(output_f, delimiter='\t')
    output_w.writerow(['sequence', 'label'])
    with open(path, 'r+') as input_f:
        input_f.readline()
        line = input_f.readline()
        # print(line)
        while input_f:
            try:
                seq, label = line.split(',')
            except ValueError:
                print(line)
                break
            kmers = get_kmer_sentence(seq, args.kmer)
            output_w.writerow([kmers, int(label)])
            line = input_f.readline()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--kmer",
        default=1,
        type=int,
        help="K-mer",
    )
    parser.add_argument(
        "--file_path",
        default=None,
        type=str,
        help="The path of the file to be processed",
    )
    parser.add_argument(
        "--output_path",
        default=None,
        type=str,
        help="The path of the processed data",
    )
    # args = parser.parse_args()
    args = parser.parse_args(['--kmer', '6', '--file_path', '../data/seq/201/seq.csv', '--output_path', '../data/seq/201/kmers6.csv'])

    Process(args)
    

    


if __name__ == "__main__":
    main()