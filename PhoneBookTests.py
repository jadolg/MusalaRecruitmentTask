import unittest

from PhoneBook import PhoneBook

NUMBERS_DO_NOT_MATCH = 'Number do not match'
RESULT_IS_NOT_NONE = 'Result is not None'
DELETE_DID_NOT_WORK = 'Delete did not work'


class PhoneBookTestCase(unittest.TestCase):
    def setUp(self):
        self.phonebook = PhoneBook()

    def test_load_from_file(self):
        self.phonebook.load_from_file('phonebook.txt')
        self.assertEqual([{'name': 'akiel', 'phone': '+359878123456'}, {'name': 'monik', 'phone': '+359878123459'}],
                         self.phonebook.phones, 'Phonebook loading failed')

    def test_parse_function(self):
        self.assertEqual('+359878123456', self.phonebook.parse_number('+359878123456'), NUMBERS_DO_NOT_MATCH)

    def test_parse_function_with_two_zero(self):
        self.assertEqual('+359878123456', self.phonebook.parse_number('00359878123456'), NUMBERS_DO_NOT_MATCH)

    def test_parse_function_with_one_zero(self):
        self.assertEqual('+359878123456', self.phonebook.parse_number('0878123456'), NUMBERS_DO_NOT_MATCH)

    def test_parse_function_cant_parse_without_plus(self):
        self.assertIsNone(self.phonebook.parse_number('359878123456'), RESULT_IS_NOT_NONE)

    def test_parse_function_invalid_operator_code(self):
        self.assertIsNone(self.phonebook.parse_number('+359008123456'), RESULT_IS_NOT_NONE)

    def test_parse_function_wrong_digit(self):
        self.assertIsNone(self.phonebook.parse_number('+359870123456'), RESULT_IS_NOT_NONE)

    def test_parse_function_with_random_data(self):
        self.assertIsNone(self.phonebook.parse_number('random text'), RESULT_IS_NOT_NONE)
        self.assertIsNone(self.phonebook.parse_number('+359 random text'), RESULT_IS_NOT_NONE)
        self.assertIsNone(self.phonebook.parse_number('+3590random text'), RESULT_IS_NOT_NONE)
        self.assertIsNone(self.phonebook.parse_number('+3598random text'), RESULT_IS_NOT_NONE)

    def test_delete_pair(self):
        self.phonebook.phones = [{'name': 'akiel', 'phone': '+359878123456'},
                                 {'name': 'monik', 'phone': '+359878123459'}]
        self.phonebook.delete_pair('akiel')
        self.assertEqual([{'name': 'monik', 'phone': '+359878123459'}], self.phonebook.phones, DELETE_DID_NOT_WORK)

    def test_get_phone_number(self):
        self.phonebook.phones = [{'name': 'akiel', 'phone': '+359878123456'},
                                 {'name': 'monik', 'phone': '+359878123459'}]
        self.assertEqual('+359878123459', self.phonebook.get_phone_number('monik'))

    def test_get_phone_number_returns_none_if_not_found(self):
        self.phonebook.phones = [{'name': 'akiel', 'phone': '+359878123456'},
                                 {'name': 'monik', 'phone': '+359878123459'}]
        self.assertIsNone(self.phonebook.get_phone_number('nobody'), RESULT_IS_NOT_NONE)

    def test_print_numbers(self):
        self.phonebook.add_pair('b', '+359878123459')
        self.phonebook.add_pair('a', '+359878123458')
        self.phonebook.add_pair('c', '+359878123457')
        self.phonebook.print_all_numbers()

    def test_set_outgoing_calls(self):
        self.phonebook.phones = [{'name': 'akiel', 'phone': '+359878123456'}, ]
        self.assertTrue(self.phonebook.set_outgoing_calls('akiel', 5), 'Could not find this contact')
        self.assertEqual([{'name': 'akiel', 'phone': '+359878123456', 'outgoing calls': 5}, ], self.phonebook.phones,
                         NUMBERS_DO_NOT_MATCH)
        self.assertFalse(self.phonebook.set_outgoing_calls('nobody', 5))

    def test_print_phones_sorted_by_outgoing_calls(self):
        self.phonebook.phones = [{'name': 'a', 'phone': '+359878123456', 'outgoing calls': 1},
                                 {'name': 'b', 'phone': '+359878123459', 'outgoing calls': 3},
                                 {'name': 'c', 'phone': '+359878123456', 'outgoing calls': 7},
                                 {'name': 'd', 'phone': '+359878123456', 'outgoing calls': 5},
                                 {'name': 'e', 'phone': '+359878123456', 'outgoing calls': 1},
                                 {'name': 'f', 'phone': '+359878123456'},
                                 ]
        self.phonebook.print_phones_sorted_by_outgoing_calls(5)
