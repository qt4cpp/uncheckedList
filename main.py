import handlefile
from handleexcel import set_styles
from manage_examlist import get_departments_from_df, get_unchecked_list

if __name__ == '__main__':
    unchecked_list = get_unchecked_list(sort=True)
    departments = get_departments_from_df(unchecked_list)

    handlefile.write_excel('test.xlsx', unchecked_list, departments)
    wb = handlefile.open_excel('test.xlsx')
    set_styles(wb)
