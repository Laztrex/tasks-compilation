import unittest
from collections import defaultdict
from termcolor import cprint
from unittest.mock import patch, call
from caesar_encryptor import CaesarEncrypt
from vijener_encryptor import VijenerEnc


class GlobalCaesarTest(unittest.TestCase):
    VALUES_FOR_TEST_NORMAL = [('скиллбокс', 3, 'encode', 'ru'), ('привет', 5, 'encode', 'ru'),
                              ('а с русским текстом выйдет?', 1, 'encode', 'ru')]
    VALUES_FOR_TEST_UPPER = [('СКИЛЛБОКС', 3, 'encode', 'ru'), ('ПРИВЕТ', 5, 'encode', 'ru'),
                             ('А С РУССКИМ ТЕКСТОМ ВЫЙДЕТ?', 1, 'encode', 'ru'), ('AVE CAESAR', 3, 'encode', 'en'),
                             ('ПРАКТИКУМ ПО МАТЕМАТИКЕ И ПАЙТОН', 22, 'encode', 'ru'),
                             ('HIDEO KOJIMA', 12, 'encode', 'en')]
    VALUES_FOR_TEST_UPPER_LOWER = [('СКиЛлБоКс', 3, 'encode', 'ru'), ('ПривЕТ', 5, 'encode', 'ru'),
                                   ('А с РУсСКим тЕкСТОм ВыЙдЕт?', 1, 'encode', 'ru'),
                                   ('Ave CAeSaR', 3, 'encode', 'en'),
                                   ('ПРАКтикУМ по МАтемаТИКЕ И ПАйТоН', 22, 'encode', 'ru'),
                                   ('HIdeO KOjiMA', 12, 'encode', 'en')]
    VALUES_FOR_TEST_MIX = [('Английский Do you speak it?', 9, 'encode'), ('50 центов is rapper', 14, 'encode'),
                           ('Рунглиш, русслиш, руглиш, или русинглиш (англ. Runglish, Russlish, Ruglish, Rusinglish) '
                            '— это смесь русского и английского...', 5, 'encode')]

    def setUp(self):
        self.caesar_test = defaultdict(lambda: [])
        for num, name_test in enumerate([self.VALUES_FOR_TEST_NORMAL,
                                         self.VALUES_FOR_TEST_UPPER,
                                         self.VALUES_FOR_TEST_UPPER_LOWER,
                                         self.VALUES_FOR_TEST_MIX]):
            self.caesar_test[num] = [CaesarEncrypt(*data) for data in name_test]
        cprint(f'Вызван {self.shortDescription()}', flush=True, color='cyan')

    def tearDown(self):
        cprint(f'Результаты будут прологированы, но потом :)')

    @patch('builtins.print', return_value=None)
    def test_normal(self, mocked_print):
        """Тест при нормальных условиях"""
        results = ['фнлоодснф', 'фхнжйч', 'бтсфттлйнуёлтупнгькеёу']

        for num, data in enumerate(self.caesar_test[0]):
            caesar_test = data.run()
            self.assertEqual(caesar_test, results[num])

    @patch('builtins.print', return_value=None)
    def test_upper(self, mocked_print):
        """Тест при верхнем регистре user_word"""
        results = ['фнлоодснф', 'фхнжйч', 'бтсфттлйнуёлтупнгькеёу', 'dyhfdhvdu',
                   'еёхазюаиведвхзъвхзюаъюехяздг', 'tupqawavuym']

        for num, data in enumerate(self.caesar_test[1]):
            caesar_test = data.run()
            self.assertEqual(caesar_test, results[num])

    @patch('builtins.print', return_value=None)
    def test_upper_lower(self, mocked_print):
        """Тест при смешанном регистре user_word"""
        results = ['фнлоодснф', 'фхнжйч', 'бтсфттлйнуёлтупнгькеёу', 'dyhfdhvdu',
                   'еёхазюаиведвхзъвхзюаъюехяздг', 'tupqawavuym']

        for num, data in enumerate(self.caesar_test[2]):
            caesar_test = data.run()
            self.assertEqual(caesar_test, results[num])

    @patch('builtins.print', return_value=None)
    def test_mix(self, mocked_print):
        """Тест при смешанном алфавите"""
        results = ['ицлфстъустmxhxdbynjtrc', '50дтыаьпwgfoddsf',
                   'хштзрнэхшццрнэхшзрнэнрнхшцнтзрнэетзрwzslqnxmwzxxqnxmwzlqnxmwzxnslqnxmвчуцсйцбхшццпузунетзрноцпузу']

        for num, data in enumerate(self.caesar_test[3]):
            caesar_test = data.run()
            self.assertEqual(caesar_test, results[num])


