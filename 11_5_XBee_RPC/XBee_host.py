import serial
import time

# XBee setting
serdev = '/dev/ttyUSB2'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())

s.write("ATMY 0x116\r\n".encode())
char = s.read(3)
print("Set MY 0x116.")
print(char.decode())

s.write("ATDL 0x216\r\n".encode())
char = s.read(3)
print("Set DL 0x216.")
print(char.decode())

s.write("ATID 0x1\r\n".encode())
char = s.read(3)
print("Set PAN ID 0x1.")
print(char.decode())

s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())

s.write("ATMY\r\n".encode())
char = s.read(4)
print("MY :")
print(char.decode())

s.write("ATDL\r\n".encode())
char = s.read(4)
print("DL : ")
print(char.decode())

s.write("ATCN\r\n".encode())
char = s.read(3)
print("Exit AT mode.")
print(char.decode())

print("start sending RPC")
time.sleep(1)
while True:
    s.write("/Acc/run\n\r".encode())
    time.sleep(1)

    #s.write("/myled1/write 1\r".encode())
    #time.sleep(1)

    #s.write("/myled2/write 1\r".encode())
    #time.sleep(1)

    #s.write("/myled3/write 1\r".encode())
    #time.sleep(1)

    #s.write("/myled3/write 0\r".encode())
    #time.sleep(1)

    #s.write("/myled2/write 0\r".encode())
    #time.sleep(1)

    #s.write("/myled1/write 0\r".encode())
    #time.sleep(1)
    
    #char = s.read(18)
    #print(char.decode())
    #time.sleep(2)
s.close()