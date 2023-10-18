from openpyxl.workbook import Workbook


def set_font(ws):
    pass


def draw_grid_line(ws):
    pass


def adjust_width(ws):
    pass


def set_styles(wb: Workbook):
    """
    Set styles to excel file.
    1. Set a Font
    2. Draw a grid line
    3. Adjust cells width to contents.
    :param wb: Edit excel file.
    :return:
    """
    for sheet in wb:
        set_font(sheet)
        draw_grid_line(sheet)
