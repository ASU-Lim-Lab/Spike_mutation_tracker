import pandas as pd
import os, sys, glob, shutil
from Bio import SeqIO
import math
import re
import time

input_file_name = input("Input file name:    ")
output_file_name = input("Output file name:    ")

start_time = time.time()

wuhan_spike = "ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAATTACCCCCTGCATACACTAATTCTTTCACACGTGGTGTTTATTACCCTGACAAAGTTTTCAGATCCTCAGTTTTACATTCAACTCAGGACTTGTTCTTACCTTTCTTTTCCAATGTTACTTGGTTCCATGCTATACATGTCTCTGGGACCAATGGTACTAAGAGGTTTGATAACCCTGTCCTACCATTTAATGATGGTGTTTATTTTGCTTCCACTGAGAAGTCTAACATAATAAGAGGCTGGATTTTTGGTACTACTTTAGATTCGAAGACCCAGTCCCTACTTATTGTTAATAACGCTACTAATGTTGTTATTAAAGTCTGTGAATTTCAATTTTGTAATGATCCATTTTTGGGTGTTTATTACCACAAAAACAACAAAAGTTGGATGGAAAGTGAGTTCAGAGTTTATTCTAGTGCGAATAATTGCACTTTTGAATATGTCTCTCAGCCTTTTCTTATGGACCTTGAAGGAAAACAGGGTAATTTCAAAAATCTTAGGGAATTTGTGTTTAAGAATATTGATGGTTATTTTAAAATATATTCTAAGCACACGCCTATTAATTTAGTGCGTGATCTCCCTCAGGGTTTTTCGGCTTTAGAACCATTGGTAGATTTGCCAATAGGTATTAACATCACTAGGTTTCAAACTTTACTTGCTTTACATAGAAGTTATTTGACTCCTGGTGATTCTTCTTCAGGTTGGACAGCTGGTGCTGCAGCTTATTATGTGGGTTATCTTCAACCTAGGACTTTTCTATTAAAATATAATGAAAATGGAACCATTACAGATGCTGTAGACTGTGCACTTGACCCTCTCTCAGAAACAAAGTGTACGTTGAAATCCTTCACTGTAGAAAAAGGAATCTATCAAACTTCTAACTTTAGAGTCCAACCAACAGAATCTATTGTTAGATTTCCTAATATTACAAACTTGTGCCCTTTTGGTGAAGTTTTTAACGCCACCAGATTTGCATCTGTTTATGCTTGGAACAGGAAGAGAATCAGCAACTGTGTTGCTGATTATTCTGTCCTATATAATTCCGCATCATTTTCCACTTTTAAGTGTTATGGAGTGTCTCCTACTAAATTAAATGATCTCTGCTTTACTAATGTCTATGCAGATTCATTTGTAATTAGAGGTGATGAAGTCAGACAAATCGCTCCAGGGCAAACTGGAAAGATTGCTGATTATAATTATAAATTACCAGATGATTTTACAGGCTGCGTTATAGCTTGGAATTCTAACAATCTTGATTCTAAGGTTGGTGGTAATTATAATTACCTGTATAGATTGTTTAGGAAGTCTAATCTCAAACCTTTTGAGAGAGATATTTCAACTGAAATCTATCAGGCCGGTAGCACACCTTGTAATGGTGTTGAAGGTTTTAATTGTTACTTTCCTTTACAATCATATGGTTTCCAACCCACTAATGGTGTTGGTTACCAACCATACAGAGTAGTAGTACTTTCTTTTGAACTTCTACATGCACCAGCAACTGTTTGTGGACCTAAAAAGTCTACTAATTTGGTTAAAAACAAATGTGTCAATTTCAACTTCAATGGTTTAACAGGCACAGGTGTTCTTACTGAGTCTAACAAAAAGTTTCTGCCTTTCCAACAATTTGGCAGAGACATTGCTGACACTACTGATGCTGTCCGTGATCCACAGACACTTGAGATTCTTGACATTACACCATGTTCTTTTGGTGGTGTCAGTGTTATAACACCAGGAACAAATACTTCTAACCAGGTTGCTGTTCTTTATCAGGATGTTAACTGCACAGAAGTCCCTGTTGCTATTCATGCAGATCAACTTACTCCTACTTGGCGTGTTTATTCTACAGGTTCTAATGTTTTTCAAACACGTGCAGGCTGTTTAATAGGGGCTGAACATGTCAACAACTCATATGAGTGTGACATACCCATTGGTGCAGGTATATGCGCTAGTTATCAGACTCAGACTAATTCTCCTCGGCGGGCACGTAGTGTAGCTAGTCAATCCATCATTGCCTACACTATGTCACTTGGTGCAGAAAATTCAGTTGCTTACTCTAATAACTCTATTGCCATACCCACAAATTTTACTATTAGTGTTACCACAGAAATTCTACCAGTGTCTATGACCAAGACATCAGTAGATTGTACAATGTACATTTGTGGTGATTCAACTGAATGCAGCAATCTTTTGTTGCAATATGGCAGTTTTTGTACACAATTAAACCGTGCTTTAACTGGAATAGCTGTTGAACAAGACAAAAACACCCAAGAAGTTTTTGCACAAGTCAAACAAATTTACAAAACACCACCAATTAAAGATTTTGGTGGTTTTAATTTTTCACAAATATTACCAGATCCATCAAAACCAAGCAAGAGGTCATTTATTGAAGATCTACTTTTCAACAAAGTGACACTTGCAGATGCTGGCTTCATCAAACAATATGGTGATTGCCTTGGTGATATTGCTGCTAGAGACCTCATTTGTGCACAAAAGTTTAACGGCCTTACTGTTTTGCCACCTTTGCTCACAGATGAAATGATTGCTCAATACACTTCTGCACTGTTAGCGGGTACAATCACTTCTGGTTGGACCTTTGGTGCAGGTGCTGCATTACAAATACCATTTGCTATGCAAATGGCTTATAGGTTTAATGGTATTGGAGTTACACAGAATGTTCTCTATGAGAACCAAAAATTGATTGCCAACCAATTTAATAGTGCTATTGGCAAAATTCAAGACTCACTTTCTTCCACAGCAAGTGCACTTGGAAAACTTCAAGATGTGGTCAACCAAAATGCACAAGCTTTAAACACGCTTGTTAAACAACTTAGCTCCAATTTTGGTGCAATTTCAAGTGTTTTAAATGATATCCTTTCACGTCTTGACAAAGTTGAGGCTGAAGTGCAAATTGATAGGTTGATCACAGGCAGACTTCAAAGTTTGCAGACATATGTGACTCAACAATTAATTAGAGCTGCAGAAATCAGAGCTTCTGCTAATCTTGCTGCTACTAAAATGTCAGAGTGTGTACTTGGACAATCAAAAAGAGTTGATTTTTGTGGAAAGGGCTATCATCTTATGTCCTTCCCTCAGTCAGCACCTCATGGTGTAGTCTTCTTGCATGTGACTTATGTCCCTGCACAAGAAAAGAACTTCACAACTGCTCCTGCCATTTGTCATGATGGAAAAGCACACTTTCCTCGTGAAGGTGTCTTTGTTTCAAATGGCACACACTGGTTTGTAACACAAAGGAATTTTTATGAACCACAAATCATTACTACAGACAACACATTTGTGTCTGGTAACTGTGATGTTGTAATAGGAATTGTCAACAACACAGTTTATGATCCTTTGCAACCTGAATTAGACTCATTCAAGGAGGAGTTAGATAAATATTTTAAGAATCATACATCACCAGATGTTGATTTAGGTGACATCTCTGGCATTAATGCTTCAGTTGTAAACATTCAAAAAGAAATTGACCGCCTCAATGAGGTTGCCAAGAATTTAAATGAATCTCTCATCGATCTCCAAGAACTTGGAAAGTATGAGCAGTATATAAAATGGCCATGGTACATTTGGCTAGGTTTTATAGCTGGCTTGATTGCCATAGTAATGGTGACAATTATGCTTTGCTGTATGACCAGTTGCTGTAGTTGTCTCAAGGGCTGTTGTTCTTGTGGATCCTGCTGCAAATTTGATGAAGACGACTCTGAGCCAGTGCTCAAAGGAGTCAAATTACATTACACATAA"
reference_fasta_id = ">wuhan_spike_gene"
with open('wuhan_reference.fa', 'w') as make_fasta:
    make_fasta.write(reference_fasta_id + "\n")
    make_fasta.write(wuhan_spike)
