import handlefile
from handleexcel import set_styles
from manage_examlist import get_departments_from_df, get_unchecked_table

if __name__ == '__main__':
    csv_path = 'data/未確定1026.csv'
    header_path = 'header'
    unchecked_table = get_unchecked_table(csv_path=csv_path, header_path=header_path, sort=True)
    departments = get_departments_from_df(unchecked_table)

    handlefile.write_excel('test.xlsx', unchecked_table, departments)
    wb = handlefile.open_excel('test.xlsx')
    set_styles(wb)
