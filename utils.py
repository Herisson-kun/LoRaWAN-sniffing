from class_packet import Packet

mtype_dict = {'000': 'Join Request', '001': 'Join Accept', '010': 'Unconfirmed Data Up', 
                  '011': 'Unconfirmed Data Down', '100': 'Confirmed Data Up', 
                  '101': 'Confirmed Data Down', '110': 'Reserved', '111': 'Proprietary'}
    
major_dict = {'00': 'LoRaWAN 1.0.x', '01': 'LoRaWAN 1.1'}

def decrypt(data):
    MHDR = get_MHDR(data[0])
    DevAddr = data[1:5][::-1]
    FCtrl = get_FCtrl(data[5])
    FCnt = get_counter(data[6:8][::-1])
    FOpts = None
    if FCtrl[3] > 0:
        FOpts = data[8:8+FCtrl[3]]
    FPort = int(data[8], 16)
    FRMPayload = data[9:-4]
    MIC = data[-4:]
    return Packet(MHDR[0], MHDR[1], DevAddr, FCtrl, FCnt, FOpts, FPort, FRMPayload, MIC)

def get_MHDR(MHDR_hex):
    MHDR = []
    MHDR_int = int(MHDR_hex, 16)
    MHDR_bin = bin(MHDR_int)[2:]
    Mtype = mtype_dict[MHDR_bin[:3]]
    Major = major_dict[MHDR_bin[6:]]
    MHDR.extend([Mtype, Major])
    return MHDR

def get_FCtrl(FCtrl_hex):
    FCtrl = []
    FCtrl_int = int(FCtrl_hex, 16)
    FCtrl_bin = bin(FCtrl_int)[2:]
    ADR = FCtrl_bin[0]
    ACK = FCtrl_bin[2]
    FPending = FCtrl_bin[3]
    FOptsLen = int(FCtrl_bin[4:], 2)
    FCtrl.extend([ADR, ACK, FPending, FOptsLen])
    return FCtrl

def get_counter(counter_hex):
    int_list = [int(byte, 16) for byte in counter_hex]
    counter = int_list[0] * 256 + int_list[1]
    return counter

def to_hex(data):
    return [hex(x) for x in data]

data_raw = bytearray(b'\x80X\xc9\x0b&\x80&\x00\x02o\xcd0 Y')
data_hex = to_hex(data_raw)
print(data_hex)
packet = decrypt(data_hex)
print(packet)