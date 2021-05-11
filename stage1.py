### Stage 1

import os
import csv
import re

# gets desired date ip pairs from logs and write to csv
def stage1():
    output = open('stage1_output.csv','w',newline='')
    csv_writer = csv.writer(output,delimiter=',',escapechar=' ',quoting=csv.QUOTE_NONE)
    path = 'fail2banlogs'
    # loop through all fail2ban logs in the log directory
    for filename in os.listdir(path):
        file = open(path+'/'+filename,'r').read()
        for line in re.findall(".*fail2ban.actions.*NOTICE.* Ban .*",file):
            date = re.split(",",line)[0]
            ip = re.split('\s',line).pop()
            csv_writer.writerow([date,ip])
    output.close()


if __name__ == "__main__":
    stage1()
