#UMUT OZDEMIR HW3 211101004

import re
pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)( - - \[)(\d+)(/)(\w+)(/)(\d+)(:)(.+)')

f = open('web_log.txt', 'r')
k = open('output_task1.txt' , 'w')
while True:
    line=f.readline()
    eslesme=pattern.sub(r'\1 \3-\5-\7',line)
    if not line:
        break
    k.write(eslesme)
