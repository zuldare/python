import openpyxl
import csv
import time

def convert_xlsx_to_csv(xlsx_path, csv_file_name_without_extension):
    # Excel is loaded in read mode in order to optimize memory use
    workbook = openpyxl.load_workbook(xlsx_path, read_only=True)
    sheet = workbook.worksheets[0]

    timestamp = int(time.time() * 1000)
    csv_file_path = f"{csv_file_name_without_extension}_{timestamp}.csv"
    

    with open(csv_file_path, 'w', newline="", encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # skip first line 
        first_row = True
        for row in sheet.rows:
            if first_row:  # omit first role
                first_row = False
                continue
            # skip first empty cell of files
            row_data = [cell.value for cell in row[1:]]  # Read
            csv_writer.writerow(row_data)

    # Cerramos el libro de trabajo para liberar memoria, importante especialmente en modo de solo lectura
    workbook.close()

# Uso de la función
convert_xlsx_to_csv('dynamicGigante.xlsx', 'ficheroOut')
