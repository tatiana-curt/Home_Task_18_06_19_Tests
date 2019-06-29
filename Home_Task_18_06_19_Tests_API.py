import unittest
import json
import requests

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        self.params = {}
        with open('fixtures/params.json', 'r', encoding='utf-8') as out_docs:
            self.params.update(json.load(out_docs))

    def test(self):
        response = requests.get(self.URL, params=self.params)
        result = response.json()['code']
        self.assertEqual(result, 200)

if __name__ == '__main__':
    unittest.main()