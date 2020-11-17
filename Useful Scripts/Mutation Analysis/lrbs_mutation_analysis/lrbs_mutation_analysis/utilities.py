import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output

from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import SeqIO
from Bio.Seq import Seq

import numpy as np
import matplotlib.pyplot as plt
import os
import time


aCounter = 0
tCounter = 0
gCounter = 0
cCounter = 0
pCounter = 0

def countNucleotide(c,degeneratedNucleotides=False):

    global aCounter
    global tCounter
    global gCounter
    global cCounter
    global pCounter


    if c == "a":
        aCounter = aCounter + 1
    elif c == "t":
        tCounter = tCounter + 1
    elif c == "g":
        gCounter = gCounter + 1
    elif c == "c":
        cCounter = cCounter + 1
    elif c == "-":
        pCounter = pCounter + 1
    elif degeneratedNucleotides:
        if c == "r":
            aCounter = aCounter + 0.5
            gCounter = gCounter + 0.5
        elif c == "y":
            cCounter = cCounter + 0.5
            tCounter = tCounter + 0.5
        elif c == "s":
            cCounter = cCounter + 0.5
            gCounter = gCounter + 0.5
        elif c == "w":
            aCounter = aCounter + 0.5
            tCounter = tCounter + 0.5
        elif c == "k":
            tCounter = tCounter + 0.5
            gCounter = gCounter + 0.5
        elif c == "m":
            cCounter = cCounter + 0.5
            aCounter = aCounter + 0.5
        elif c == "b":
            cCounter = cCounter + 0.33
            gCounter = gCounter + 0.33
            tCounter = tCounter + 0.33
        elif c == "d":
            aCounter = aCounter + 0.33
            gCounter = gCounter + 0.33
            tCounter = tCounter + 0.33
        elif c == "h":
            cCounter = cCounter + 0.33
            aCounter = aCounter + 0.33
            tCounter = tCounter + 0.33
        elif c == "v":
            cCounter = cCounter + 0.33
            gCounter = gCounter + 0.33
            aCounter = aCounter + 0.33
        else:
            aCounter = aCounter + 0.25
            tCounter = tCounter + 0.25
            cCounter = cCounter + 0.25
            gCounter = gCounter + 0.25



def resetCounters():
    
    global aCounter
    global tCounter
    global gCounter
    global cCounter
    global pCounter
    
    aCounter = 0
    tCounter = 0
    gCounter = 0
    cCounter = 0
    pCounter = 0





def AlignmentParser (degeneratedNucleotides = False, f_align = "align.aln", f_out="nc_count.txt"):
    
    global aCounter
    global tCounter
    global gCounter
    global cCounter
    global pCounter
    
    aCounter = 0
    tCounter = 0
    gCounter = 0
    cCounter = 0
    pCounter = 0
    counter = 0
    seq = 0
    nset = 0
    
    with open(f_align, 'r') as infile:
        for i in range(0,3):
            s = infile.readline()

        buff = infile.readline()
    #     fseq = buff.split(" ")[0] #first sequence

        with open(f_out, 'w') as outfile:
            outfile.write("Nt\tA\tT\tG\tC\t-\n")


            while buff:

                clear_output(wait=True)
                data = []

                while buff and buff != '\n': #reading the complete 60 nucleotides set alingment 
                    #parsing just the sequence
                    if len(buff.split(" ")) > 1 and len(buff.split(" ")) < 50 and len(buff.split("*")) < 2:
                        buff = buff.split(" ")
                        buff = buff[len(buff)-1] 
                        data.append(buff)

                    buff = infile.readline()

                buff = " "
                i = 0
                if data:
                    #Iterating throw columns
                    while buff != '\n': 
                        #Iterating throw rows
                        for j in data:
                            buff = j[i].lower()

                            if buff != '\n':
                                countNucleotide(buff,degeneratedNucleotides)
                        if buff != '\n':
                            outfile.write(str(1+i+(nset*60)) + "\t" + str(aCounter) + "\t" + str(tCounter) + "\t" + str(gCounter) + "\t" + str(cCounter) + "\t" + str(pCounter) + "\n")
                        resetCounters()
                        i = i + 1


                    if nset == 390:
                        hola2 = data

                    if nset == 391:
                        hola = data
                    nset = nset + 1
                    print ("base pair:" + str(nset*60))


                while buff == '\n':
                    buff = infile.readline()


    #     print("A:" + str(aCounter) + " T:" + str(tCounter) + " G:" + str(gCounter) + " C:" + str(cCounter) + " -:" + str(pCounter))
    #     print("\n "+ str(aCounter+tCounter+gCounter+cCounter+pCounter))

    

