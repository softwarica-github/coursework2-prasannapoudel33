import unittest
from unittest.mock import patch

# Assuming ask_ip_dialog is in a module named src.ask_mode
from src.ask_mode import ask_ip_dialog


class TestAskIPDialog(unittest.TestCase):

    @patch("src.ask_mode.Tkinter.IntVar")
    def test_mode_selection(self, mock_IntVar):
        mock_mode = mock_IntVar.return_value
        mock_mode.get.side_effect = [0, 1]  # Simulate the modes being set

        # First call simulation, expecting Client Mode (0)
        mode = ask_ip_dialog()
        self.assertEqual(mode, 0)

        # Reset the side effect for the next call
        mock_mode.get.side_effect = [1]  # Simulate Server Mode (1)

        # Second call simulation, expecting Server Mode (1)
        mode = ask_ip_dialog()
        self.assertEqual(mode, 1)


if __name__ == "__main__":
    unittest.main()
