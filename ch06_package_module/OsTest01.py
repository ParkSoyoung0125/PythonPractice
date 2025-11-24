save_path = input('생성할 폴더 이름 입력 : ')

import os

# if not os.path.isdir(save_path): # 폴더가 존재하지 않는 경우
#     os.mkdir(save_path)
# else :
#     print(f'{save_path} 폴더는 존재합니다.')
#end if

# 특정 다이렉토리에 하위 디렉토리 여러 개 생성하기
targetFolder = 'd:\\' # \는 특수문자라서 \\라고 표시해야함
parentPath = os.path.join(targetFolder, 'sample')

print(parentPath)

try:
    os.mkdir(parentPath)

    # 반복문을 사용하여, 하위폴더 10개를 만들어주
    for idx in range(1,11):
        newFolder = os.path.join(parentPath,'folder'+ str(idx).zfill(2)) # zfill(n) : n자리까지 0 채우기
        # print(newFolder)
        os.mkdir(newFolder)

except FileExistsError:
    print('해당 다이렉토리가 이미 존재합니다.')
#end try