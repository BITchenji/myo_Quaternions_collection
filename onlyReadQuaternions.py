# -*- coding: utf-8 -*-
"""

@author: Chen Ji
"""
from __future__ import print_function
import serial
import numpy as np

QuaternionsData = [ ]


comunicacaoSerial0 = serial.Serial('/dev/ttyUSB0', 115200)
comunicacaoSerial1 = serial.Serial('/dev/ttyUSB1', 115200)


MYO_Data0 = comunicacaoSerial0.readline()
MYO_Data1 = comunicacaoSerial1.readline()

myo_data0 = np.fromstring(MYO_Data0, dtype=float, sep=' ')
print(myo_data0)   #01010101 表示成功连接MYO
myo_data1 = np.fromstring(MYO_Data1, dtype=float, sep=' ')
print(myo_data1)   #01010101

i = int(0)

while(1):

	MYO_Data0 = comunicacaoSerial0.readline()
	MYO_Data1 = comunicacaoSerial1.readline()

	myo_data0 = np.fromstring(MYO_Data0, dtype=float, sep=' ')
	myo_data1 = np.fromstring(MYO_Data1, dtype=float, sep=' ')

	quaternion0 = list(myo_data0)
	quaternion1 = list(myo_data1)    #把ndarray转换为list

	quaternion3 = quaternion0 + quaternion1

	quaternion = [round(i, 2) for i in quaternion3]  #把quaternion化为小数点后两位小数

	QuaternionsData.append(quaternion)

	i =  len(QuaternionsData) - 1
	
	#print(QuaternionsData[i])

	strQuaternionData = ' '.join('%s' %id for id in QuaternionsData[i])   #把QuaternionsData[i]转换为字符串
	
	q = open('/home/chenji/Desktop/Quaternions.m','a')
	q.write(strQuaternionData + '\n')
	q.close()

	i = i + 1



