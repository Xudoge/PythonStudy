

import re

test_pattern=re.compile('\(X\=0.00')

int32_pattern=re.compile('\d*')              #整形
float_pattern=re.compile('\d*[.]\d*')        #浮点数
num_pattern='\d*[.]?\d*'                 #整形或者浮点数
bool_pattern=re.compile('(true)|(false)')   #布尔
vec2_pattern=re.compile('\(X\='+num_pattern+',Y='+num_pattern+'\)')                                      #vec2
vec3_pattern=re.compile('\(X\='+num_pattern+',Y='+num_pattern+',Z='+num_pattern+'\)')                    #vec3
rot_pattern=re.compile('\(Pitch\='+num_pattern+',Yaw\='+num_pattern+',Roll\='+num_pattern+'\)')          #rotator
#transfrom
tra_pattern=re.compile('\(Rotation\=\(X\='+num_pattern+',Y\='+num_pattern+',Z\='+num_pattern+',W\='+num_pattern+'\),Translation\=\(X\='+num_pattern+',Y\='+num_pattern+',Z\='+num_pattern+'\),Scale3D\=\(X\='+num_pattern+',Y\='+num_pattern+',Z\='+num_pattern+'\)\)')


pattern_list=[
{'int32':int32_pattern},
{'float':float_pattern},
{'bool':bool_pattern},
{'FVector':vec3_pattern},
{'FVector2D':vec2_pattern},
{'FRotator':rot_pattern},
{'FTransform':tra_pattern}
]


num='(true,false)'
# num='true'





pattern=re.compile(bool_pattern)

result1=re.search(pattern,num)
result2=re.match(pattern,num)

v=''
m= re.sub(pattern,v,num,0)

print(result1)
print(m)
print(result2)


# def GetType(str):
#     for pattern in pattern_list:
#         m=re.search(pattern[1],str)



# def GetType