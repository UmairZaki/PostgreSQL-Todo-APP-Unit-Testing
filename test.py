import app1
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        app1.app.testing = True
        self.app = app1.app.test_client()

    def test_allTasks(self):
        result = self.app.get('/getTask')
        self.assertEqual(result.status_code,200)

    def test_singleTasks(self):
        result = self.app.get('/getSingleTask/102')
        self.assertEqual(result.status_code,200)


    def test_addTask(self):
        result = self.app.post('/createTask')
        self.assertEqual(result.status_code,200)

    def test_updateTask(self):
        result = self.app.put('/updateTask')
        self.assertEqual(result.status_code,200)

    def test_deleteTask(self):
        result = self.app.delete('/deleteTask/101')
        self.assertEqual(result.status_code,200)

    

if __name__ == '__main__':
    unittest.main()
