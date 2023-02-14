import json
import os

data_dir = r'../data/sample_articles'
file_list = [f for f in os.listdir(data_dir) if '.json' in f]

def print_samples():
    for file_name in file_list:
        with open(os.path.join(data_dir, file_name), 'r') as file:
            data = json.load(file)
        print(data)
        print('='*50)


if __name__ == '__main__':    
    print_samples()
    print(file_list)