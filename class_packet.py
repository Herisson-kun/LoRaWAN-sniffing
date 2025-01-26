class Packet():
    def __init__(self, Mtype, Major, DevAddr, FCtrl, FCnt, FOpts, FPort, FRMPayload, MIC):
        self.Mtype = Mtype
        self.Major = Major
        self.DevAddr = DevAddr
        self.FCtrl = FCtrl
        self.FCnt = FCnt
        self.FOpts = FOpts
        self.FPort = FPort
        self.FRMPayload = FRMPayload
        self.MIC = MIC
    
    def __str__(self):
        return f'Mtype: {self.Mtype}, Major: {self.Major}, DevAddr: {self.DevAddr}, FCtrl: {self.FCtrl}, FCnt: {self.FCnt}, FPort: {self.FPort}, FRMPayload: {self.FRMPayload}, MIC: {self.MIC}'
    
    def __repr__(self):
        return f'Mtype: {self.Mtype}, Major: {self.Major}, DevAddr: {self.DevAddr}, FCtrl: {self.FCtrl}, FCnt: {self.FCnt}, FPort: {self.FPort}, FRMPayload: {self.FRMPayload}, MIC: {self.MIC}'