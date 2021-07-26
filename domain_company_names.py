import time
import os 
import csv
import subprocess

word_list = csv.reader('permutation_words.csv')
pay_word = []
brand_word = []
with open('permutation_words.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(row)
        if row[1] == 'p':
            pay_word.append(row[0])
        else:
            brand_word.append(row[0])
master_list = []
for x in pay_word:
    for y in brand_word:
        master_list.append(x+y)
        master_list.append(y+x)

print(master_list)
for name in master_list:
    time.sleep(0.3)
    res = subprocess.check_output('whois ' +name+'.com', shell=True)
    if b'No match for domain' in res:
        print(name+'.com')
    
