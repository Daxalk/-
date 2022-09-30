import os
root_direction = os.path.abspath(r'D:\test\123')
os.chmod(root_direction, os.X_OK)
previous = ''
tmp = str(root_direction).split('\\')

for folders in range(len(tmp)-1):
    previous += tmp[folders] + '\\'
os.chmod(previous, 000)