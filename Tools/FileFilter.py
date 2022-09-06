import os
path = r'F:\音频轨'  # r为raw，作用就是将\不作为转义字符而单纯做一个‘\’
# os.walk()用于输出当前文件夹下所有内容
# root为当前根目录 dirs为向前目录下的文件夹名 files为当前目录下的所有文件
for root, dirs, files in os.walk(path):
    for i in files:
        # 将文件名分开为前后缀
        file_pre = os.path.splitext(i)
        # 将文件前缀赋给front,将文件后缀赋给end
        front, end = file_pre
        if end != '.mp3':
            file_name = os.path.join(root, i)
            print(file_name)
