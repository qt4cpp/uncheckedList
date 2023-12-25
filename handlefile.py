import csv
import os
import sys

import pandas as pd
from openpyxl.reader.excel import load_workbook


def read_header(path='header'):
    with open(path) as f:
        lines = list(csv.reader(f, skipinitialspace=True))
    return lines[0]


def read_csv(csv_path, filter_list):
    df = pd.read_csv(csv_path)
    return df.loc[:, filter_list]


def sjis_to_utf8(file_path):
    with open(file_path, 'r', encoding='cp932') as file:
        utf8_text = file.read().encode('utf-8')
    with open(file_path, 'w') as file:
        file.write(utf8_text.decode('utf-8'))


def write_excel(path, exam_list, departments):
    with (pd.ExcelWriter(path, mode='w') as writer):
        for department in departments:
            department_df = exam_list[exam_list["依頼科"] == department]
            new_df = department_df.reset_index()
            new_df.iloc[:, 2:].to_excel(writer, sheet_name=department)


def open_excel(file):
    return load_workbook(filename=file)
