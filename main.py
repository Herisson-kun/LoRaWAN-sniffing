import csv
from utils import decrypt


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

print("Bad Packets : ", counter_bad)
print("Good Packets : ", counter_good)
print("ratio : ", counter_good/(counter_good+counter_bad)*100, "%")
