import csv
import pandas as pd

# this is a new file that will have data as per out needs
fo_out = open('output.csv', 'w')

# this writer object would put data in the new file.
writer_obj = csv.writer(fo_out)

fo = open('test.csv')
for line_data in fo:
    writer_obj.writerow(line_data.split(',', 7))

fo_out.close()

# load the new file having 8 columns.
df = pd.read_csv('output.csv',
                 names=['col1', 'col2', 'col3', 'col4','col5','col6', 'col7','col8'])

# removing the new line character \n present at end of the value.
df['col8'] = df['col8'].apply(lambda elem:elem.strip())
print(df)


