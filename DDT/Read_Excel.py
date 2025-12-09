import xlrd

def reading_testdata(filepath, sheetname):
    workbook = xlrd.open_workbook(filepath)            ## Book Obj
    worksheet = workbook.sheet_by_name(sheetname)      ## Sheet Obj
    rows = worksheet.get_rows()                        ## Generator Obj
    header = next(rows)

    d = {}
    for ele in rows:
        d[ele[0].value] =  ele[2].value
    return d


