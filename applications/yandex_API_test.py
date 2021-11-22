import unittest
from data.yndex_API import createfolder, get_folder_info, del_folder

FOLDERNAME = 'TEST_FOLDER'


class TestYandexAPI(unittest.TestCase):
    def test_createfolder(self):
        result = createfolder(FOLDERNAME)
        self.assertTrue(result == 201, f'Сервер ответил: {result}')

    def test_get_folder_info(self):
        self.assertTrue(get_folder_info(FOLDERNAME) == 'dir')

    def test_folder_status_code_201(self):
        self.assertEqual(createfolder(FOLDERNAME), 409)

    def test_folder_status_code_404(self):
        self.assertEqual(createfolder('//folder 02'), 404)

    def test_del_folder(self):
        self.assertEqual(del_folder(FOLDERNAME), 204)
