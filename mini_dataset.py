import os
import sys 
import shutil
import pandas as pd
import argparse

sys.path.append(".")

parser = argparse.ArgumentParser()
parser.add_argument("--num_frame", default = 20, type=int, help= "Number of data frames to slice")
parser.add_argument("--org_path_hum", default= "hum", type=str, help="Original path of hum audios")
parser.add_argument("--org_path_song", default='song', type=str, help="Original path of songs")
parser.add_argument("--new_path_hum", default = "mini_dataset_hum", type=str, help="New path for mini dataset of hum audios")
parser.add_argument("--new_path_song", default= "mini_dataset_song", type=str, help="New path for mini dataset of songs")
opt = parser.parse_args()

num_frame = opt.num_frame
org_path_hum = opt.org_path_hum
org_path_song = opt.org_path_song
new_path_hum = opt.new_path_hum
new_path_song = opt.new_path_song

# # Slice datafeame
# data_frame = pd.read_csv("train_meta.csv")
# mini_dataset = data_frame.head(num_frame)
# mini_dataset.to_csv("mini_dataset.csv")

# Slice music folder
if not os.path.exists(new_path_song):
    os.makedirs(new_path_song)

# all_files_hum = os.listdir(org_path_hum)
# all_files_hum.sort()

all_files_song = os.listdir(org_path_song)
all_files_song.sort()

for file in all_files_song[:20]:
    shutil.move(org_path_song + "/" + file, new_path_song + "/" + file)