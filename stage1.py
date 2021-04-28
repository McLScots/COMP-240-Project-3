### Stage 1

import os
import csv

# gets desired date ip pairs from logs and write to csv
def stage1():
    output = open('stage1_output.csv','w',newline='')
    csv_writer = csv.writer(output,delimiter=',',escapechar=' ',quoting=csv.QUOTE_NONE)
    path = 'fail2banlogs'
    # loop through all fail2ban logs in the log directory
    for filename in os.listdir(path):
        print(filename)
        file = open(path+'/'+filename,'r')
        lines = file.readlines()
        for line in lines:
            if line_check(line):
                csv_writer.writerow([get_date(line),get_ip(line)])
        file.close()
    output.close()
                
# checks if a line in the fail2ban log is of interest            
def line_check(line):
    if 'fail2ban.actions' in line and 'NOTICE' in line:
        return True

# extracts the date from line in fail2ban log
def get_date(line):
    date = ''
    # loop through string until we see a comma
    for char in line:
        if char != ',':
            date += char
        else:
            break
    return date

# extracts the ip from line in fail2ban log
def get_ip(line):
    ip = ''
    # loop through string in reverse until we see a space
    for i in range(len(line)-1,-1,-1):
        char = line[i]
        if char != ' ':
           ip = char + ip
        else:
            break
    return ip


if __name__ == "__main__":
    stage1()
