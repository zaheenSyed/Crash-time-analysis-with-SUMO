# python
## XML to CSV 

## https://www.pythonpool.com/python-xml-to-csv/


import xml.etree.ElementTree as ET
import csv
 
tree = ET.parse("sample.xml")
root = tree.getroot()
 
Resident_data = open('ResidentData.csv', 'w')
 
csvwriter = csv.writer(Resident_data)
resident_head = []
 
count = 0
for member in root.findall('Resident'):
    resident = []
    address_list = []
    if count == 0:
        name = member.find('Name').tag
        resident_head.append(name)
        Phone = member.find('Phone').tag
        resident_head.append(Phone)
        Email = member.find('Email').tag
        resident_head.append(Email)
         
        csvwriter.writerow(resident_head)
        count = count + 1
 
    name = member.find('Name').text
    resident.append(name)
    Phone = member.find('Phone').text
    resident.append(Phone)
    Email = member.find('Email').text
    resident.append(Email)
     
    csvwriter.writerow(resident)
 
 
Resident_data.close()
print("it works")
