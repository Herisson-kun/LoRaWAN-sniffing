"""
LoRaWAN Sniffer
Author: Johan Bartosik, Vincent Fromont and Farah Ourir
"""
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
import csv  
import adafruit_rfm9x
import os

# Configure RFM9x LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Crée le fichier CSV et ajoute l'en-tête
csv_filename = "lorawan_capture.csv"
if not os.path.exists(csv_filename):
    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Packet (Hexadecimal)", "RSSI", "SNR"])  # En-têtes des colonnes

# Turn on RFM9X
try:
    rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 868.1)
    rfm9x.signal_bandwidth = 125000
    rfm9x.coding_rate = 5
    rfm9x.spreading_factor = 7
    print("Module Ready")
except RuntimeError as error:
    print('RFM9x Error: ', error)
    
# Listening
while True:
    time.sleep(0.1)
    packet = rfm9x.receive(with_header=True, timeout=5)
    # If no packet was received during the timeout then None is returned.
    print("listening")
    print(packet)
    if packet is not None:
        # Received a packet!
        # Print out the raw bytes of the packet:
        received_time = time.strftime("%d-%m-%Y %H:%M:%S")
        packet_hexa = [hex(x) for x in packet]
        rssi = rfm9x.last_rssi
        snr = rfm9x.last_snr
        print("Received:", packet_hexa)
        print("RSSI: {0}".format(rssi))
        print("SNR : {0}".format(snr))
        print("time : ", received_time)
        
        # Écrire dans le fichier CSV
        if any(x != "0x00" for x in packet_hexa):
            with open(csv_filename, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([received_time, " ".join(packet_hexa), rssi, snr])
        
    


