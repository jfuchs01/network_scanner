import scapy.all as scapy
from PyQt5.QtCore import QThread, pyqtSignal

class NetworkScanner(QThread):
    """
    NetworkScanner inherits from QThread to perform network scanning operations
    in a separate thread, preventing the GUI from freezing.
    """
    # Signal to emit results to the GUI
    result_signal = pyqtSignal(object)

    def __init__(self, ip_range):
        super().__init__()
        self.ip_range = ip_range

    def run(self):
        """
        The main function that runs when the thread starts.
        It performs the network scan and emits the results.
        """
        self.scan_network(self.ip_range)

    def scan_network(self, ip_range):
        """
        Scans the network using ARP requests to discover devices.
        :param ip_range: The IP range to scan, e.g., '192.168.1.1/24'
        """
        arp_request = scapy.ARP(pdst=ip_range)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        devices = []
        for element in answered_list:
            device_info = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
            devices.append(device_info)

        # Emit the results to the GUI
        self.result_signal.emit(devices)
