import csv
import xlrd
with open('aqi.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    max_aqi=150 #預設
    max_city=''
    # read file row by row 
    for row in reader:
        if row[2] !='AQI':
            if int(row[2])< max_aqi:
                max_aqi=int(row[2])
                max_city=row[0]
        else:
            pass
        print(max_city+"空氣最好,"+"AQI是",str(max_aqi))


# data = xlrd.open_workbook('aqi.csv')
# print(xl.sheet_names())#獲取所有sheet的名字
# print(xl.nsheets)
# print(xl.sheets())
# print(xl.sheet_by_name('目錄')) #通過名稱獲取
# print(xl.sheet_by_index(1)) #通過索引獲取

