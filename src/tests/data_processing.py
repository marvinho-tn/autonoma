import unittest
import data_processing

class TestDataProcessing(unittest.TestCase):
    def test_load_data(self):
        # Teste unitário para a função load_data
        data = data_processing.load_data('test_data.csv')
        self.assertIsInstance(data, np.ndarray)

    def test_preprocess_data(self):
        # Teste unitário para a função preprocess_data
        data = np.array([1, 2, 3, 4, 5])
        preprocessed_data = data_processing.preprocess_data(data)
        self.assertEqual(preprocessed_data.mean(), 3)

if __name__ == '__main__':
    unittest.main()