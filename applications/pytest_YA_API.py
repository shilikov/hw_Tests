from data.yndex_API import createfolder, get_folder_info, del_folder
import pytest

MAKE_FOLDER_CASES = [
    ("folder 01", 201),
    ("folder 10", 201),
    ("folder 15", 201),
    ("//folder 02", 404),
    ("folder 01", 409),
    ("folder 03/subfolder", 409),
]

DEL_FOLDER_CASES = [
    ("folder 01", 204),
    ("folder 10", 204),
    ("folder 15", 204),
]

class TestYandexMakeFolder:
    @pytest.mark.parametrize("folder_name, "
                             "expected_result",
                             MAKE_FOLDER_CASES
                             )
    def test_folder_status_code_argument(self, folder_name, expected_result):
        assert createfolder(folder_name) == expected_result, 'Error'

    @pytest.mark.parametrize("folder_name, "
                             "expected_result",
                             DEL_FOLDER_CASES
                             )
    def test_del_folder(self, folder_name, expected_result):
        assert del_folder(folder_name) == expected_result, 'Error'


