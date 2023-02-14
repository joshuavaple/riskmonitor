import json
import importlib

def load_data_model():
    with importlib.resources.open_text("riskmonitor.datamodel", "model_article.json") as file:
        model_article = json.load(file)
    print(model_article)

if __name__ == '__main__':
    load_data_model()
