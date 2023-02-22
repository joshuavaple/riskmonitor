"""Dataloader class to load raw json files and process them"""
import json
import os
import pandas as pd

class DataLoader:

    @staticmethod
    def load_json(data_config):
        """Loads json files of common keys in a specified folder path and returns the following:
        a list of article dictionaries, a dictionary of combined common keys, and a pandas dataframe"""
        data_path = data_config.path
        article_list = []
        article_dict = {}
        for json_file_name in os.listdir(data_path):
            json_file_path = os.path.join(data_path, json_file_name)
            with open(json_file_path) as f:
                data = json.load(f)
            article_list.append(data)
        for article in article_list:
            for k in article.keys():
                article_dict[k] = tuple(d[k] for d in article_list) # as a tuple is created, no need to flatten and put in lists
        article_df = pd.DataFrame(article_dict)
        return article_list, article_dict, article_df
    
    @staticmethod
    def process_data(data_config):
        pass
