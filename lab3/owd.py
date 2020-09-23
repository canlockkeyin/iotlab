from decimal import *

getcontext().prec = 10

f1 = open("sequence_numbers_udpwlan_modified.log", "r")
f2 = open("sequence_numbers_piwlanudp_modified.log", "r")

lines1 = f1.readlines()
f1.close()

lines2 = f2.readlines()
f2.close()

packet_dict = {}

for line in lines2:
    split = line.split(" ")
    time = split[0]
    num = split[1]
    num = num[0:len(num)-1]
    packet_dict[num] = Decimal(time)

lasttime = sorted(packet_dict.values())[-1] 
firsttime = sorted(packet_dict.values())[0]
timediff = Decimal(lasttime) - Decimal(firsttime)

totalsize = Decimal(sorted(packet_dict.keys())[-1])

print(totalsize, timediff)

print("Bitrate", totalsize/timediff)

delay_dict = {}

for line in lines1:
    split = line.split(" ")
    time = split[0]
    num = split[1]
    num = num[0:len(num)-1]
    if num in packet_dict.keys():
        delay_dict[num] = abs(packet_dict[num] - Decimal(time))
        #print(num, delay_dict[num])

n = len(delay_dict)
avg = sum(delay_dict.values()) / n
var = sum([((abs(x) - avg) ** 2) for x in delay_dict.values()]) / n
print("Werte:", n)
print("Mittelwert (us):", avg * Decimal(1)) #1e6
print("Standardabweichung (us):", var ** Decimal(0.5) * Decimal(1))