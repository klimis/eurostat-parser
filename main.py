import sys
from eurostatapiclient import EurostatAPIClient


def eurotstat_client(main_code: str, params):
    VERSION = 'v2.1'
    FORMAT = 'json'
    # Specify language : en, fr, de
    LANGUAGE = 'en'

    client = EurostatAPIClient(VERSION, FORMAT, LANGUAGE)
    dataset = client.get_dataset(main_code)

    print(dataset.label)

    df1 = client.get_dataset(main_code, params=params)
    df1 = df1.to_dataframe()
    df1 = df1[["values", "time", "geo"]]  # keep only this cells
    df = df1.dropna()  # drop row if any value is null
    df.to_csv("./data/eurostat %s.csv" % main_code, index=False)


def splitter(code: str):
    main_code = code.split('?')[0]
    param_part = code.split('?')[1]
    params = dict(item.split("=") for item in param_part.split("&"))  # split and convert to dict
    return main_code, params


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError('Please provide the eurostat api code inside double quotes')

    eurostat_param = sys.argv[1]
    main_code, params = splitter(eurostat_param)
    eurotstat_client(main_code, params)
