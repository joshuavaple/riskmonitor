from riskmonitor.configs.config import CFG


# check DataLoader class:
def run():
    from riskmonitor.configs.config import CFG
    from riskmonitor.utils.config import Config
    from riskmonitor.dataloader.dataloader import DataLoader
    config = Config.from_json(CFG)
    data_config = config.data
    dataloader = DataLoader()
    _,_,article_df = DataLoader().load_json(data_config=data_config)
    print(article_df)


if __name__ == "__main__":
    run()
