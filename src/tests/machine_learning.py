import unittest
import machine_learning

class TestMachineLearning(unittest.TestCase):
    def test_build_model(self):
        # Teste unitário para a função build_model
        model = machine_learning.build_model()
        self.assertIsInstance(model, tf.keras.Model)

    def test_train_model(self):
        # Teste unitário para a função train_model
        X_train = np.array([[1, 2, 3], [4, 5, 6]])
        y_train = np.array([7, 8])
        model = machine_learning.build_model()
        machine_learning.train_model(model, X_train, y_train)
        self.assertGreater(model.history.history['loss'][0], 0)

if __name__ == '__main__':
    unittest.main()