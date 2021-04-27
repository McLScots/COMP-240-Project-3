### Stage 1

import os


def stage1():
    path = 'fail2banlogs'
    for filename in os.listdir(path):
        print(filename)
        file = open(path+'/'+filename,'r')
        lines = file.readlines()
        print(lines[1])
        


if __name__ == "__main__":
    stage1()
