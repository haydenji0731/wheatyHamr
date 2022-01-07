# author: Hyunjoo Ji
# description: calculating the transcript length

############################################################

# add imports here
import sys
import re

############################################################

def get_length(data_l):
#    d = dict()
    out_l = list()
    for x in data_l:
        tmp_l = x.split(".")
        out_l.append(tmp_l[0] + "." + tmp_l[1])
#        tmp2_l = re.split(';|=|:', tmp_l[14])
#         gene_id = tmp2_l[2]
#         if gene_id not in d.keys():
#             d[gene_id] = 1
        # if tmp_l[2] == "mRNA":
            #tmp2_l = re.split(';|=|:', tmp_l[12])
            #len = int(tmp_l[4]) - int(tmp_l[3])
            #d[tmp2_l[3]] = len
    return out_l


if __name__ == "__main__":
    # the annotatin must ONLY contain primary transcript
    file_name = input("Input annotation file:")
    output_name = input("Output file name:")
    file = open(file_name, "r")
    data = file.readlines()
    clean_l = list()
    for x in list(data):
        clean_l.append(x.rstrip("\n"))
    gene_len_d = get_length(clean_l)
    outfile = open(output_name, "w")
    for x in gene_len_d:
        outfile.write(x + "\n")
    # for x in gene_len_d.keys():
    #     outfile.write(x + "\n")
    outfile.close()