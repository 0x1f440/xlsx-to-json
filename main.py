import os
import glob
import pandas

excel_files = [file for file in glob.glob('*.{}'.format('xlsx'))]

for file_name in excel_files:
    workbook = pandas.ExcelFile(file_name)

    for sheet_name in workbook.sheet_names:
        sheet = pandas.read_excel(workbook, sheet_name=sheet_name)
        keys = sheet.keys()

        for lang_code in keys[1:]:
            folder_name = lang_code.upper()
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            df = sheet[[keys[0], lang_code]].set_index(keys[0])
            json_file = open(f'{folder_name}/{sheet_name}.json', mode='w', encoding='utf-8')
            json_file.write(df.transpose().to_json(orient='index', force_ascii=False).split(':', 1)[-1][:-1])
            json_file.close()

