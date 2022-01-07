# author: Hyunjoo Ji
# description: exclude transcript IDs without a mod

############################################################

# add imports here
import re

############################################################

def deleteNonmodified(data_l):
    modified_l = list()
    for x in data_l:
        x_l = re.split(',', x)
        isModified = False
        for i in range(1, 97):
            # if x_l[1] == '"gene_name"':
            #     break
            if x_l[i] != '0':
                isModified = True
                break
        if isModified:
            modified_l.append(x)
    return modified_l

if __name__ == "__main__":
    # the annotatin must ONLY contain primary transcript
    file_name = input("Input merged mod count csv file:")
    output_name = input("Output file name:")
    file = open(file_name, "r")
    data = file.readlines()
    data_l = list()
    for x in data:
        data_l.append(x.rstrip("\n"))
    modified_l = deleteNonmodified(data_l)
    outfile = open(output_name, "w")
    for x in modified_l:
        outfile.write(x + "\n")
    outfile.close()

