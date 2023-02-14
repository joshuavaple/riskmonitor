import json
import os


file_list = [f for f in os.listdir() if '.json' in f]

def print_samples():
    for file_name in file_list:
        with open(file_name, 'r') as file:
            data = json.load(file)
        print(data)
        print('='*50)


if __name__ == '__main__':    
    print_samples()