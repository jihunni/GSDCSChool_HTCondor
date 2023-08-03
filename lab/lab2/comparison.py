#!/usr/bin/env python3
"""
This program calculates the number of equal base pairs from two fasta files.
INPUT : input1.fasta, input2.fasta
command example  : python3 comparison.py bonobo.fasta chimpanzee.fasta
"""
import argparse
import os

from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

parser = argparse.ArgumentParser(description='Alignment score')
parser.add_argument('seq1', type=str, help='input_fasta_file_1')
parser.add_argument('seq2', type=str, help='input_fasta_file_2')
args = parser.parse_args()

seq1_file_name = parser.parse_args().seq1
seq2_file_name = parser.parse_args().seq2

seq1_biopy = SeqIO.read(seq1_file_name,"fasta").seq
seq2_biopy = SeqIO.read(seq2_file_name,"fasta").seq

alignments = pairwise2.align.globalxx(seq1_biopy, seq2_biopy)

#seq1
#print(format_alignment(*alignments[0]))
#print(alignments)
print("Input \t length \t matched \t unmatched")
print(seq1_file_name, "\t", alignments[0].end, "\t", alignments[0].score, "\t", alignments[0].end - alignments[0].score)
print(seq2_file_name, "\t", alignments[1].end, "\t", alignments[1].score, "\t", alignments[1].end - alignments[1].score)
#print("seq1 total length: ", alignments[0].end )
#print("seq2 total length: ", alignments[1].end )
#print("overlapped : ", alignments[0].score)
#print("Unoverlapped for seq1: ", alignments[0].end - alignments[0].score)
#print("Unoverlapped for seq2: ", alignments[1].end - alignments[0].score)