class GlobalVijenerTest(unittest.TestCase):
    VALUES_FOR_TEST_NORMAL = [('скиллбокс', 'привет', 'encode', 'ru'), ('привет', 'скиллбокс', 'encode', 'ru'),
                              ('карл у клары украл кораллы', 'кларнет', 'encode', 'ru'),
                              ('аннигиляция', 'гарленд', 'encode', 'ru')]
    VALUES_FOR_TEST_UPPER = [('СКИЛЛБОКС', 'ПРИВЕТ', 'encode', 'ru'), ('ПРИВЕТ', 'СКИЛЛБОКС', 'encode', 'ru'),
                             ('КАРЛ У КЛАРЫ УКРАЛ КОРАЛЛЫ', 'КЛАРНЕТ', 'encode', 'ru'),
                             ('АННИГИЛЯЦИЯ', 'ГАРЛЕНД', 'encode', 'ru')]
    VALUES_FOR_TEST_UPPER_LOWER = [('СКиЛлБоКс', 'ПрИВЕт', 'encode', 'ru'), ('ПривЕТ', 'скиллбокС', 'encode', 'ru'),
                                   ('КАрЛ у КЛары УкрАл КОРАллЫ', 'кларНеТ', 'encode', 'ru'),
                                   ('АННИГилЯцИя', 'Гарленд', 'encode', 'en'), ]

    def setUp(self):
        self.vijener_test = defaultdict(lambda: [])
        for num, name_test in enumerate([self.VALUES_FOR_TEST_NORMAL,
                                         self.VALUES_FOR_TEST_UPPER,
                                         self.VALUES_FOR_TEST_UPPER_LOWER, ]):
            self.vijener_test[num] = [VijenerEnc(*data) for data in name_test]
        cprint(f'Вызван {self.shortDescription()}', flush=True, color='cyan')

    def tearDown(self):
        cprint(f'Результаты будут прологированы, но потом :)')

    @patch('builtins.print', return_value=None)
    def test_normal(self, mocked_print):
        """Тест при нормальных условиях"""
        results = ['быснруюыъ', 'быснру', 'хлрьбпюкьыдшхтццобнрюё', 'гнюфзцпвцщк']

        for num, data in enumerate(self.vijener_test[0]):
            vijener_test = data.run()
            self.assertEqual(vijener_test, results[num])

    @patch('builtins.print', return_value=None)
    def test_upper(self, mocked_print):
        """Тест при верхнем регистре user_word"""
        results = ['быснруюыъ', 'быснру', 'хлрьбпюкьыдшхтццобнрюё', 'гнюфзцпвцщк']

        for num, data in enumerate(self.vijener_test[1]):
            vijener_test = data.run()
            self.assertEqual(vijener_test, results[num])

    @patch('builtins.print', return_value=None)
    def test_upper_lower(self, mocked_print):
        """Тест при смешанном регистре user_word"""
        results = ['быснруюыъ', 'быснру', 'хлрьбпюкьыдшхтццобнрюё', 'гнюфзцпвцщк']

        for num, data in enumerate(self.vijener_test[2]):
            vijener_test = data.run()
            self.assertEqual(vijener_test, results[num])


if __name__ == '__main__':
    unittest.main()
