from data import docs2
import unittest



class UnitTestDoc(unittest.TestCase):
    def setUP(self):
        ...


    @classmethod
    def setupClass(cls):
        print('setupClass create user')

    def setUp(self) -> None:
        print('setUp')





    def test_multiplex_int(self):
        """
        проверка прав доступа
        """
        self.assertEqual(docs2.owners("10006"), 'Аристарх Павлов')

    def test_multiplex_int1(self):
        """
        проверка прав доступа
        """
        self.assertEqual(docs2.owners("11-2"), "Геннадий Покемонов")

    def test_multiplex_int2(self):
        """
        проверка прав доступа
        """
        self.assertEqual(docs2.owners("2207 876234"), 'Василий Гупкин')

    def test_multiplex_int3(self):
        """
        проверка прав доступа к несуществующему документу
        """
        self.assertEqual(docs2.owners("123"), f'документ не найден')

    def test_add_new_document(self):
        """
        добавляем документ на существующую полку
        """
        self.assertEqual(docs2.documents_add('11-04', 'invoice', 'Boba Fett', '3'), '3')

    def test_add_new_document1(self):
        """
        добавляем документ на существующую полку
        """
        self.assertEqual(docs2.documents_add('2206 7468941', 'passport', 'Darth Vader', '2'), '2')

    def test_add_new_document2(self):
        """
        добавляем документ на не существующую полку
        """
        self.assertEqual(docs2.documents_add('2206 7468941', 'passport', 'Darth Vader', '100'), None)

    def test_add_new_shelf(self):
        """
        добавляем полку
        """
        self.assertEqual(docs2.selv_add('4'), ('4', True))

    def test_add_new_shelf2(self):
        """
        добавляем полку
        """
        self.assertEqual(docs2.selv_add('1000'), ('1000', True))

    def test_remove_document(self):
        """удаляем документ"""
        self.assertEqual(docs2.doc_del('10006'), ('10006', True))

    def test_remove_document1(self):
        """удаляем не существующий документ"""
        self.assertEqual(docs2.doc_del('1006'), None)









    def tearDown(self) -> None:
        print('tearDown')

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass 123")