import unittest
from unittest.mock import patch, MagicMock
from src.client_mode import SOCKETS, ClientDialogBox


class TestClientDialogBox(unittest.TestCase):
    @patch("src.client_mode.SOCKETS")
    @patch("src.client_mode.ask_ip.ask_ip_dialog")
    def test_socket_connection_and_dialog(self, mock_ask_ip_dialog, mock_sockets):
        # Mock user input for IP address and port
        mock_ask_ip_dialog.return_value = ("127.0.0.1", 5000)

        # Mock SOCKETS instance
        mock_socket_instance = MagicMock()
        mock_sockets.return_value = mock_socket_instance

        # Initialize ClientDialogBox
        app = ClientDialogBox()
        app.ip_address.set("127.0.0.1")
        app.port.set(5000)

        # Simulate sending a text message
        app.Sending_data.insert("1.0", "Hello, World!")
        app.send_text_message()

        # Ensure the message was added to the chat history
        self.assertIn("Hello, World!", app.history.get("1.0", "end"))

        # Ensure SOCKETS methods were called as expected
        mock_sockets.assert_called_once()
        mock_socket_instance.connect.assert_called_once_with(("127.0.0.1", 5000))
        mock_socket_instance.send.assert_called_once_with("Hello, World!")


if __name__ == "__main__":
    unittest.main()
