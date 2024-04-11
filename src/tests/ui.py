import unittest
import ui

class TestUI(unittest.TestCase):
    def test_display_menu(self):
        # Teste unitário para a função display_menu
        ui.display_menu()
        self.assertTrue(True)

    def test_get_user_choice(self):
        # Teste unitário para a função get_user_choice
        ui.display_menu()
        choice = ui.get_user_choice()
        self.assertIsInstance(choice, int)

if __name__ == '__main__':
    unittest.main()