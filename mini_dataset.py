import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--num_frame", default = 20, type=int, help= "Number of data frames to slice")
parser.add_argument("--save_path", default= "Audio-Processing", type=str, help="Save path")
opt = parser.parse_args()

num_frame = opt.num_frame
save_path = opt.save_path

data_frame = pd.read_csv("train_meta.csv")
mini_dataset = data_frame.head(num_frame)
mini_dataset.to_csv("mini_dataset.csv")