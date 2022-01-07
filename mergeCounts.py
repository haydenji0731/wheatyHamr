# author: Hyunjoo Ji
# description: merging intermediate mods counts

############################################################

# add imports here
import pandas as pd

############################################################


if __name__ == "__main__":
    trans_file_name = input("Input primary transcript list:")
    trans_file = open(trans_file_name, "r")
    trans_tmp_l = trans_file.readlines()
    trans_l = list()
    for x in trans_tmp_l:
        trans_l.append(x.rstrip("\n"))
    samp_file_name = input("Input sample list:")
    samp_file = open(samp_file_name, "r")
    samp_tmp_l = samp_file.readlines()
    samp_l = list()
    for x in samp_tmp_l:
        samp_l.append(x.rstrip("\n"))
    data_dir = input("Enter dir for your data:")
    


    # print(trans_l)
