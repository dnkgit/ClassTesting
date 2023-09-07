from network import WLAN
import machine

class WS_WLAN():

    def __init__(self, debugRequired, wpaPassword):

        self.StaticIP = ''
        self.ssid = ''
        if wpaPassword != '':
            self.wpa2_passwd = wpaPassword
        else:
            self.wpa2_passwd = ''
        self.numberOfReconnections = 0

        self.wlan = WLAN(WLAN.STA)
        self.wlan.init()

        self.doDebug = debugRequired


    def set_StaticIP(self, newStaticIP):
        self.StaticIP = newStaticIP

    def set_SSID(self, newSSID):
        self.ssid = newSSID

    def doConnect(self):

        if not self.wlan.isconnected() :
            nets = self.wlan.scan()
            for net in nets:
                if net.ssid == self.ssid :
                    self.debugPrint(f"Connecting to {self.ssid}")
                    self.wlan.connect(net.ssid, auth=(WLAN.WPA2, self.wpa2_passwd), timeout=5000)
                    while not self.wlan.isconnected():
                        machine.idle()
                    self.debugPrint(f"Connected to {self.ssid}")
                    break

    def isConnectionActive(self):
        return self.wlan.isconnected()

    def get_WifiNetworksScanned(self):
        networks = self.wlan.scan()
        return networks

    def debugPrint(self, debugString):
        if self.doDebug:
            print(debugString)
