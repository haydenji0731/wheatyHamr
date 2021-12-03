# author: Hyunjoo Ji
# description: extracting primary transcript from the IWGSC wheat annotation file

############################################################

# add imports here
import sys
import re

############################################################


def pre_process(data):
    data_l = list(data)
    clean_l = list()
    for x in data_l:
        if len(x) == 9:
            clean_l.append(x)
    return clean_l

def store_primary_trans(data_l):
    d = dict()
    for x in data_l:
        tmp_l = x.split("\t")
        # if tmp_l[2] == "gene" or tmp_l[2] == "ncRNA_gene":
        if tmp_l[2] == "gene":
            tmp2_l = re.split(';|=|:', tmp_l[8])
            # add the gene key with a random placeholder
            # the value for a gene key is a tuple (longest transcript length, transcript id)
            d[tmp2_l[2]] = (-1, "blah")
        # elif tmp_l[2] == "mRNA" or tmp_l[2] == "rRNA":
        elif tmp_l[2] == "mRNA":
            tmp2_l = re.split(';|=|:', tmp_l[8])
            parent = tmp2_l[5]
            parent_val = d[parent]
            max = parent_val[0]
            curr = int(tmp_l[4]) - int(tmp_l[3])
            if curr > max:
                new_tup = (curr, tmp2_l[2])
                d[parent] = new_tup
    return d

def extract(gene_d):
    val_l = list()
    for x in gene_d.keys():
        val = gene_d[x]
        val_l.append(val[1])
    return val_l

if __name__ == "__main__":
    # will throw an error if no file is specified in the program call
    # file_name = sys.argv[1]
    file_name = input("Input annotation file:")
    output_name = input("Output file name:")
    file = open(file_name, "r")
    data = file.readlines()
    clean_l = list()
    for x in list(data):
        if len(x.split("\t")) == 9:
            clean_l.append(x)
    gene_d = store_primary_trans(clean_l)
    trans_l = extract(gene_d)
    outfile = open(output_name, "w")
    for x in trans_l:
        outfile.write(x + "\n")
    outfile.close()



