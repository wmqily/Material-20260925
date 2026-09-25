import pandas as pd

csv_file_path = 'mooc.csv'  df = pd.read_csv(csv_file_path,encoding='utf-8')
import pandas as pd

# csv_file_path = '1.csv'  
# import chardet
#
# with open(csv_file_path, 'rb') as f:
#     result = chardet.detect(f.read())
# df = pd.read_csv(csv_file_path, encoding=result['encoding'])

column_name = 'Comment content' 
column_data = df[column_name]

txt_file_path = 'output.txt'  
with open(txt_file_path, 'w', encoding='utf-8') as file:
    for item in column_data:
        file.write(f"{item}\n")

print(f"column '{column_name}'  content has been successfully written '{txt_file_path}'")
