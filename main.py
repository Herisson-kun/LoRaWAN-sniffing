import csv
from utils.utils import decrypt
import os
import datetime


packets = []
counter_good = 0
counter_bad = 0
# Ouvrir le fichier CSV
with open('csv/lorawan_capture.csv', mode='r') as file:
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
        try:
            packet = decrypt(time, data, rssi, snr)
            if packet == "Error":
                counter_bad+=1
            elif rssi > 30:
                counter_bad+=1 
            else:
                packets.append(packet)
                counter_good+=1
        except:
            print("Error")        

for packet in packets:
    print(packet)
    print()
    # Create the capture directory if it doesn't exist
    capture_dir = 'csv/capture'
    os.makedirs(capture_dir, exist_ok=True)

    # Generate a unique filename based on the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'processed_packets_{timestamp}.csv'
    filepath = os.path.join(capture_dir, filename)

    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Écrire l'en-tête
        writer.writerow(['Time', 'Mtype', 'Major', 'DevAddr', 'FCtrl', 'FCnt', 'FOpts', 'FPort', 'FRMPayload', 'MIC', 'RSSI', 'SNR'])
        
        for packet in packets:
            writer.writerow([
                packet.Time,
                packet.Mtype,
                packet.Major,
                packet.DevAddr,
                packet.FCtrl,
                packet.FCnt,
                packet.FOpts,
                packet.FPort,
                packet.FRMPayload,
                packet.MIC,
                packet.RSSI,
                packet.SNR
            ])
print("Bad Packets : ", counter_bad)
print("Good Packets : ", counter_good)
print("ratio : ", counter_good/(counter_good+counter_bad)*100, "%")
