import csv
from utils import decrypt


packets = []

# Ouvrir le fichier CSV
with open('csv/packet_capture.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Passer l'en-tête
    
    for row in reader:
        # Extraire les informations de chaque ligne
        time = row[0]  # Première colonne (temps)
        rawpacket = row[1]  # Deuxième colonne (paquet brut en hexadécimal)
        rssi = float(row[2])  # Troisième colonne (RSSI, converti en flottant)
        snr = float(row[3])  # Quatrième colonne (SNR, converti en flottant)

        # Convertir le rawpacket (en hexadécimal) en une liste de bytes
        rawpacket_split = rawpacket.split()
        data = [x for x in rawpacket_split]

        # Appeler la fonction decrypt pour obtenir un objet Packet
        packet = decrypt(time, data, rssi, snr)
        
        # Ajouter l'objet Packet à la liste
        packets.append(packet)

print(packets)