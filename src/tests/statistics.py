import unittest
import statistics

class TestStatistics(unittest.TestCase):
    def test_calculate_mean(self):
        # Teste unitário para a função calculate_mean
        data = np.array([1, 2, 3, 4, 5])
        mean = statistics.calculate_mean(data)
        self.assertEqual(mean, 3)

    def test_calculate_std(self):
        # Teste unitário para a função calculate_std
        data = np.array([1, 2, 3, 4, 5])
        std = statistics.calculate_std(data)
        self.assertAlmostEqual(std, 1.5811388300841898)

if __name__ == '__main__':
    unittest.main()