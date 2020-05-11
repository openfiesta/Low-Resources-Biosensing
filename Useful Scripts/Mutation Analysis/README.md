### 

<img src="https://jogl.io/assets/imgs/logo.png" width="180px" height="250px" align="right">



### Table of Contents

[TOC]



### Introduction

We have started this project aiming to develop a series of tools for analyzing the existing primers for doing the nCov diagnosis based in the presence of its RNA. 

Specifically, the goal of following tools is to provide a simple way for analyzing the mutation rate in huge amounts of sequences data (>8k sequences). 

The goal is to use this information to compare different primer sets (RT-PCR, RT-LAMP...) and predict which of them would work better, due to the more conserved nature of the regions their target along all the nCov strains worldwide.

You could send all your questions to franxi2953@gmail.com



### Next steps (Help welcomed!)

- Checking the scripts and improve their performance.

- Creating an script which could give an score of different genome regions (like the ones targeted by primers) based in the variation saved in the "Variation.txt" file.

- Perform this same analysis at different levels (regional, continental, global...) and compare the results.

- Perform the clustering of different nCov strains based in the total genome variation between themselves.

  

### Mutation Analysis pipeline

Before starting: All the scripts have being wrote in Python for Jupyter lab (https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).

We are working with the GISAID nCov database (https://www.gisaid.org/) taking into account only the high coverage sequences. At the date of the first trials this comprises 8124 sequences worldwide.

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



1. #### Mutation Analysis


##### Parsing the .aln file

1. Name the alignment file as "align.aln" and put it in the same folder as the script "AlignmentParser.ipynb".

2. Run the script with jupyter lab.

3. The output file ("nc_count.txt") will have a structure comprised by 6 columns, with the numbers of nucleotide position and the number of sequences with Adenine, Thymine, Guanine, Cytosine or a gap at this position.


##### Computing variance per nucleotide

1. Put the nc_count.txt file from the previous script in the same folder of the "DeviationCalc.ipynb" script.

2. Run the script with jupyter lab.

3. You will see 2 output files:
   -  "Variation.eps" with the graph representing each variation per nucleotide in the entire sequence in vectorial format.
   - A "Variation.txt" with a two columns file, one with the nucleotide position and the other with a number that represents how many sequences vary from the consensus.

##### Computing the consensus sequence

1. Put the nc_count.txt file from the previous script in the same folder of the "SeqMaker.ipynb" script.

2. Adjust the flag "INCLUDE_GAPS" on the top of the script in case you want your consensus sequence with gaps. A consensus gap mean that this particular region was not described in the majority of the sequences.
3. Run the script with jupyter lab.

4. The output file "consensusSeq.txt" have the FASTA of the consensus sequence.


### Primer analysis

#### LAMP visual primer analysis

##### Performing the analysis

1. Create a file named "primers.txt" in the same folder than the "LampPrimerTester.ipynb" script. This file should contain the FASTA sequence of the primers, with the names "F3", "B3", "FIP" and "BIP". And example of the "primers.txt" file structure could be found in the examples folder.

   **[NOTE]** At the moment, this script do not support Loop primers.

2. Put the "consensusSeq.txt" and the "Variation.txt" files (see previous chapter for the scripts that generate this files) in the same folder than the "LampPrimerTester.ipynb" script.

3. Run the script.

##### Analysis of the results

The output of the script is the following screen:

![lampoutput](images/lampoutput.jpg)

**Legend**:

a) Primers alignment with consensus sequence (Using biopython pairwise2 package)

**[Note]**: Here (marked with a small red rectangle) you could see how the BIP primer target a region which, in the computed consensus sequence, have a different nucleotide that the one included in the primer.

b) Amplicon visualization; a 2 lines heat-map:

- The first line include a heat-map of the variation of each nucleotide. By default the color is normalized with the 8k sequence nCov analysis and comprises 3 ranges:
  - Dark Blue: less than 10 sequences vary from the consensus.
  - Light blue: between 10 and 80 sequences vary from the consensus.
  - Turquoise: between 80 and 800 sequences vary from the consensus.
  - Yellow: more than 800 sequences vary from the consensus. 
- The second line include the regions targeted by the different primers:
  1. F3 (5' - 3')
  2. FIP, before the loop (5' - 3')
  3. FIP, after the loop (3' - 5')
  4. BIP, after the loop (5' - 3')
  5. BIP, before the loop (3' - 5')
  6. B3, (3' - 5')





