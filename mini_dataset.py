import os
import sys 
import shutil
import pandas as pd
import argparse

sys.path.append(".")

parser = argparse.ArgumentParser()
parser.add_argument("--num_frame", default = 20, type=int, help= "Number of data frames to slice")
parser.add_argument("--org_path", default= "dataset", type=str, help="Original path of audio")
parser.add_argument("--new_path", default = "mini_dataset", type=str, help="New path for mini dataset")
opt = parser.parse_args()

num_frame = opt.num_frame
org_path = opt.org_path
new_path = opt.new_path

# Slice datafeame
data_frame = pd.read_csv("train_meta.csv")
mini_dataset = data_frame.head(num_frame)
mini_dataset.to_csv("mini_dataset.csv")

# Slice music folder
all_files = os.listdir(org_path)

for file in all_files[:20]:
    shutil.move(org_path + file, new_path + file)