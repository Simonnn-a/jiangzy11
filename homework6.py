#_*_ conding:utf-8 _*-
#@Time:2020/10/13 &{TIME}
# file=open('123.txt','r',encoding='utf-8')
# lines=file.readlines()
# print(lines)
#
# for i in lines:
#     print(i.split(',')[0])
#
# with open('123.txt','r',encoding='utf-8') as file1:
#     lines1=file1.readlines()
#     print(lines1)

import csv
file=csv.reader(open('234.csv','r',encoding='utf-8'))
for i in file:
    print(i)

with open('234.csv','r',encoding='utf-8') as file4:
    lines=file4.readlines()
    print(lines)
for j in lines:
    print(j.split(',')[0])
stu1=['somon','11','shanxi']
stu2=['bob','22','guilin']
file0=open('234.csv','a+',newline='')
write=csv.writer(file0,dialect='excel')
write.writerow(stu1)
write.writerow(stu2)

from xml.dom import minidom
dom=minidom.parse('qwe.xml')
root=dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
dom=minidom.parse('qwe.xml')
root=dom.documentElement
name1=root.getElementsByTagName('name')
age1=root.getElementsByTagName('age')
city1=root.getElementsByTagName('city')
print(name1[1].firstChild.data)
print(age1[1].firstChild.data)
print(city1[1].firstChild.data)

for i in range(4):
    print(name1[1].firstChild.data)
    print(age1[1].firstChild.data)
    print(city1[1].firstChild.data)
from xml.dom import minidom
dom=minidom.parse('qwe.xml')
root=dom.documentElement
root1=root.getElementsByTagName('studuent')
print(root1[0].nodeName)
print(root1[0].nodeValue)
print(root1[0].nodeType)











