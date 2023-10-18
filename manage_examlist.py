import pandas as pd

import handlefile


def get_departments_from_df(df:pd.DataFrame):
    return list(set(df["依頼科"]))


def get_unchecked_index(df: pd.DataFrame):
    return df.isna().loc[:, "確認"]


def sort_list(df: pd.DataFrame):
    return df.sort_values(["依頼医", "検査日"])


def get_unchecked_list(sort=True):
    header = handlefile.read_header(path="header")
    exam_list = handlefile.read_csv("data/1005.csv", filter_list=header)
    unchecked_index = get_unchecked_index(exam_list)
    unchecked_list = exam_list[unchecked_index]
    if sort:
        return sort_list(unchecked_list)
    return unchecked_list


def remove_unnecessary_columns(df: pd.DataFrame, index):
    return df.iloc[:, index:]

