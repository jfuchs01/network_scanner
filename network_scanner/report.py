import datetime

class ReportGenerator:
    """
    ReportGenerator creates a report from the scan results.
    """
    
    def __init__(self, scan_data):
        """
        Initializes the ReportGenerator with the provided scan data.
        :param scan_data: The data obtained from the network scan.
        """
        self.scan_data = scan_data

    def generate_text_report(self):
        """
        Generates a text report from the scan data.
        """
        report_lines = ["Network Scan Report", f"Generated on {datetime.datetime.now()}", "-"*50]

        for device in self.scan_data:
            ip = device.get('ip', 'N/A')
            mac = device.get('mac', 'N/A')
            report_lines.append(f"IP Address: {ip}\nMAC Address: {mac}\n")
            if 'vulnerabilities' in device:
                report_lines.append("Vulnerabilities:")
                for vuln in device['vulnerabilities']:
                    report_lines.append(f" - {vuln}")
            report_lines.append("-"*50)

        return "\n".join(report_lines)

    def save_report_to_file(self, filename="network_scan_report.txt"):
        """
        Saves the generated report to a text file.
        :param filename: The name of the file to save the report to.
        """
        report_content = self.generate_text_report()
        with open(filename, 'w') as file:
            file.write(report_content)
        print(f"Report saved to {filename}")

    def print_report(self):
        """
        Prints the report to the console.
        """
        report_content = self.generate_text_report()
        print(report_content)
