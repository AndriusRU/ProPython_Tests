import pytest
import dataYandex as dataYa
from YandexDisk import YandexDisk


class TestYandexDisk:

    @staticmethod
    def setup(self):
        print('Start test')

    @staticmethod
    def teardown(self):
        print('End test')

    @pytest.mark.parametrize("f_name, result", dataYa.MAKE_FOLDER)
    def test_create_folder(self, f_name, result):
        assert YandexDisk.create_folder(YandexDisk(dataYa.token), f_name) == result

    @pytest.mark.parametrize("f_name, status", dataYa.DELETE_FOLDER)
    def test_delete_folder(self, f_name, status):
        assert YandexDisk.delete_folder(YandexDisk(dataYa.token), f_name) == status


if __name__ == '__main__':
    pytest.main()