def DeviationCalc (countGaps = True, f_count="nc_count.txt", f_out="Variation.txt"):
    sumDiff = 0
    b=0
    variation = []
    counter = 0

    if countGaps:
        g = 5
    else:
        g = 4



    with open(f_count, 'r') as infile:
        line = infile.readline()
        line = infile.readline().split('\n')[0]
        while line:

            line = line.split('\t')
            line = line[1:6]

            for i in range(0,g):

                if float(line[i]) > b:
                    sumDiff = sumDiff + b 
                    b = float(line[i])

                else:
                    sumDiff = sumDiff + float(line[i])

            b = 0
            variation.append(sumDiff)
            sumDiff = 0
            line = infile.readline().split('\n')[0]
            counter = counter + 1


    counter = 0
    plt.plot(variation,'.')
    #plt.savefig('Variation.eps',format='eps')

    with open(f_out, 'w') as outfile:
        for i in variation:
            outfile.write(str(counter+1)+"\t"+str(i)+"\n")
            counter = counter + 1
            
def ConsensusSeq (INCLUDE_GAPS = True, f_count="nc_count.txt", f_out="consensusSeq.txt"):
    
    seq = []
    output = ""
    nc = 0
    b = 0

    if INCLUDE_GAPS:
        g = 5
    else:
        g = 4

    with open(f_count, 'r') as infile:
        line = infile.readline()
        line = infile.readline().split('\n')[0]
        while line:

            line = line.split('\t')
            line = line[1:6]


            for i in range(0,g):
    #                 The NC is the most represented and is represented in more than 10 seqs (So it's not an outlier)
                if (float(line[i]) > b) and (float(line[i]) > 10.0): 
                    b = float(line[i])
                    nc = i


            if nc == 0:
                seq.append("a")
            elif nc == 1:
                seq.append("t")
            elif nc == 2:
                seq.append("g")
            elif nc == 3:
                seq.append("c")
            elif INCLUDE_GAPS and nc == 4:
                seq.append("-")


            b = 0
            nc = 5
            line = infile.readline().split('\n')[0]
    #         counter = counter + 1

    with open(f_out, 'w') as outfile:
        outfile.write(">Consensus\n")
        outfile.write(output.join(seq))
        
def ComputeMutation (p, nc_i ,i,n,m_t,mutated_nt,output_s,nucleotide_count):
    
    if n > m_t:
        mutated_nt.seq[p] += " " + str(nc_i-1) + " "
        output_s.seq[p] = output_s.seq[p] + "\n" + str(nc_i) + "\t" + str(n) + "\t" + "\t".join(nucleotide_count[i].split('\t')[1:6])



class sequences:
    def __init__(self,p):
        self.seq = {
            "F3":p,
            "B3":p,
            "LF":p,
            "LB":p,
            "FIP":p,
            "rFIP":p,
            "BIP":p,
            "rBIP":p
        }

        
