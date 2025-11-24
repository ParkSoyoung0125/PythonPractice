# os 모듈을 사용하여 d 드라이브에 exercise 디렉토리를 생성하세요
# 그리고, exercise 디렉토리 아래에 다음 항목들에 대한 디렉토리를 생성해 보세요

import os

targetFolder = 'd:\\'
parentPath = os.path.join(targetFolder,'exercise')
print(parentPath)

try:
    os.mkdir(parentPath)
    exercise = ['alpha', 'bravo', 'delta', 'nova', 'terra', 'pixel', 'orbit', 'matrix', 'spark', 'fusion']

    for i in exercise:
        newFolder = os.path.join(parentPath,str(i))
        os.mkdir(newFolder)

except FileExistsError:
    print('이미 존재하는 디렉토리입니다.')