from z3 import *
from zio import *
import commands

serial_num = []

def do_command(cmd_line):
	(status, output) = commands.getstatusoutput(cmd_line)
	return output

for i in range(10):
	serial_num.append(BitVec("serial_num_%d"%i, 32))

v12 = BitVec("v12", 16)
v13 = BitVec("v13", 16)

def sub_40834B(val):
	result = ((((val ^ 0x7892) + 0x4D30) ^ 0x3421)&0xffff) / 11;
	result2 = ((((val ^ 0x7892) + 0x4D30) ^ 0x3421)&0xffff) % 11;

	result = If(result2 != 0, 0, result)
	return result

def sub_40A3EE(a1, a2):
	v2 = (((a2 ^ a1 ^ 0x22C078) - 0x2C175) ^ 0xFFE53167) & 0xFFFFFF
	result2 = v2 % 0x11
	result = If(result2 != 0, 0, v2 / 0x11)
	return result

s = Solver()
for i in range(10):
	s.add(serial_num[i] < 0x100)
	s.add(serial_num[i] >= 0)

s.add(serial_num[3] == 0xAC)
v12 = (serial_num[7]^serial_num[1])
v12 = v12 << 8
v13 = serial_num[5] ^ serial_num[2]

v14 = sub_40834B(v13 + v12)
s.add(v14 != 0)
s.add(v14 <= 1000)
s.add(v14 > 0)

#print v14
v15 = sub_40A3EE((serial_num[6]^serial_num[0])+(((serial_num[8]^serial_num[4]) + ((serial_num[5] ^ serial_num[9]) << 8)) << 8), 0x5b8c27)

#0x3fa9e0c0

date_time = 0x30798
date_time = 0x30798+10
times = 512
times = 512+10
name_info = raw_input("name:")
outbuff = do_command("./gen_name_data %s %d %d"%(name_info, date_time, times)).strip()

name_val = int(outbuff, 16)

buff = l32(name_val)
s.add(v15 >= 0x10000)
s.append(v15 == date_time)

s.add(v14 == times)
#"""
s.add(serial_num[4] == ord(buff[0]))
s.add(serial_num[5] == ord(buff[1]))
s.add(serial_num[6] == ord(buff[2]))
s.add(serial_num[7] == ord(buff[3]))
#"""
serial_num_val = []
if s.check() == sat:
	for i in range(10):
		serial_num_val.append(s.model()[serial_num[i]].as_long())

	#print serial_num_val
	print "serial_num:", 
	print "".join(["%02x"%(c) for c in serial_num_val])