def PrimerTest (f_consensus="consensusSeq.txt",f_primers="primers.txt",f_variation="Variation.txt",f_count="nc_count.txt", f_name = int(round(time.time() * 1000)), ranges=[50,500,2500], mutation_threshold=50):
    
    consensus = []
    range_variation = []
    nucleotide_count =[]
    plocation = []
    i_plocation = []
    l_plocation = []

    # Range for creating plotting colors
    range1 = ranges[0]
    range2 = ranges[1]
    range3 = ranges[2]

    # Mutation threshold
    m_t = mutation_threshold

    sizeb = 0

    fip = 0
    rfip = 0
    a_end = 0

    p_start = sequences(0)
    primers = sequences("")
    primers_fragments = sequences("")
    output_s = sequences("")
    mutated_nt = sequences("")


    print("________________ALIGNING PRIMERS_________________")
    with open(f_consensus, 'r') as cons:
        for record in SeqIO.parse(cons, "fasta"):
            consensus = str(record.seq).upper()
        with open(f_primers, 'r') as primersIO:
                for primersIO in SeqIO.parse(primersIO, "fasta"):
                    if "F3" in primersIO.id:

                        primers.seq["F3"] = primersIO.seq

                        alignments = pairwise2.align.localms(consensus, primersIO.seq,2,-4, -10,-1)
                        print("----------" + primersIO.id + "----------")
                        print(format_alignment(*alignments[0]))
                        p_start.seq["F3"] = alignments[0][3]
                        primers_fragments.seq["F3"] = format_alignment(*alignments[0]).split(" ")[1].split("\n")[0]

                    elif "B3" in primersIO.id:

                        primers.seq["B3"] = primersIO.seq

                        alignments = pairwise2.align.localms(consensus, primersIO.seq.reverse_complement(),2,-4, -10,-1)
                        print("----------" + primersIO.id + "----------")
                        print(format_alignment(*alignments[0]))
                        p_start.seq["B3"] = alignments[0][3]
                        primers_fragments.seq["B3"] = format_alignment(*alignments[0]).split(" ")[1].split("\n")[0]

                        a_end = alignments[0][4]

                    if "LF" in primersIO.id:

                        primers.seq["LF"] = primersIO.seq

                        alignments = pairwise2.align.localms(consensus, primersIO.seq.reverse_complement(),2,-4, -10,-1)
                        print("----------" + primersIO.id + "----------")
                        print(format_alignment(*alignments[0]))
                        p_start.seq["LF"] = alignments[0][3]
                        primers_fragments.seq["LF"] = format_alignment(*alignments[0]).split(" ")[1].split("\n")[0]

                    elif "LB" in primersIO.id:

                        primers.seq["LB"] = primersIO.seq

                        alignments = pairwise2.align.localms(consensus, primersIO.seq,2,-4, -10,-1)
                        print("----------" + primersIO.id + "----------")
                        print(format_alignment(*alignments[0]))
                        p_start.seq["LB"] = alignments[0][3]
                        primers_fragments.seq["LB"] = format_alignment(*alignments[0]).split(" ")[1].split("\n")[0]

                    elif "FIP" in primersIO.id:

                        primers.seq["FIP"] = primersIO.seq

                        alignments = pairwise2.align.localms(consensus, primersIO.seq,2,-4, -10,-1)
                        print("----------" + primersIO.id + "----------")
                        print(format_alignment(*alignments[0]))
                        p_start.seq["FIP"] = alignments[0][3]
                        buff = format_alignment(*alignments[0]).split(" ")
                        primers_fragments.seq["FIP"] = buff[1].split("\n")[0]

                        alignments = pairwise2.align.localms(consensus, primersIO.seq.reverse_complement(),2,-4, -10,-1)
                        print("----------REVERSE COMPLEMENT OF " + primersIO.id + "----------")
                        print(format_alignment(*alignments[0]))
                        buff = format_alignment(*alignments[0]).split(" ")
                        p_start.seq["rFIP"] = alignments[0][3]
                        primers_fragments.seq["rFIP"] = buff[1].split("\n")[0]


                    elif "BIP" in primersIO.id:

                        primers.seq["BIP"] = primersIO.seq

                        alignments = pairwise2.align.localms(consensus, primersIO.seq,2,-4, -10,-1)
                        print("----------REVERSE COMPLEMENT OF " + primersIO.id + "----------")
                        print(format_alignment(*alignments[0]))
                        p_start.seq["rBIP"] = alignments[0][3]
                        primers_fragments.seq["rBIP"] = format_alignment(*alignments[0]).split(" ")[1].split("\n")[0]
                        sizeb=len(primersIO.seq)

                        alignments = pairwise2.align.localms(consensus, primersIO.seq.reverse_complement(),2,-4, -10,-1)
                        print("----------" + primersIO.id + "----------")
                        print(format_alignment(*alignments[0]))
                        p_start.seq["BIP"] = alignments[0][3]
                        primers_fragments.seq["BIP"] = format_alignment(*alignments[0]).split(" ")[1].split("\n")[0]

    print("PRIMERS RANGE:" + str(p_start.seq["F3"]) + " - " + str(a_end))

    print("________________COMPUTING VARIATION MATRIX_________________")

    if not os.path.isdir(f_name):
        os.mkdir(f_name)

    with open(str(f_name) + "/output.txt", 'w') as output:
        with open(f_variation, 'r') as variation:
            with open(f_count, 'r') as ncount:

                nc_variation = variation.readline()
                ncount.readline()
    #             The +1 in the following line is because pairwise2 alignment bases number start at 0 and the nc_count & variation.txt starts at 1
                while not str(p_start.seq["F3"]+1) in nc_variation:
                    nc_variation = variation.readline()
                    ncount.readline()
                
                range_variation.append(float(nc_variation.split("\t")[1].split("\n")[0]))
                nucleotide_count.append(ncount.readline())
                
                while not str(a_end) in nc_variation:
                    
                    nc_variation = variation.readline()
                    range_variation.append(float(nc_variation.split("\t")[1].split("\n")[0]))

                    nucleotide_count.append(ncount.readline())

    #                 print(nucleotide_count[len(nucleotide_count)-1])
    #                 print(range_variation[len(nucleotide_count)-1])

                buff = []
                i = 0
            
            
                for n,i in zip(range_variation, range(0,len(range_variation))):
                    #calculate variation
                    if n < range1:
                        buff.append(0)
                    elif n < range2:
                        buff.append(0.33)
                    elif n < range3:
                        buff.append(0.66)
                    else:
                        buff.append(1)

                    #Do this region have primers?
                #             F3 & B3
                    if i < len(str(primers_fragments.seq["F3"])): #F3
                        plocation.append(0.1)
                        nucleotide_index = i+1
                        ComputeMutation("F3", nucleotide_index, i,n, m_t,mutated_nt,output_s,nucleotide_count)


                    elif i > (p_start.seq["B3"]-p_start.seq["F3"]) and i < ((p_start.seq["B3"]-p_start.seq["F3"]) + len(str(primers_fragments.seq["B3"]))):
                        plocation.append(0.9)
                        nucleotide_index = len(primers_fragments.seq["B3"])-(i-(p_start.seq["B3"]-p_start.seq["F3"]))
                        ComputeMutation("B3", nucleotide_index, i,n,m_t,mutated_nt,output_s,nucleotide_count)

                    else:
                        plocation.append(0)


                #                 FIP AND BIP
                    if i > (p_start.seq["FIP"]-p_start.seq["F3"]) and i < ((p_start.seq["FIP"]-p_start.seq["F3"]) + len(str(primers_fragments.seq["FIP"]))): 
                        i_plocation.append(0.3)
                        nucleotide_index = len(primers.seq["FIP"]) - (len(primers_fragments.seq["FIP"])- ((i+1) - (p_start.seq["FIP"] - p_start.seq["F3"])))
                        ComputeMutation("FIP", nucleotide_index, i,n,m_t,mutated_nt,output_s,nucleotide_count)

                    elif i > (p_start.seq["rFIP"]-p_start.seq["F3"]) and i < ((p_start.seq["rFIP"]-p_start.seq["F3"]) + len(str(primers_fragments.seq["rFIP"]))): 
                        i_plocation.append(0.3)
                        nucleotide_index = (p_start.seq["rFIP"]-p_start.seq["F3"]) + len(primers_fragments.seq["rFIP"]) - i
                        if nucleotide_index > len(primers_fragments.seq["rBIP"]):
                            ComputeMutation("rFIP", nucleotide_index, i,n,m_t,mutated_nt,output_s,nucleotide_count)

                    elif i > (p_start.seq["rBIP"]-p_start.seq["F3"]) and i < ((p_start.seq["rBIP"]-p_start.seq["F3"]) + len(str(primers_fragments.seq["rBIP"]))): 
                        i_plocation.append(0.6)
                        nucleotide_index = (i+1)-(p_start.seq["rBIP"]-p_start.seq["F3"])
                        ComputeMutation("rBIP", nucleotide_index, i,n,m_t,mutated_nt,output_s,nucleotide_count)

                    elif i > (p_start.seq["BIP"]-p_start.seq["F3"]) and i < ((p_start.seq["BIP"]-p_start.seq["F3"]) + len(str(primers_fragments.seq["BIP"]))): 
                        i_plocation.append(0.6)
                        nucleotide_index = len(primers.seq["BIP"]) - (i - (p_start.seq["BIP"]-p_start.seq["F3"]))
                        if nucleotide_index > len(primers_fragments.seq["rBIP"]):
                            ComputeMutation("BIP", nucleotide_index, i,n,m_t,mutated_nt,output_s,nucleotide_count)

                    else:
                        i_plocation.append(0)



                #                 LOOP PRIMERS   
                    if i > (p_start.seq["LF"]-p_start.seq["F3"]) and i < ((p_start.seq["LF"]-p_start.seq["F3"]) + len(str(primers_fragments.seq["LF"]))):
                        l_plocation.append(0.5)
                        nucleotide_index = len(primers_fragments.seq["LF"])-(i-(p_start.seq["LF"]-p_start.seq["F3"]))
                        ComputeMutation("LF", nucleotide_index, i,n,m_t,mutated_nt,output_s,nucleotide_count)

                    elif i > (p_start.seq["LB"]-p_start.seq["F3"]) and i < ((p_start.seq["LB"]-p_start.seq["F3"]) + len(str(primers_fragments.seq["LB"]))):
                        l_plocation.append(0.5)
                        nucleotide_index = 1+i-(p_start.seq["LB"]-p_start.seq["F3"])
                        ComputeMutation("LB", nucleotide_index, i,n,m_t,mutated_nt,output_s,nucleotide_count)
                    else:
                        l_plocation.append(0)


                range_variation = buff

                rv = np.array([range_variation])
                rv = np.vstack((rv, np.array([plocation])))
                rv = np.vstack((rv, np.array([i_plocation])))
                rv = np.vstack((rv, np.array([l_plocation])))

                fig, ax = plt.subplots(figsize=( (a_end - p_start.seq["F3"])/10, 1))
                im = ax.imshow(rv,aspect='auto')


                plt.show()
                fig.savefig(str(f_name) + "/heatmap.png")

                for n in primers.seq:
                    if primers.seq[n] != "":
                        output.write(">" + n +"\n")
                        output.write(str(primers.seq[n]) + "\n")

                output.write("\n------------------------------------------------")
                output.write("\n|            MUTATION ANALYSIS                 |")
                output.write("\n------------------------------------------------\n")

    #             Calculate FIP and BIP complete sequences

                output_s.seq["FIP"] = output_s.seq["rFIP"] + output_s.seq["FIP"]
                output_s.seq["BIP"] = output_s.seq["BIP"] + output_s.seq["rBIP"]

                mutated_nt.seq["FIP"] = mutated_nt.seq["rFIP"] + mutated_nt.seq["FIP"]
                mutated_nt.seq["BIP"] = mutated_nt.seq["BIP"] + mutated_nt.seq["rBIP"]

                for n in output_s.seq:

                    if output_s.seq[n] != "" and not "r" in n:

                        output.write("\n" + str(n) + "\n")
                        output.write("------------------------------------------\n")
                        for nc,ni in zip(primers.seq[n],range(0,len(primers.seq[n]))):
                            if " " + str(ni) + " " in mutated_nt.seq[n]:
                                output.write(" *" + nc + "* ")
                            else:
                                output.write(nc)
                        output.write("\nMutated nucleotides count in the TARGET STRAND:")
                        output.write("\nnc\tvar.\tA\tT\tG\tC\t-\n")
                        output.write(output_s.seq[n])

                output.close()
                print("Row legend:\n\t- 1st: Mutation rate.\n\t- 2nd: B3 and F3 primers alignment.\n\t- 3rd: FIP and BIP primers alignment.\n\t- 4th: Loop primers alignment.")