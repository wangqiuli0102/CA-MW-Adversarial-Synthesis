'''
provided by LUNA16
csv script

Modified by Wei Chen(wchen@cqu.edu.cn), Qiuli Wang(wangqiuli@cqu.edu.cn)
7/12/2020

wchen@cqu.edu.cn
'''

import csv
import platform

def writeTXT(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line+'\n')

def writeCSV(filename, lines):
    if 'Darwin' in platform.system():
        with open(filename, "wb") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(lines)
    else:
        with open(filename, "w", newline='') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerows(lines)

def readCSV(filename):
    lines = []
    with open(filename, "r") as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            lines.append(line)
    return lines

def tryFloat(value):
    try:
        value = float(value)
    except:
        value = value
    
    return value

def getColumn(lines, columnid, elementType=''):
    column = []
    for line in lines:
        try:
            value = line[columnid]
        except:
            continue
            
        if elementType == 'float':
            value = tryFloat(value)

        column.append(value)
    return column
