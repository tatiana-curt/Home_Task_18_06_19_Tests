# Следует протестировать основные функции по получению информации
# о документах, добавлении и удалении элементов из словаря

import unittest
import app
import json
from mock import patch

documents = []
directories = {}
def setUpModule():
    with open('fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
        documents.extend(json.load(out_docs))
    with open('fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
        directories.update(json.load(out_dirs))

@patch('app.directories', directories, create=True)
@patch('app.documents', documents, create=True)
class TestSecretaryProgram(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertTrue(app.check_document_existance(documents[1]['number']))
        with patch('app.input', return_value=documents[1]['number']):
            self.assertEqual(app.get_doc_owner_name(), documents[1]['name'])

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)
        self.assertGreater(len(app.get_all_doc_owners_names()), 0)

    def test_remove_doc_from_shelf(self):
        app.remove_doc_from_shelf(documents[0]['number'])
        self.assertNotIn(documents[0]['number'], directories['1'])

    def test_add_new_shelf(self):
        with patch('app.input', return_value='4'):
            self.assertIn(app.add_new_shelf()[0], directories.keys())
            # print(directories.keys())

    def test_append_doc_to_shelf(self):
        app.append_doc_to_shelf(documents[0]['number'], '3')
        self.assertIn(documents[0]['number'], directories['3'])

    def test_delete_doc(self):
        del_doc_number = documents[1]['number']
        self.assertTrue(app.check_document_existance(del_doc_number))
        with patch('app.input', return_value=del_doc_number):
            app.delete_doc()
        self.assertFalse(app.check_document_existance(del_doc_number))

    @patch('app.input')
    def test_move_doc_to_shelf(self, mock_input):
        mock_input.side_effect = [documents[1]['number'], '3']
        app.move_doc_to_shelf()
        self.assertIn(documents[1]['number'], directories['3'])
    #

    def test_get_doc_shelf(self):
        doc_number = documents[0]['number']
        with patch('app.input', return_value=doc_number):
            self.assertEqual(app.get_doc_shelf(), '1')
    #
    @patch('app.input')
    def test_add_new_doc(self, mock_input):
        mock_input.side_effect = [documents[0]['number'], documents[0]['type'], documents[0]['name'], '4']
        app.add_new_doc()
        self.assertGreater(len(documents), 3)

if __name__ == '__main__':
    unittest.main()