import openpyxl
import csv
from datetime import datetime

def xlsx_to_csv(xlsx_file_path, csv_file_name_without_extension, delimiter='|'):
    
    # Formatear el nombre del archivo de salida con la marca de tiempo
    now = datetime.now()
    formatted_now = now.strftime('%Y%m%d_%H_%M_%S')

    csv_file_path = f"{csv_file_name_without_extension}_{formatted_now}.csv"
    
    # Cargar el libro de Excel
    workbook = openpyxl.load_workbook(xlsx_file_path)
    # Seleccionar explícitamente la primera hoja del libro
    sheet = workbook.worksheets[0]
    
    with open(csv_file_path, 'w', newline="", encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=delimiter)
        # Empezar desde la tercera fila y descartar la primera columna de cada fila
        for row in sheet.iter_rows(min_row=2, values_only=True):
            # Usar slicing [1:] para descartar el primer elemento de cada fila
            writer.writerow(row[1:])

# xlsx_to_csv('dynamicGigante.xlsx', 'outputDynamicGigante')
xlsx_to_csv('original.xlsx', 'output_')
