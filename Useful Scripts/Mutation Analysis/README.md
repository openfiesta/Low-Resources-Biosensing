### 

<img src="https://jogl.io/assets/imgs/logo.png" width="180px" height="250px" align="right">



### Table of Contents

- Introduction
- Next steps (Help welcomed!)
- Installing the library
- Library functions





### Introduction

We have started this project aiming to develop a series of tools for analyzing the existing primers for nCov diagnosis. 

Specifically, the goal of the following library is to provide a simple framework for analyzing the mutation rate in huge amounts of its sequences data (>8k sequences). 

The objective is to use this information to compare different primer sets (RT-PCR, RT-LAMP...) and predict which of them would work better, regarding the conservation of the targeted regions.

In the "OLD" folder you could find the beta version of the library functions, when they were just Jupyter Lab scripts.

You could send all your questions to franxi2953@gmail.com



### Next steps (Help welcomed!)

- Try the library and fix errors.

  

### Installing the library

1.  Git pull the "lrbs_mutation_analysis" folder.

2.  Run  `pip install -e 'folder_location\lrbs_mutation_analysis'`

3. Expected output `Successfully installed lrbs-mutation-analysis`

   

### Library functions



#### AlignmentParser (degeneratedNucleotides = False, f_align = "align.aln", f_out="nc_count.txt")



- <b>degeneratedNucleotides</b> Counting other nucleotides other tha A/T/G/C/- ?

- <b>f_align</b> Location of the .aln file **in Clustal format**. For example, output of MAFFT online tool (https://mafft.cbrc.jp/alignment/software/closelyrelatedviralgenomes.html). 

- <b>f_out</b> Output file location. The output file will have a structure comprised by 6 columns, with the numbers of nucleotide position and the number of sequences with Adenine, Thymine, Guanine, Cytosine or a gap at this position.





#### DeviationCalc (countGaps = True, f_count="nc_count.txt", f_out="Variation.txt")



- <b>countGaps</b> Counting "-" for computing deviation?
- <b>f_count</b> Location of the AlignmentParser fuction output.

- <b>f_out</b> Output location. The output will be a two columns file, one with the nucleotide position and the other with number of sequences that vary from the consensus.






#### **ConsensusSeq (INCLUDE_GAPS = True, f_count="nc_count.txt", f_out="consensusSeq.txt")**



- **INCLUDE_GAPS** Making the consensus sequence with gaps included? 

- **f_count** Location of the AlignmentParser fuction output.

- **f_out**  Output location. The output file "consensusSeq.txt" have the FASTA of the consensus sequence.

  




#### **PrimerTest (f_consensus="consensusSeq.txt", f_primers="primers.txt", f_variation="Variation.txt", f_count="nc_count.txt", f_name = int(round(time.time() * 1000)), ranges=[50,500,2500], mutation_threshold=50)**



- **f_consensus** Location of the consensus sequence file (Output of the ConsensusSeq function). **This sequence must include gaps**.

- **f_primers** Primers file. This file should contain the FASTA sequence of the primers, with the names "F3", "B3", "LB", "LF", FIP" and "BIP". And example of the "primers.txt" file structure could be found in the examples folder.

- **f_variation** Location of the DeviationCalc function output.

- **f_count** Location of the AlignmentParser function output.
- **f_name** Location of the output folder. If the folder doesn't exist it will be created.

- **ranges** A vector comprising three numbers that indicates the three ranges of number of mutated sequences for computing color intensities in the resulting heatmap.

- **mutation_threshold** The limit that indicates how many sequences need to vary from the consensus to start the mutation analysis.



The graphical script output includes a primer alignment and a heatmap indicating the region's variation within the areas where the primers align.



There is also a second output that can be found in the folder indicated in the "f_name" parameter. This result includes:

- An "output.txt" file, with the sequence of all the primers with the position of the primers' nucleotides that are aligned with highly mutated nucleotides in the target strand (With the respective nucleotide count of the targeted nucleotides).
- A .png file storing the heatmap.



