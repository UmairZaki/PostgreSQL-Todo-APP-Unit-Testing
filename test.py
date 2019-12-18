
import my_app
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        my_app.app.testing = True
        self.app = my_app.app.test_client()

    def test_allTasks(self):
        result = self.app.get('/todo/api/v1.0/tasks')
        self.assertEqual(result.status_code,200)
        # Make your assertions

    def test_singleTasks(self):
        result = self.app.get('/todo/api/v1.0/tasks/2')
        self.assertEqual(result.status_code,200)


    def test_addTask(self):
        result = self.app.post('/todo/api/v1.0/tasks')
        self.assertEqual(result.status_code,200)

    def test_updateTask(self):
        result = self.app.get('/todo/api/v1.0/tasks/4')
        self.assertEqual(result.status_code,200)

    def test_deleteTask(self):
        result = self.app.delete('/todo/api/v1.0/tasks/5')
        self.assertEqual(result.status_code,200)

    

if __name__ == '__main__':
    unittest.main()