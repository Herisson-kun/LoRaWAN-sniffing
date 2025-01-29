class Packet():
    def __init__(self, Time, Mtype, Major, DevAddr, FCtrl, FCnt, FOpts, FPort, FRMPayload, MIC, RSSI, SNR):
        self.Time = Time
        self.Mtype = Mtype
        self.Major = Major
        self.DevAddr = DevAddr
        self.FCtrl = FCtrl
        self.FCnt = FCnt
        self.FOpts = FOpts
        self.FPort = FPort
        self.FRMPayload = FRMPayload
        self.MIC = MIC
        self.RSSI = RSSI
        self.SNR = SNR
        
    
    def __str__(self):
        return (
            f"Packet Details:\n"
            f"Time        : {self.Time}\n"
            f"Mtype       : {self.Mtype}\n"
            f"Major       : {self.Major}\n"
            f"DevAddr     : {self.DevAddr}\n"
            f"FCtrl       : {self.FCtrl}\n"
            f"FCnt        : {self.FCnt}\n"
            f"FOpts       : {self.FOpts}\n"
            f"FPort       : {self.FPort}\n"
            f"FRMPayload  : {self.FRMPayload}\n"
            f"MIC         : {self.MIC}\n"
            f"RSSI        : {self.RSSI}\n"
            f"SNR         : {self.SNR}"
        )

    def __repr__(self):
        return (
            f"Packet(Time={self.Time}, Mtype={self.Mtype}, Major={self.Major}, "
            f"DevAddr={self.DevAddr}, FCtrl={self.FCtrl}, FCnt={self.FCnt}, "
            f"FOpts={self.FOpts}, FPort={self.FPort}, FRMPayload={self.FRMPayload}, "
            f"MIC={self.MIC}, RSSI={self.RSSI}, SNR={self.SNR})"
        )