make_fasta.close()

os.system("mafft --6merpair --thread -1 --compactmapout --addfragments %s wuhan_reference.fa > mafft2vcf_input" % (input_file_name)) 

codon_table = {
    "TTT":"F",
    "TTC":"F",
    "TTA":"L",
    "TTG":"L",
    "CTT":"L",
    "CTC":"L",
    "CTA":"L",
    "CTG":"L",
    "ATT":"I",
    "ATC":"I",
    "ATA":"I",
    "ATG":"M",
    "GTT":"V",
    "GTC":"V",
    "GTA":"V",
    "GTG":"V",
    "TCT":"S",
    "TCC":"S",
    "TCA":"S",
    "TCG":"S",
    "CCT":"P",
    "CCC":"P",
    "CCA":"P",
    "CCG":"P",
    "ACT":"T",
    "ACC":"T",
    "ACA":"T",
    "ACG":"T",
    "GCT":"A",
    "GCC":"A",
    "GCA":"A",
    "GCG":"A",
    "TAT":"Y",
    "TAC":"Y",
    "TAA":"*",
    "TAG":"*",
    "CAT":"H",
    "CAC":"H",
    "CAA":"Q",
    "CAG":"Q",
    "AAT":"N",
    "AAC":"N",
    "AAA":"K",
    "AAG":"K",
    "GAT":"D",
    "GAC":"D",
    "GAA":"E",
    "GAG":"E",
    "TGT":"C",
    "TGC":"C",
    "TGA":"*",
    "TGG":"W",
    "CGT":"R",
    "CGC":"R",
    "CGA":"R",
    "CGG":"R",
    "AGT":"S",
    "AGC":"S",
    "AGA":"R",
    "AGG":"R",
    "GGT":"G",
    "GGC":"G",
    "GGA":"G",
    "GGG":"G"
}


