import unittest
from unittest.mock import MagicMock, patch
from src.server_mode import SOCKETS  # Adjust import path as necessary


class TestSOCKETS(unittest.TestCase):
    def setUp(self):
        self.sockets = SOCKETS()
        self.sockets.conn = MagicMock()

    def tearDown(self):
        # Simulate closing the mock socket connection
        self.sockets.conn.close()

    @patch("src.server_mode.socket.socket")
    def test_send(self, mock_socket):
        # Mock socket connection
        self.sockets.conn.sendall = MagicMock()

        # Test data
        test_data = "Hello, World!"

        # Attempt to send data
        self.sockets.send(test_data)

        # Check if sendall was called with the correct data
        self.sockets.conn.sendall.assert_called_with(test_data.encode("utf-8"))


if __name__ == "__main__":
    unittest.main()
