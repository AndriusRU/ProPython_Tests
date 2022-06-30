import app
import unittest
from unittest.mock import patch
from parameterized import parameterized

class TestFunction(unittest.TestCase):

    def setUp(self):
        print('Begin test ', self)

    def tearDown(self):
        print('End test ', self)

    # Проверка существования документов
    @parameterized.expand([("2207 876234", True), ("10006", True)])
    def test_check_document_existance(self, doc, my_bool):
        self.assertEqual(app.check_document_existance(doc), my_bool)

    # Проверка принадлежности документа человеку
    @patch('builtins.input', side_effect=["11-2"])
    def test_get_doc_owner_name(self, mock_input):
        self.assertEqual(app.get_doc_owner_name(), "Геннадий Покемонов")

    # Проверка удаления существующего документа
    @patch('builtins.input', return_value="10006")
    def test_delete_doc(self, mock_input):
        call_1 = mock_input()
        self.assertEqual(app.delete_doc(), (call_1, True))

    # Проверка добавления полок - как существующей, так и новой
    @parameterized.expand([("10", True), ("1", False)])
    def test_add_new_shelf(self, shelf, my_bool):
        self.assertEqual(app.add_new_shelf(shelf), (shelf, my_bool))

    # Проверка удаления несуществующего документа
    @patch('builtins.input', side_effect="1006")
    def test_delete_doc_fail(self, mock_input):
        call_1 = mock_input()
        self.assertEqual(app.delete_doc(), None)


if __name__ == '__main__':
    unittest.main()