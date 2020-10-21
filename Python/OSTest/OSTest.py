import os
import shutil



path='Part04'

# os.makedirs(path)

# os.renames('Part04','Part04_01')


source='C:/Users/lostm/Desktop/PythonTest/OSTest/Part01/Part02/Part03'
destination='C:/Users/lostm/Desktop/PythonTest/OSTest/Part01/Part03'


shutil.copytree(source,destination)
