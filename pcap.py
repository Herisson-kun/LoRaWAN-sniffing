from class_packet import Packet
from scapy.all import wrpcap,Ether
import os


list_packets = []

'''
Code de lecture 
'''

# Création d'une trame LoRaWAN
list_packets = [
    Packet(0x40, 0x00, 0xA1B2C3D4, 0x00, 0x0001, b"", 0x01, b"\x03\x04\x05\x06", 0x12345678),
    Packet(0x40, 0x00, 0xA1B2C3D5, 0x00, 0x0002, b"", 0x01, b"\x07\x08\x09\x0A", 0x87654321),
    Packet(0x40, 0x00, 0xA1B2C3D6, 0x00, 0x0003, b"", 0x01, b"\x0B\x0C\x0D\x0E", 0xAABBCCDD),
]


'''
Fin de la lecture des packets
'''

# Conversion en paquet Scapy
scapy_packets = [Ether() for p in list_packets]

output_file = './log_pcap/output.pcap'

# Check if the output file already exists
if os.path.exists(output_file):
    # If it exists, create a new file name by appending a number to the file name
    file_name, file_extension = os.path.splitext(output_file)
    i = 1
    while os.path.exists(f"{file_name}_{i}{file_extension}"):
        i += 1
    output_file = f"{file_name}_{i}{file_extension}"

# Write the packets to the PCAP file
wrpcap(output_file, scapy_packets, linktype=270)
