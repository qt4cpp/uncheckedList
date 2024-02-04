import csv

import pandas as pd
from openpyxl.reader.excel import load_workbook


def read_header(path='header'):
    """headerファイルを読み出す"""
    with open(path, encoding='utf-8') as f:
        lines = list(csv.reader(f, skipinitialspace=True))
    return lines[0]


def read_csv(csv_path, filter_list):
    """csvファイルを読み出す"""
    df = pd.read_csv(csv_path)
    return df.loc[:, filter_list]


def sjis_to_utf8(file_path):
    """windowsでcp932のファイルが渡されたらutf-8に変換して返す"""
    with open(file_path, 'r', encoding='cp932') as file_cp932:
        text = file_cp932.read()
    with open(file_path, 'w', encoding='utf-8') as file_utf8:
        file_utf8.write(text)


def write_excel(path, exam_list, departments):
    """excelファイルを書き出す"""
    departments.sort()
    with (pd.ExcelWriter(path, mode='w') as writer):
        for department in departments:
            department_df = exam_list[exam_list["依頼科"] == department]
            new_df = department_df.reset_index()
            new_df.iloc[:, 2:].to_excel(writer, sheet_name=department)


def open_excel(file):
    """excelファイルを開く"""
    return load_workbook(filename=file)
