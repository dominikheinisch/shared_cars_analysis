import pandas as pd
from ast import literal_eval


DATASETS_DIR = 'datasets/'
SAMPLE_FILE = DATASETS_DIR + 'shared-cars-sample.csv'


def load_df():
    return pd.read_csv(
        filepath_or_buffer=SAMPLE_FILE,
        converters={'cars_list': literal_eval},
        parse_dates=['timestamp']
    )
