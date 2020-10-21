import csv
import re
import os
import shutil


mod_line_name='Name'
base_line_valuePart="work"
mod_line_valuePart="test"
csv_name='test'

mod_line_name_Index=0

header=[]
data=[]
type=[]

int32_pattern=re.compile('\d*')
float_pattern=re.compile('\d*[.]\d*')
type_priority=['FString','float','int32','blank']

def modfiyCsvData(list):
    for row in list:
        line_value = row[mod_line_name_Index]
        line_value=re.sub(base_line_valuePart,mod_line_valuePart,line_value)
        row[mod_line_name_Index]=line_value
    return list
 


def CheckType(value):
    m= re.match(int32_pattern,value)
    if m!=None:
        if m.span()==(0,len(value)):
            return 'int32'
        else:
            m= re.match(float_pattern,value)
            if m!=None:
                if m.span()==(0,len(value)):
                    return 'float'
  
    return 'FString'

def Type(value,index):
    mtype=CheckType(value)
    
    m= type_priority.index(mtype)
    n= type_priority.index(type[index])

    if (m<n):
        type[index]=mtype



with open(csv_name+'.csv', encoding='utf-8') as csvfile:
    header.clear()
    data.clear()
    type.clear()
    reader=csv.reader(csvfile)
    header=next(reader)

    for row in header:
        type.append('blank')

    mod_line_name_Index= header.index(mod_line_name)

    for row in reader:
        data.append(row)
        print(row)
        x=0
        for element in row:  
           print(CheckType(element))
           Type(element,x)
           x=x+1



for m in os.listdir():
    if m=='Result':
        shutil.rmtree('Result') 
        break   
       
os.makedirs('Result')
os.makedirs('Result/Struct')


new_csv_path='Result/'+ csv_name +'_result.csv'
with open(new_csv_path, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    data=modfiyCsvData(data)
    writer.writerows(data)

new_csv_struct_path='Result/Struct/'+csv_name+'_struct.h'
with open(new_csv_struct_path, 'w', encoding='utf-8', newline='') as hfile:
    writer = csv.writer(hfile)
    writer.writerow(['USTRUCT(BlueprintType)'])	
    writer.writerow(['struct '+csv_name+'_Struct'])
    writer.writerow(['{'])
    writer.writerow([ '\t'+'GENERATED_USTRUCT_BODY()'])
    writer.writerow([' '])
    x=0
    for row in header:
        if x==0:
            pass
        else:
            str='\t'+type[x]+'\t'+header[x]+','+'\n'
            hfile.write(str)
            pass
        x=x+1
    writer.writerow(['}'])
