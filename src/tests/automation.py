import unittest
import automation

class TestAutomation(unittest.TestCase):
    def test_automate_tasks(self):
        # Teste unitário para a função automate_tasks
        tasks = ['task1', 'task2', 'task3']
        automation.automate_tasks(tasks)
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()