"""Model configurations in json format. 
Paths are always relative to the location of the script being run,
paths are not relative to any objects in the source codes.
If running scripts are not in the folder `scripts` - parallel to the src folder
then the paths here need to be checked and modified accordingly"""


# "./" = root folder of the project
CFG = {
    "data": {
        "path": "../data/sample_articles/",
        "x": "",
        "y": "",
        "test_size": 0.2,
        "random_state": 2022,
        "ngram_range": (1, 2),
        "min_df": 10

    },
    "train": {
            "solver": "liblinear",
            "max_iter": 1000,
            "random_state": 2022,
            "C": 0.01,
            "penalty": "l2",
    },
    "output": {
        "output_path": "../models/",
        "model_name": "",
    }
}