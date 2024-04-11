import unittest
import interaction

class TestInteraction(unittest.TestCase):
    def test_process_natural_language_input(self):
        # Teste unitário para a função process_natural_language_input
        input_text = 'Hello, world!'
        processed_text = interaction.process_natural_language_input(input_text)
        self.assertIsInstance(processed_text, str)

    def test_synthesize_speech(self):
        # Teste unitário para a função synthesize_speech
        output_text = 'Hello, world!'
        synthesized_speech = interaction.synthesize_speech(output_text)
        self.assertIsInstance(synthesized_speech, str)

if __name__ == '__main__':
    unittest.main()