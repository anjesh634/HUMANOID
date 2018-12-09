import serial
import crcmod
import struct

serial_port = serial.Serial('/dev/ttyUSB0', baudrate=57600, timeout=0.05)

packet_id = 1
packet_length = 3
instruction = 1
packet = bytearray([0xff, 0xff, 0xfd, 0x00, packet_id, packet_length, 0, instruction])

crc_fun = crcmod.mkCrcFun(0x18005, initCrc=0, rev=False)
crc = crc_fun(bytes(packet))

packet.extend(struct.pack('<H', crc))

print('Packet: ' + ":".join("{:08b}".format(c) for c in packet))
print('Packet: ' + ":".join("{:02x}".format(c) for c in packet))

serial_port.write(packet)

header = serial_port.read(3)
print('Received header: ' + ":".join("{:02x}".format(ord(c)) for c in header))

body = serial_port.read(4)
print('Received body: ' + ":".join("{:02x}".format(ord(c)) for c in body))
