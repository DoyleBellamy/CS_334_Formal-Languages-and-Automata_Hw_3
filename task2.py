#UMUT OZDEMIR HW3 211101004

import re
import sys

date = sys.argv[1]
duration = sys.argv[2]
resource = sys.argv[3]

f = open('clean_log.txt', 'r')
f2 = open('output_task2.txt', 'w')
patternForDate = re.compile(r'(\d+)(/)(\w+)(/)(\d+)(:)(\d\d)(:)(\d\d)(:)(\d\d)')
eslesme = patternForDate.finditer(date)
gelme_zamani = 0
ay = 0

for match in eslesme:
    if match.group(3) == "Jan":
        ay = 1
    elif match.group(3) == "Feb":
        ay = 2
    elif match.group(3) == "Mar":
        ay = 3
    elif match.group(3) == "Apr":
        ay = 4
    elif match.group(3) == "May":
        ay = 5
    elif match.group(3) == "Jun":
        ay = 6
    elif match.group(3) == "Jul":
        ay = 7
    elif match.group(3) == "Aug":
        ay = 8
    elif match.group(3) == "Sep":
        ay = 9
    elif match.group(3) == "Oct":
        ay = 10
    elif match.group(3) == "Nov":
        ay = 11
    elif match.group(3) == "Dec":
        ay = 12
    gelme_zamani = int(match.group(1))*86400+ay*2628288+(int(match.group(5))-1970)*31536000+int(match.group(7))*3600+int(match.group(9))*60+int(match.group(11))
    # print(gelme_zamani)

pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)( - - \[)(\d+)(/)(\w+)(/)(\d+)(:)(\d\d)(:)(\d\d)(:)(\d\d)(.{9})'+"GET "+re.escape(resource)+r'(.+?)')

#Veri tutulan yer
access_time = []
access_time_FORMED = []
idler = []
idlerin_gecme_sayisi = []


while True:
    line = f.readline()
    if not line:
        break
    matches = pattern.finditer(line)
    yeniIp = ""
    temp_access = 0
    temp_access_FORMED = ""
    ay=0
    for match in matches:
        # print(match.group(0))
        yeniIp = match.group(1)
        temp_access_FORMED = pattern.sub(r'\3\4\5\6\7\8\9\10\11\12\13', str(match.group(0)))
        # print(temp_access_FORMED)
        # print(yeniIp)
        if match.group(5) == "Jan": ay = 1
        elif match.group(5) == "Feb": ay = 2
        elif match.group(5) == "Mar": ay = 3
        elif match.group(5) == "Apr": ay = 4
        elif match.group(5) == "May": ay = 5
        elif match.group(5) == "Jun": ay = 6
        elif match.group(5) == "Jul": ay = 7
        elif match.group(5) == "Aug": ay = 8
        elif match.group(5) == "Sep": ay = 9
        elif match.group(5) == "Oct": ay = 10
        elif match.group(5) == "Nov": ay = 11
        elif match.group(5) == "Dec": ay = 12
        temp_access = int(match.group(3))*86400+ay*2628288+(int(match.group(7))-1970)*31536000+int(match.group(9))*3600+int(match.group(11))*60+int(match.group(13))
    if int(temp_access)-int(duration) >= int(gelme_zamani):
        continue
    if int(temp_access)-int(gelme_zamani)<0:
        continue
    if yeniIp in idler:
        k = idler.index(yeniIp)
        idlerin_gecme_sayisi[k] += 1
    else :
        idler.append(yeniIp)
        idlerin_gecme_sayisi.append(1)
        access_time.append(temp_access)
        access_time_FORMED.append(temp_access_FORMED)
i = 0
while i < len(idler):
    temp = -1
    o = 0
    big_index = 0
    while o < len(idler):
        if temp < idlerin_gecme_sayisi[o]:
            big_index = o
            temp = idlerin_gecme_sayisi[o]
        o += 1
    f2.write(str(idler[big_index])+" "+str(idlerin_gecme_sayisi[big_index])+" "+str(access_time[big_index])+" -> AccessTime("+access_time_FORMED[big_index]+")\n")
    idlerin_gecme_sayisi[big_index] = -1
    i += 1