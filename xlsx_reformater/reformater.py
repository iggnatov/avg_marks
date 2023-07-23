import csv

from openpyxl import Workbook, load_workbook


def reformat():
    """Reformat table.xlsx to a file.csv with only necessary columns"""

    wb = load_workbook(filename='mytable.xlsx')
    ws = wb.active
    ws.unmerge_cells('A1:Q1')
    ws.delete_rows(1)

    ws.delete_cols(1, 4)
    ws.delete_cols(5, 4)
    ws.delete_cols(6, 1)
    ws.delete_cols(7, 2)

    rows = ws.max_row

    ws['A1'].value = 'spec_code_id'
    ws['B1'].value = 'financing_type'
    ws['C1'].value = 'originals'
    ws['D1'].value = 'avg_marks'
    ws['E1'].value = 'grade'
    ws['F1'].value = 'certificate_number'

    for row in ws.iter_rows(min_row=1, min_col=1, max_col=6, max_row=1):
        for cell in row:
            if 'Техническая эксплуатация' in cell.value:
                cell.value = cell.value.replace(' (по отраслям)', '')

    for row in ws.iter_rows(min_row=2, min_col=1, max_col=1, max_row=rows):
        for cell in row:
            if 'Техническая эксплуатация' in cell.value:
                cell.value = cell.value.replace(' (по отраслям)', '')

    for row in ws.iter_rows(min_row=2, min_col=2, max_col=2, max_row=rows):
        for cell in row:
            if cell.value == 'Бюджет':
                cell.value = True
            else:
                cell.value = False

    for row in ws.iter_rows(min_row=2, min_col=3, max_col=3, max_row=rows):
        for cell in row:
            if cell.value == 'Сдан':
                cell.value = True
            else:
                cell.value = False

    # for row in ws.iter_rows(min_row=2, min_col=4, max_col=4, max_row=rows):
    #     for cell in row:
    #         print(cell.value)

    for row in ws.iter_rows(min_row=2, min_col=5, max_col=5, max_row=rows):
        for cell in row:
            if cell.value == 'Аттестат об основном общем образовании':
                cell.value = True
            else:
                cell.value = False

    wb.save('mytable1.xlsx')
    wb.close()

    with open('test.csv', 'w', newline="") as f:
        c = csv.writer(f)
        for r in ws.rows:
            c.writerow([cell.value for cell in r])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reformat()
