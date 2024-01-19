from openpyxl.styles import Font, Side, Border

from openpyxl.workbook import Workbook


def set_font(ws):
    font = Font(name='MS PGothic',
                size=11)

    for row in ws:
        for cell in row:
            ws[cell.coordinate].font = font


def draw_grid_line(ws):
    side = Side(style='thin', color='000000')
    border = Border(top=side, right=side, bottom=side, left=side)

    for row in ws:
        for cell in row:
            ws[cell.coordinate].border = border


def adjust_width(ws):
    widths = {'A': 10, 'B': 20, 'C': 12, 'D': 12, 'E': 12,
              'F': 12, 'G': 8, 'H': 8, 'I': 25, 'J': 27, 'K': 20}
    for col, width in widths.items():
        ws.column_dimensions[col].width = width


def set_styles(wb: Workbook, file_path):
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
        adjust_width(sheet)

    wb.save(file_path)