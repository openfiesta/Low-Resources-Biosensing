### Mutation Analysis pipeline

Before starting: All the scripts have being wrote in Python for Jupyter lab (https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).

We are working with the GISAID nCov database (https://www.gisaid.org/) taking into account the high coverage sequences. At the date of the first trials this comprises 8124 sequences worldwide.

You could send all your questions to franxi2953@gmail.com



#### Sequences joiner

1) Create a folder named "seq" in the same directory of the script "SeqJoiner.ipynb"

2) Paste the sequences there.

3) Run the script with jupyter lab.

4) You will find the output file in the "seq" directory. This file is a multi-FASTA file, comprised by all the sequences named by the EPI_ISL_ reference. You could check all the metadata of the sequences, with this references here -> https://github.com/nextstrain/ncov/blob/master/data/metadata.tsv.



#### Multiple Sequence Alignment

For the MSA we used MAFFT alignment as it's the most optimized tool we found for huge amounts of data. It could be run both locally or in the on line server, thanks to its memory saving mode.

Running the MSA locally (16GB of RAM and a Intel(R) Core(TM) i7-4790K CPU) last around 48 hours to complete the analysis. The on line server will perform the same task in 10 minutes. 

For the on line server we followed this protocol: https://mafft.cbrc.jp/alignment/software/closelyrelatedviralgenomes.html

The output will be a huge alignment (.aln) file. You could visualize this data with AliView (https://ormbunkar.se/aliview/). It's the free software we found to manage in a more efficient way files as big as the onbe produced with 8k sequences.



#### Mutation Analysis

##### Parsing the .aln file

1) Name the alignment file as "align.aln" and put it in the same folder as the script "AlignmentParser.ipynb".

2) Run the script with jupyter lab.

3) The output file ("nc_count.txt") will have a structure comprised by 6 columns, with the numbers of nucleotide position and the number of sequences with Adenine, Thymine, Guanine, Cytosine or a gap at this position.

##### Calculating variance per nucleotide

1) Put the nc_count.txt file from the previous script in the same folder of the "DeviationCalc.ipynb" script.

2) Run the script with jupyter lab.

3) You will see 2 output files:

- A "Variation.eps" with the graph representing each variation per nucleotide in the entire sequence in vectorial format.
- A "Variation.txt" with a two columns file, one with the nucleotide position and the other with a number that represents how many sequences vary from the consensus.



### Next steps (Help welcomed!)

- Checking the scripts and improve their performance.
- Creating an script which could give an score of different genome regions (like the ones targeted by primers) based in the variation saved in the "Variation.txt" file.
- Perform this same analysis at different levels (regional, continental, global...) and compare the results.
- Perform the clustering of different nCov strains based in the total genome variation between themselves.