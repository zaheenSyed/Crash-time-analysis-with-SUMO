# Windows API to open EXCEL

## THis code does not work. 

# https://pythonexcels.com/python/2009/10/05/python-excel-mini-cookbook


from pickle import TRUE
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')

print("it started")
wb = excel.Workbooks.Open("D:\Github\Crash time analysis with SUMO\Data_run1_11sep21/zz.xlsx")
wb.XmlImport("D:\Github\Crash time analysis with SUMO\Data_run1_11sep21/traveltime.xml")
wb.SaveAs("result.xlsx")
wb.Close()

print("it worked")



