import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

ws.append(['姓名','電話','Email'])
ws.append(['John','0987654321','asdf@gmail.com'])
ws.append(['John','0987654321','asdf@gmail.com'])
ws.append(['John','0987654321','asdf@gmail.com'])
ws.append(['John','0987654321','asdf@gmail.com'])
ws.append(['John','0987654321','asdf@gmail.com'])
ws.append(['John','0987654321','asdf@gmail.com'])
ws.append(['John','0987654321','asdf@gmail.com'])

wb.save('output.xlsx')