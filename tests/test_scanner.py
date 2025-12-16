import unittest
import socket
import threading
from scanner import scan_port
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

    def test_invalid_hostname(self):
        with self.assertRaises(ValueError):
            scan_port("not_a_real_host_123", 80)

    def test_invalid_hostname_valid_port(self):
        with self.assertRaises(ValueError):
            scan_port("invalid_host_name$$$", 443)

if __name__ == "__main__":
    unittest.main()

