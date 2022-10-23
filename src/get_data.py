import os
import yaml
import pandas as pd
import argparse
import PIL



def read_params(config_path):
    with open(config_path,'r') as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config=read_params(config_path)
    #print(config)
    input_path = []
    label = []

    for clas in os.listdir("data_given"):
        for path in os.listdir("data_given/"+ clas):
            if clas == "Cat":
                label.append(0)
            else:
                label.append(1)
            input_path.append(os.path.join("data_given", clas, path))

    print(input_path[0], label[0])
    print(len(label))
    df = pd.DataFrame()
    df["image"] = input_path
    df["label"] = label
    df = df.sample(frac=1).reset_index(drop=True)

    df['label'] = df['label'].astype('str')

    

    df = df[df['image'] != 'PetImages/Cat/Thumbs.db']
    df = df[df['image'] != 'PetImages/Dog/Thumbs.db']
    df = df[df['image'] != 'PetImages/Cat/666.jpg']
    df = df[df['image'] != 'PetImages/Dog/11702.jpg']
    return df


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    data=get_data(config_path=parsed_args.config)