import pandas as pd
from eurostatapiclient import  EurostatAPIClient

def eurotstat_client(CODE_MAIN : str, params : bytearray):
    VERSION = 'v2.1'
    # Only json is currently available
    FORMAT = 'json'
    # Specify language : en, fr, de
    LANGUAGE = 'en'
    client = EurostatAPIClient(VERSION, FORMAT, LANGUAGE)
    dataset = client.get_dataset(CODE_MAIN)
    print(dataset.label)

    df1 = client.get_dataset(CODE_MAIN, params=params)
    df1 = df1.to_dataframe()
    df1 = df1[["values", "time","geo"]] #keep only this cells
    df = df1.dropna() #drop row if any value is null
    df.to_csv('./data/eurostat.csv', index=True)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    CODE_MAIN = 't2020_rk210'
    params = {
        'siec': 'C0000X0350-0370',        'siec': 'E7000',        'siec': 'G3000',        'siec': 'H8000',
        'siec': 'O4000XBIO',        'siec': 'RA000',
        'precision': '1',        'unit': 'PC',        'nrg_bal': 'FC_OTH_HH_E'
    }

   # params = {
   #     'fieldid': 'VEG','fieldid': 'TOTAL','fieldid': 'ANI', 'precision': '1', 'unit': 'KCAL'
   # }
   # CODE_MAIN = 't2020_rk100'
    eurotstat_client(CODE_MAIN, params)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
