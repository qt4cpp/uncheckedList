import pandas as pd

import handlefile


def get_departments_from_df(df:pd.DataFrame):
    """DataFrameのから含まれる診療科を収集する"""
    return list(set(df["依頼科"]))


def get_unchecked_index(df: pd.DataFrame):
    """所見を確認していないものだけを抽出する"""
    return df.isna().loc[:, "確認"]


def sort_list(df: pd.DataFrame):
    """依頼医と検査日でソートする"""
    return df.sort_values(["依頼医", "検査日"])


def filter_reading_required(df: pd.DataFrame) -> pd.DataFrame:
    """要読影があるものだけにするフィルタリングする"""
    required_reading_df = df.dropna(subset=["要読影"])
    return required_reading_df


def filter_departments(df: pd.DataFrame, department_list) -> pd.DataFrame:
    """診療科を限定する"""
    filtered_df = df[df["依頼科"].isin(department_list)]
    return filtered_df


def get_unchecked_table(csv_path, header_path, sort=True):
    """確認されていないテーブルを返す、操作用の関数"""
    header = handlefile.read_header(path=header_path)
    exam_list = handlefile.read_csv(csv_path, filter_list=header)
    unchecked_index = get_unchecked_index(exam_list)
    unchecked_list = exam_list[unchecked_index]
    if sort:
        return sort_list(unchecked_list)
    return unchecked_list


def remove_unnecessary_columns(df: pd.DataFrame, index):
    """必要なインデックスだけを抽出して返す"""
    return df.iloc[:, index:]

