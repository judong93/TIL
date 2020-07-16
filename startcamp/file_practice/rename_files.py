#1.os를 import 한다.
import os

#2.작업하고자 하는 폴더로 들어간다.
os.chdir(r'C:\Users\aclass\Desktop\박주동\file_practice\dummy')

#3. 폴더에 있는 파일들을 가져온다.
filenames = os.listdir('.')


#4. 파일들을 반복하면서 파일명을 바꾼다.
for filename in filenames:
    os.rename(filename, f'SAMSUNG_{filename}')
print(filenames)
