import unittest
import automa

class TestAutomation(unittest.TestCase):
    def test_automate_tasks(self):
        # Teste unitário para a função automate_tasks
        tasks = ['task1', 'task2', 'task3']
        automa.automate_tasks(tasks)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()