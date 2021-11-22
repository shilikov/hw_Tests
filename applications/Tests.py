import unittest
from data import docs2
from parameterized import parameterized


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand([
        ["2207 876234", "Василий Гупкин"],
        ["11-2", "Геннадий Покемонов"],
        ["10006", "Аристарх Павлов"],
        ["19906", 'документ не найден']
    ])
    def test_get_doc_owner_name(self, input_, actual_):
        self.assertEqual(docs2.owners(input_), actual_)
