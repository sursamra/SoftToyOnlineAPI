import unittest
import json

from ..app import app


class TestToyCatalogAPI(unittest.TestCase):
    def setUp(self):
        app.config['ENV'] = 'development'
        app.config['TESTING'] = True
        app.config['REPOSITORY'] = 'memory'
        self.app = app.test_client()

    def test_get_toys(self):
        response = self.app.get('/toys')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('toys' in data)

    def test_add_toy(self):
        toy_data = {"name": "NewToy", "description": "soft toy", "price": 25, "quantity": 1000}
        response = self.app.post('/toys', data=json.dumps(toy_data), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)
        self.assertTrue('toy' in data)

    def test_update_toy_when_toy_exists(self):
        toy_data = {"name": "UpdatedToy"}
        response = self.app.put('/toys/3', data=json.dumps(toy_data), content_type='application/json')
        data = {}
        try:
            data = json.loads(response.get_data(as_text=True))
        except Exception as ex:
            pass
        self.assertEqual(data['message'], "Toy updated successfully")
        self.assertEqual(response.status_code, 200)

    def test_update_toy_when_toy_does_not_exists(self):
        toy_data = {"name": "UpdatedToy"}
        response = self.app.put('/toys/10', data=json.dumps(toy_data), content_type='application/json')
        try:
            data = json.loads(response.get_data(as_text=True))
        except Exception as ex:
            # print("Error while parsing response as JSON:", ex)
            pass

        self.assertIn("Toy not found", response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)

    def test_delete_toy_when_toy_exits(self):
        response = self.app.delete('/toys/5')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Toy deleted successfully")

    def test_delete_toy_when_toy_does_not_exists(self):
        response = self.app.delete('/toys/999')
        try:
            data = json.loads(response.get_data(as_text=True))
        except Exception as ex:
            print("Error while parsing response as JSON:", ex)

        self.assertIn("Toy not found", response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)

    def test_search_toys_by_name(self):
        response = self.app.get('/toys?name=Harkle')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('toys' in data)
        self.assertTrue(all('Harkle' in toy['name'] for toy in data['toys']))

    def test_pagination(self):
        response = self.app.get('/toys?page=1&per_page=2')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('toys' in data)
        per_page = 2
        expected_num_items = min(per_page, len(data['toys']))
        self.assertEqual(len(data['toys']), expected_num_items)


if __name__ == '__main__':
    unittest.main()
