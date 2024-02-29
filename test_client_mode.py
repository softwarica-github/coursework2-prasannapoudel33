import unittest
from unittest.mock import patch, MagicMock
from src.client_mode import SOCKETS, ClientDialogBox


class TestClientDialogBox(unittest.TestCase):
    def send_text_message(self, app, mock_ask_ip_dialog, mock_sockets):
        if app.status.cget("text") == "Connected":
            input_data = app.Sending_data.get("1.0", "end").strip()  # Strip whitespace
            if input_data:
                app.s.send(input_data.encode("utf-8"))
                input_data = "me: " + input_data
                app.history.config(state="normal")  # Enable editing
                app.history.insert("end", input_data + "\n")  # Add newline
                app.history.config(state="disabled")  # Disable editing
                app.history.see("end")  # Scroll to end
            else:
                print("[=] Input Not Provided")
        else:
            print("[+] Not Connected")

    @patch("src.client_mode.ask_ip.ask_ip_dialog")
    @patch("src.client_mode.SOCKETS")
    def test_socket_connection_and_dialog(self, mock_sockets, mock_ask_ip_dialog):
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
        app.Sending_data.insert("1.0", "Hello, World!\n")  # Insert into Sending_data
        self.send_text_message(app, mock_ask_ip_dialog, mock_sockets)

        # Ensure the message was added to the chat history
        self.assertIn("Hello, World!", app.history.get("1.0", "end"))

        # Ensure SOCKETS methods were called as expected
        mock_sockets.assert_called_once()
        mock_socket_instance.connect.assert_called_once_with(("127.0.0.1", 5000))
        mock_socket_instance.send.assert_called_once_with("Hello, World!")


if __name__ == "__main__":
    unittest.main()
