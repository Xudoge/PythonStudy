
import os         #文件库
import shutil     #比os更高级的文件库
import csv        #csv表格处理
import re         #正则表达式


list_csv=[]
 
print(os.listdir())

# 识别py文件目录下的csv表
for file in os.listdir():
    if os.path.splitext(file)[1]=='.csv':
        list_csv.append(file)


# UE4 数据类型正则表达式
int32_pattern=re.compile('\d*')              #整形
float_pattern=re.compile('\d*[.]\d*')        #浮点数
num_pattern='\d*[.]?\d*'                     #整形或者浮点数
bool_pattern=re.compile('(True)|(False)')    #布尔
vec2_pattern=re.compile('\(X\='+num_pattern+',Y='+num_pattern+'\)')                                      #vec2
vec3_pattern=re.compile('\(X\='+num_pattern+',Y='+num_pattern+',Z='+num_pattern+'\)')                    #vec3
rot_pattern=re.compile('\(Pitch\='+num_pattern+',Yaw\='+num_pattern+',Roll\='+num_pattern+'\)')          #rotator
#transfrom
tra_pattern=re.compile('\(Rotation\=\(X\='+num_pattern+',Y\='+num_pattern+',Z\='+num_pattern+',W\='+num_pattern+'\),Translation\=\(X\='+num_pattern+',Y\='+num_pattern+',Z\='+num_pattern+'\),Scale3D\=\(X\='+num_pattern+',Y\='+num_pattern+',Z\='+num_pattern+'\)\)')

tarray_pattern=re.compile('\(\,+\)')
tarray_pattern_str=re.compile('\((.*\,+.*\)*)')

pattern_list=[
{'TypeName':'int32','Pattern':int32_pattern},
{'TypeName':'float','Pattern':float_pattern},
{'TypeName':'bool','Pattern':bool_pattern},
{'TypeName':'FVector','Pattern':vec3_pattern},
{'TypeName':'FVector2D','Pattern':vec2_pattern},
{'TypeName':'FRotator','Pattern':rot_pattern},
{'TypeName':'FTransform','Pattern':tra_pattern}
]

# 类型优先级 如果第一次判断出int，但第二次是FString则是FString   
type_priority=['FString' ,'bool','FVector','FVector2D','FRotator','FTransform','float','int32','blank']


#  类型检测
def CheckType(value):       

    if value=='':
        return {'TypeName':'FString','isArray':False}

    # 循环匹配
    for m_pattern in pattern_list:
        m=re.search(m_pattern['Pattern'],value)
        if m!=None:
            if m.span()==(0,len(value)):
                return {'TypeName':m_pattern['TypeName'],'isArray':False}
            else:
                # 如果不匹配则删除匹配的部分，拿剩余剩余字段，判断其是不是一个数组
                v=''
                n= re.sub(m_pattern['Pattern'],v,value,0)
                r=re.match(tarray_pattern,n)
                if r!=None:
                    return {'TypeName':m_pattern['TypeName'],'isArray':True}
  
    # 判断是不是字符数组   
    m=re.match(tarray_pattern_str,value)
    if m!=None:
        if m.span()==(0,len(value)):
            return {'TypeName':'FString','isArray':True}
    
    return {'TypeName':'FString','isArray':False}


#  类型确认
type=[]
def Type(value,index):
    mtype=CheckType(value)
    
    v={'TypeName':'blank','isArray':False}

    m= type_priority.index(mtype['TypeName'])
    n= type_priority.index(type[index]['TypeName'])

    m_bool=mtype['isArray']
    n_bool=type[index]['isArray']

    if (m<n):
        v['TypeName']=mtype['TypeName']
        
    # 如果type已经判断为非数组，那么接下来它也不可能是数组 
    if n_bool==False:
        v['isArray']=False
    else:
        v['isArray']=m_bool

    type[index]=v



# 删除老文件，创建新Result文件
for m in os.listdir():
    if m=='Result':
        shutil.rmtree('Result') 
        break   
       
os.makedirs('Result')


# UStruct生成
for m in list_csv:

    csv_name=os.path.splitext(m)[0]

    with open(m,encoding='utf-8')as  csvfile:
        type.clear()
        reader=csv.reader(csvfile)
        header=next(reader)


        for row in header:
            
            type.append({'TypeName':'blank','isArray':True})

        for row in reader:
            x=0
            for element in row: 
                Type(element,x)
                x=x+1

        new_csv_struct_path='Result/'+csv_name+'_Struct.h'
        with open(new_csv_struct_path, 'w', encoding='utf-8', newline='') as hfile:
            writer = csv.writer(hfile)
            writer.writerow(['USTRUCT(BlueprintType)'])	
            writer.writerow(['struct F'+csv_name+'_Struct'+' : public FTableRowBase'])
            writer.writerow(['{'])
            writer.writerow([ '\t'+'GENERATED_USTRUCT_BODY()'])
            writer.writerow([' '])
            x=0
            for row in header:
                if x==0:
                    pass
                else:
                    writer.writerow([ '\t'+'UPROPERTY()'])
                    if type[x]['isArray']==True:
                        str='\t'+'TArray<'+type[x]['TypeName']+'>'+'\t'+header[x]+';'+'\n'
                    else:
                        str='\t'+type[x]['TypeName']+'\t'+header[x]+';'+'\n'
                    hfile.write(str)
                    pass
                x=x+1
                writer.writerow([' '])
            writer.writerow(['};'])