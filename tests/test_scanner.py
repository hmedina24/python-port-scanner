import unittest
import socket
import threading
from scanner import scan_port, parse_ports
from utils.common_ports import resolve_service


class TestPortScanner(unittest.TestCase):

    def test_valid_open_port(self):
        def run_server():
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("127.0.0.1", 9999))
            server.listen(1)
            conn, _ = server.accept()
            conn.close()
            server.close()

        thread = threading.Thread(target=run_server, daemon=True)
        thread.start()

        status = scan_port("127.0.0.1", 9999)
        self.assertEqual(status, "open")

    def test_invalid_port(self):
        with self.assertRaises(ValueError):
            scan_port("127.0.0.1", -1)

    def test_service_resolution(self):
        self.assertEqual(resolve_service(80), "HTTP")
        self.assertEqual(resolve_service(9999), "Unknown")

    def test_valid_ip_address(self):
        status = scan_port("127.0.0.1", 80)
        self.assertIn(status, ["open", "closed"])

    def test_invalid_ip_valid_port(self):
        with self.assertRaises(ValueError):
            scan_port("256.256.256.256", 80)

    def test_valid_hostname(self):
        status = scan_port("localhost", 80)
        self.assertIn(status, ["open", "closed"])

    def test_invalid_hostname_valid_port(self):
        with self.assertRaises(ValueError):
            scan_port("invalid_host_name$$$", 443)

    def test_parse_ports_specific(self):
        ports = parse_ports("22,80,443")
        self.assertEqual(ports, [22,80,443])

    def test_parse_ports_invalid(self):
        with self.assertRaises(ValueError):
            parse_ports("70000")

    def test_parse_ports_defaults(self):
        ports = parse_ports(None)
        self.assertGreater(len(ports), 0)

if __name__ == "__main__":
    unittest.main()

