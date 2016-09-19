from zio import *
serial_num = [1] * 10

serial_num = [2, 147, 131, 172, 192, 224, 169, 63, 253, 64]

def sub_40834B(val):
	result = ((((val ^ 0x7892) + 0x4D30) ^ 0x3421)&0xffff) / 11;
	result2 = ((((val ^ 0x7892) + 0x4D30) ^ 0x3421)&0xffff) % 11;

	if result2 != 0:
		result = 0
	return result

def sub_40A3EE(a1, a2):
	v2 = (((a2 ^ a1 ^ 0x22C078) - 0x2C175) ^ 0xFFE53167) & 0xFFFFFF
	result2 = v2 % 0x11
	if result2 != 0:
		result = 0
	else:
		result = v2 / 0x11
	return result

#v12 = BitVec("v12" 8)
v12 = (serial_num[7]^serial_num[1]) << 8
v13 = serial_num[5] ^ serial_num[2]

print hex(v12 + v13)
v14 = sub_40834B(v13 + v12)

print v14

v15 = sub_40A3EE((serial_num[6]^serial_num[0])+(((serial_num[8]^serial_num[4]) + ((serial_num[5] ^ serial_num[9]) << 8)) << 8), 0x5b8c27)
print hex(v15)
#0x33fef3a9
#buff = l32(0x33fef3a9)
#s.add(v15 >= 0x12345678)

#s.add(v14 == 1000)
"""
s.add(serial_num[4] == ord(buff[0]))
s.add(serial_num[5] == ord(buff[1]))
s.add(serial_num[6] == ord(buff[2]))
s.add(serial_num[7] == ord(buff[3]))
"""
