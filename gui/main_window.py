import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit
from scanner import NetworkScanner
from vulnerability import VulnerabilityScanner

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Advanced Network Scanner Tool')
        self.initUI()
        self.network_scanner = NetworkScanner('192.168.1.1/24')  # Example IP range
        self.vuln_scanner = VulnerabilityScanner()

    def initUI(self):
        # Main layout
        layout = QVBoxLayout()

        # Scan buttons
        self.scan_network_button = QPushButton('Scan Network')
        self.scan_network_button.clicked.connect(self.scan_network)
        layout.addWidget(self.scan_network_button)

        self.scan_vulnerabilities_button = QPushButton('Scan for Vulnerabilities')
        self.scan_vulnerabilities_button.clicked.connect(self.scan_vulnerabilities)
        layout.addWidget(self.scan_vulnerabilities_button)

        # Text area for displaying scan results
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        layout.addWidget(self.results_text)

        # Setting the layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def scan_network(self):
        self.results_text.append("Starting network scan...")
        self.network_scanner.result_signal.connect(self.display_scan_results)
        self.network_scanner.start()

    def scan_vulnerabilities(self):
        self.results_text.append("Scanning for vulnerabilities...")
        self.vuln_scanner.finished.connect(self.display_vulnerabilities)
        self.vuln_scanner.run_scan('192.168.1.1')  # Example IP

    def display_scan_results(self, results):
        self.results_text.append("Network scan completed.")
        for device in results:
            self.results_text.append(f"IP: {device['ip']}, MAC: {device['mac']}")

    def display_vulnerabilities(self, results):
        self.results_text.append("Vulnerability scan completed.")
        for item in results:
            self.results_text.append(f"IP: {item['ip']}, Vulnerabilities: {item['vulnerabilities']}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
