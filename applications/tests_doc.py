import pytest

from data import docs2

GET_NAME_CASES = [
    ("2207 876234", "Василий Гупкин"),
    ('11-2', "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов")
]

GET_SHELF_CASES = [
    ('2207 876234', 'документ #2207 876234 расположен на полке: - #1'),
    ('11-2', 'документ #11-2 расположен на полке: - #1'),
    ('10006', 'документ #10006 расположен на полке: - #2'),
    ('123', 'документ не найден на полке')
]

ADD_SHELF_CASES = ['4', '5', '6', '7']

ADD_NEW_DOCUMENT_CASES = [
    ('11-04', 'invoice', 'Boba Fett', '3', '3'),
    ('2206 7468941', 'passport', 'Darth Vader', '2', '2')
]

DELETE_DOCUMENT_CASES = [
    '2207 876234',
    '11-2', '10006'
]

CHECK_DOCUMENT = [
    ("2207 876234", True),
    ("11-2", True),
    ("10006", True),
    ("19906", False)
]


class TestApplication:

    # @pytest.mark.parametrize('doc_number, expected_result', GET_NAME_CASES)
    # def test_get_name_by_document_number(self, doc_number, expected_result):
    #     actual_result = docs2.owners(doc_number)
    #     assert actual_result == expected_result, 'Error'


    @pytest.mark.parametrize(
        'document_number,'
        'document_type,'
        'name, shelf,'
        'expected_result',
        ADD_NEW_DOCUMENT_CASES
    )
    def test_add_new_document(self, document_number, document_type, name, shelf, expected_result):
        actual_result = docs2.documents_add(document_number, document_type, name, shelf)
        assert actual_result == expected_result, 'Error'


    @pytest.mark.parametrize(
        'document_number',
        DELETE_DOCUMENT_CASES
    )

    def test_remove_document(self, document_number):
        assert docs2.doc_del(document_number) == (document_number, True)




    @pytest.mark.parametrize(
        'number, '
        'expected_res',
        CHECK_DOCUMENT
    )
    def test_check_document_existance(self, number, expected_res):
        actual_res = docs2.people(number)
        assert actual_res == expected_res

    @pytest.mark.parametrize(
        'doc_number, '
        'expected_result',
        GET_NAME_CASES
    )
    def test_get_name_by_document_number(self, doc_number, expected_result):
        actual_result = docs2.owners(doc_number)
        assert actual_result == expected_result, 'Error'

    @pytest.mark.parametrize(
        'doc_number, '
        'expected_result',
        GET_SHELF_CASES
    )
    def test_get_shelf_by_document_number(self, doc_number, expected_result):
        actual_result = docs2.shelves(doc_number)
        assert actual_result == expected_result, "Error"

    @pytest.mark.parametrize(
        'shelf',
        ADD_SHELF_CASES
    )
    def test_add_new_shelf(self, shelf):
        assert docs2.selv_add(shelf) == (shelf, True)