keep_only_aa = True #Remove duplicate amino acid positions, keeping only the first mismatching nucleotide
remove_synonymous = True #Remove mutations that don't result in an amino acid substitution


vcf_frame = pd.DataFrame()

with open("mafft2vcf_input") as alignment_file: #compactmapout_mafft, run323_mafft, mafft2vcf_input
    
    sequence_count = 0

    for record in SeqIO.parse(alignment_file, "fasta"):
        #print(record.id)
        sequence_count += 1
        mismatch_count = 0 #Exactly matching nucleotides
        ambig_count = 0 #Count of ambiguities
        coordinate_list = [] #nt position in spike
        aa_pos_list = [] #AA position in spike
        reference_list = [] #Reference nucleotides
        alternate_list = [] #Alternate nucleotides
        ref_codon_list = [] #Reference codon list
        alt_codon_list = [] #Alternate codon list
        ref_aa_list = [] #Reference AA list
        alt_aa_list = [] #Alternate AA list
        deletion_start = 0
        deletion_ref_nt = ""
        deletion_alt_nt = ""
        sequence_frame = pd.DataFrame()
        
        ###########################
        #  
        # Main comparison loop
        # 
        # Check for ambiguity -> skip if so
        # 
        # Determine if deletion -> add to buffer if so
        # 
        # - If neither, empty deletion buffer and check for mismatch
        #
        ###########################
        
        for x in range(0, len(wuhan_spike)): #Compare reference to sequence
            if str.upper(record.seq[x]) in ["N","Y","R","W","S","K","M"]: #If sequence is an ambig, tally and skip other steps
                ambig_count += 1
                
                pass

            elif str.upper(record.seq[x]) == '-': #First check if a deletion is on the input sequence
                if deletion_start == 0: #Check if the buffer is empty. If so, start a new buffer, else add the nucleotide to the buffer
                    deletion_len = 1
                    deletion_start = x
                    deletion_ref_nt += str.upper(wuhan_spike[x])
                    deletion_alt_nt += "-N"
                    #print(deletion_ref_nt)
                else:
                    deletion_ref_nt += str.upper(wuhan_spike[x])
                    deletion_alt_nt += "N"
                    deletion_len += 1
                    #print(deletion_ref_nt)
                    #print(deletion_alt_nt)

            else: #If there is not a deletion on the input
                if deletion_start != 0: #Empty the deletion buffer to output and reset
                    
                    coordinate_list.append(deletion_start + 1) #string starts at 0, add 1 for true nt position
                    reference_list.append(str(deletion_ref_nt))
                    alternate_list.append(str(deletion_alt_nt))
                    deletion_codon = (deletion_start +1) % 3 #string starts at 0, add 1 for true nt position
                    ref_aa_pos = math.ceil((deletion_start +1)/ 3) #string starts at 0, add 1 for true nt position
                    aa_pos_list.append(ref_aa_pos)
                    codon_position = (deletion_start + 1) % 3 #string starts at 0, add 1 for true nt position
                    three_prime_rule = True
                    if deletion_len > 0 and deletion_len % 3 ==0: #Fill in amino acid information for the remaining deleted nucleotides
                        if codon_position == 1:
                            reference_codon = str.upper(wuhan_spike[deletion_start]) + str.upper(wuhan_spike[deletion_start+1]) + str.upper(wuhan_spike[deletion_start+2])
                            next_nucleotides = ""
                            for y in range(0, len(record.seq)):
                                if len(next_nucleotides) == 3:
                                    break
                                if str.upper(record.seq[deletion_start + deletion_len + y]) in ["A","G","T","C"]:
                                    next_nucleotides += str.upper(record.seq[deletion_start +  deletion_len + y])
                                else:
                                    pass
                            if len(next_nucleotides) < 3: #Deletion occurs at end of sequence
                                alt_codon = "EOF"
                            else:
                                alt_codon = next_nucleotides
                        elif codon_position == 2:
                            reference_codon = str.upper(wuhan_spike[deletion_start-1]) + str.upper(wuhan_spike[deletion_start]) + str.upper(wuhan_spike[deletion_start+1])
                            next_nucleotides = ""
                            for y in range(0, len(record.seq)):
                                if len(next_nucleotides) == 2:
                                    break
                                if str.upper(record.seq[deletion_start +  deletion_len + y]) in ["A","G","T","C"]:
                                    next_nucleotides += str.upper(record.seq[deletion_start +  deletion_len + y])
                                else:
                                    pass
                            if len(next_nucleotides) < 2:
                                alt_codon = "EOF"
                            else:
                                test_alt_codon = str.upper(record.seq[deletion_start-1]) + next_nucleotides
                                test_ref_aa = codon_table[reference_codon]
                                test_alt_aa = codon_table[test_alt_codon]
                                if test_ref_aa == test_alt_aa:
                                    alt_codon = test_alt_codon
                                    three_prime_rule = False
                                else:
                                    alt_codon = "del"
                        elif codon_position == 0:
                            reference_codon = str.upper(wuhan_spike[deletion_start-2]) + str.upper(wuhan_spike[deletion_start-1]) + str.upper(wuhan_spike[deletion_start])
                            next_nucleotides = ""
                            for y in range(0, len(record.seq)):
                                if len(next_nucleotides) == 1:
                                    break
                                if str.upper(record.seq[deletion_start +  deletion_len + y]) in ["A","G","T","C"]:
                                    next_nucleotides += str.upper(record.seq[deletion_start +  deletion_len + y])
                                else:
                                    pass
                            if len(next_nucleotides) < 1:
                                alt_codon = "EOF"
                            else:
                                test_alt_codon = str.upper(record.seq[deletion_start-2]) + str.upper(record.seq[deletion_start -1]) + next_nucleotides
                                test_ref_aa = codon_table[reference_codon]
                                test_alt_aa = codon_table[test_alt_codon]
                                if test_ref_aa == test_alt_aa:
                                    alt_codon = test_alt_codon
                                    three_prime_rule = False
                                else:
                                    alt_codon = "del"
                            
                        ref_codon_list.append(reference_codon)
                        alt_codon_list.append(alt_codon)
                        if deletion_len > 0 and deletion_len % 3 ==0: #Nt deletion in multiple of 3; fill in AA deletion information
                            
                            #if codon_position % 3 == 0: #Deletion in 3rd position
                            #    alt_codon = str.upper(record.seq[x-2]) + str.upper(record.seq[x-1]) + str.upper(record.seq[x + deletion_len])
                            aa_deletion = int((deletion_len) / 3)
                            
                            for each_aa in range(1,aa_deletion+1): #Append deleted AAs information to lists

                                coordinate_list.append(str(deletion_start +1) + "cont"+ str(each_aa))
                                reference_list.append("Deletion")
                                alternate_list.append("del")
                                    
                                if each_aa == (aa_deletion): #AAs at end of deletion
                                    if codon_position == 0:
                                        final_codon = deletion_ref_nt[-2:] + str.upper(wuhan_spike[x])
                                        alt_codon_list.append("del")
                                    elif codon_position == 2:
                                        final_codon = deletion_ref_nt[-1:] + str.upper(wuhan_spike[x]) + str.upper(wuhan_spike[x+1])
                                        if three_prime_rule == True:
                                            alt_codon_list.append(test_alt_codon)
                                        else:
                                            alt_codon_list.append("del")                                        
                                    elif codon_position == 1:
                                        final_codon = deletion_ref_nt[-3:]
                                        if three_prime_rule == True:
                                            alt_codon_list.append(test_alt_codon)
                                        else:
                                            alt_codon_list.append("del")
                                    ref_codon_list.append(final_codon)
                                    del_aa_pos = ref_aa_pos + each_aa
                                    aa_pos_list.append(del_aa_pos)
                                else: #AAs in middle of deltion
                                    if codon_position == 0:
                                        ref_codon_list.append(deletion_ref_nt[(1 + (3 * (each_aa-1))):(4 + (3* (each_aa-1)))])
                                    elif codon_position == 1:
                                        ref_codon_list.append(deletion_ref_nt[(3 + (3 * (each_aa-1))):(6 + (3* (each_aa-1)))])
                                    elif codon_position == 2:
                                        ref_codon_list.append(deletion_ref_nt[(2 + (3 * (each_aa-1))):(5 + (3* (each_aa-1)))])
                                    alt_codon_list.append("del")
                                    del_aa_pos = ref_aa_pos + each_aa
                                    aa_pos_list.append(del_aa_pos)
                            

                        

                    else: #Deletion causes frameshift; 
                        ref_codon_list.append("FSDel")
                        alt_codon_list.append("FSDel")
                    deletion_start = 0
                    deletion_ref_nt = ""
                    deletion_alt_nt = ""

                if wuhan_spike[x] != str.upper(record.seq[x]): #Check for a reference/input mismatch and append to lists if there is a mismatch
                    mismatch_count +=1
                    codon_position = (x + 1) % 3 #string starts at 0, add 1 for true nt position
                    
                    #reference_codon = ""
                    #alt_codon = ""
                    if codon_position == 1:
                        reference_codon = str.upper(wuhan_spike[x]) + str.upper(wuhan_spike[x+1]) + str.upper(wuhan_spike[x+2])
                        alt_codon = str.upper(record.seq[x]) + str.upper(record.seq[x+1]) + str.upper(record.seq[x+2])
                    elif codon_position == 2:
                        reference_codon = str.upper(wuhan_spike[x-1]) + str.upper(wuhan_spike[x]) + str.upper(wuhan_spike[x+1]) #ok?
                        alt_codon = str.upper(record.seq[x-1]) + str.upper(record.seq[x]) + str.upper(record.seq[x+1])
                    elif codon_position == 0:
                        reference_codon = str.upper(wuhan_spike[x-2]) + str.upper(wuhan_spike[x-1]) + str.upper(wuhan_spike[x])
                        alt_codon = str.upper(record.seq[x-2]) + str.upper(record.seq[x-1]) + str.upper(record.seq[x])
                    
                    if re.search('[NYRWSKM-]', alt_codon) == None: #If the alternate codon does not contain ambiguities, then append information to lists
                        ref_aa_pos = math.ceil((x +1)/ 3)
                        aa_pos_list.append(ref_aa_pos)
                        ref_codon_list.append(reference_codon)
                        alt_codon_list.append(alt_codon)
                    
                        coordinate_list.append(x + 1) #string starts at 0, add 1 for true nt position
                        reference_list.append(str(wuhan_spike[x]))
                        alternate_list.append(str.upper(record.seq[x]))
                        



                    #print(x, wuhan_spike[x], str.upper(record.seq[x]))
        # print(len(coordinate_list))
        # print(len(reference_list))
        # print(len(alternate_list))
        # print(len(ref_codon_list))
        # print(len(alt_codon_list))
        #print(aa_pos_list)
        #print(alt_codon_list)
        sequence_frame['POS'] = coordinate_list
        sequence_frame['REF'] = reference_list
        sequence_frame['ALT'] = alternate_list
        sequence_frame['AA_POS'] = aa_pos_list
        sequence_frame['REF_CODON'] = ref_codon_list
        sequence_frame['ALT_CODON'] = alt_codon_list
        
        aa_mismatch = len(set(aa_pos_list))
        sequence_frame['AA_MISM'] = aa_mismatch
        for each_ref_codon in ref_codon_list: #Convert ref codon to AA
            if len(each_ref_codon) == 3:
                ref_aa = codon_table[each_ref_codon]
                ref_aa_list.append(ref_aa)
            else:
                ref_aa_list.append("Non-SNP") 
        sequence_frame['REF_AA'] = ref_aa_list
        for each_alt_codon in alt_codon_list: #Convert alt codon to AA
            if len(each_alt_codon) == 3 and each_alt_codon != "del" and re.search('[-N]',each_alt_codon) == None:
                alt_aa = codon_table[each_alt_codon]
                alt_aa_list.append(alt_aa)
            elif each_alt_codon == "del":
                alt_aa_list.append("del")
            # elif str(each_alt_codon).startswith('-'):
            #     alt_aa_list.append("del")
            else:
                alt_aa_list.append("Non-SNP") 
        sequence_frame['ALT_AA'] = alt_aa_list
        sequence_frame.insert(0, "REGION", 'spike_gene')
        if keep_only_aa == True: #Allows only a single entry for each amino acid position. Keeps only first nucleotide mismatch of codon
            sequence_frame.drop_duplicates(subset=['AA_POS'], keep='first', inplace=True)
        if remove_synonymous == True:
            sequence_frame = sequence_frame[sequence_frame['REF_AA'] != sequence_frame['ALT_AA']]

        if len(coordinate_list) > 1:
            sequence_frame['SAMPLE'] = str(record.id)
            sequence_frame['IDENTITY'] = round((len(record.seq) - mismatch_count) / len(record.seq), ndigits=3)
            sequence_frame['AMBIG'] = round(ambig_count / len(record.seq), ndigits=3)
            vcf_frame = pd.concat([vcf_frame, sequence_frame])
        
        
        #print(vcf_frame)
        if sequence_count % 100 == 0:
            print("Sequences completed: %s\r" % (sequence_count))

vcf_frame.to_csv(output_file_name + "_test.csv", index=False)

##########
#
# Convert dataframe to visualization format
#
##########


aa_index = ['F','L','I','M','V','S','P','T','A','Y','*','H','D','N','K','E','Q','C','W','R','G','del']
wuhan_spike_protein = 'MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT*'


tally_frame = pd.DataFrame(columns = aa_index, index= range(1, 1275))
tally_frame.fillna(0, inplace=True)

for index, row in vcf_frame.iterrows():
    if row['ALT_AA'] != "Non-SNP":
        tally_frame.at[row['AA_POS'], row['ALT_AA']] += 1 

aa_position_count = []
for position in range(0, len(wuhan_spike_protein)):
    aa_position_count.append(str(wuhan_spike_protein[position] + str(position + 1).zfill(4)))

tally_frame.insert(0, 'REFERENCE', aa_position_count)

#print(tally_frame)

tally_frame.to_csv('%s_mutation_tally.csv' % (output_file_name) ,index = False)

end_time = time.time()
elapsed_time = (end_time - start_time) / 60 # Minutes

print(str(elapsed_time) + " minutes to complete")
