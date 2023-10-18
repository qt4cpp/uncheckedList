import pandas as pd

import handlefile
from manage_examlist import get_unchecked_index, get_departments_from_df, get_unchecked_list

if __name__ == '__main__':
    unchecked_list = get_unchecked_list(sort=True)
    departments = get_departments_from_df(unchecked_list)

    handlefile.write_excel('test.xlsx', unchecked_list, departments)
