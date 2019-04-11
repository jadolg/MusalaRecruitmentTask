import re


class PhoneBook:
    phones = []

    @staticmethod
    def parse_number(line: str) -> str:
        """
        Parses a Bulgarian phone number on any format
        :param line: text where the supposed number is without any extra data
        :return: either the phone number or None
        """
        number = None
        if line.startswith('00359'):
            number = line.replace('00', '+', 1)
        elif line.startswith('08'):
            number = line.replace('0', '+359', 1)
        elif line.startswith('+359'):
            number = line

        if number and not re.match(r'^\+3598[789][2-9]\d{6}$', number):
            return None

        return number

    def load_from_file(self, file: str):
        """
        Loads name,phone pairs from a file into self.phones
        :param file: path to the file containing the data
        :return: Nothing
        """
        self.phones = []

        phones_file = open(file, 'r')
        for line in phones_file:
            try:
                name, phone = [part.strip() for part in line.split(',')]
                self.add_pair(name, phone)
            except ValueError:
                continue
        phones_file.close()

    def add_pair(self, name: str, number: str):
        """
        Add a new pair of name, number to the phones array
        :param name: name of the contact
        :param number: number of the contact
        :return: Nothing
        """
        phone = self.parse_number(number)
        if phone:
            self.phones.append({'name': name, 'phone': phone})
            # Sort after inserting to avoid sorting when printing
            list.sort(self.phones, key=lambda pair: pair['name'])
        else:
            raise ValueError("")

    def get_phone_number(self, name: str) -> str:
        """
        Gets a specific phone number by name
        :param name: name of the contact
        :return: either the phone number corresponding to this name or None
        """
        for number in self.phones:
            if number['name'] == name:
                return number['phone']
        return None

    def delete_pair(self, name: str):
        """
        Deletes the pair name, number from the phones array
        :param name: name of the contact
        :return: Nothing
        """
        for number in self.phones:
            if number['name'] == name:
                self.phones.remove(number)

    def print_all_numbers(self):
        """
        Prints all numbers which are already sorted by name
        :return:
        """
        for number in self.phones:
            print(f'Name: {number["name"]} Number:{number["phone"]}')

    def set_outgoing_calls(self, name, outgoing_calls: int) -> bool:
        """
        Set the amount of outgoing calls for a number
        :param name: name of the contact
        :param outgoing_calls: amount of outgoing calls
        :return:
        """
        for number in self.phones:
            if number['name'] == name:
                number['outgoing calls'] = outgoing_calls
                return True
        return False

    def print_phones_sorted_by_outgoing_calls(self, limit=5):
        """
        Print the phones sorted by outgoing calls
        :param limit: how many numbers to show in the output
        :return:
        """
        for i, number in enumerate(sorted(self.phones,
                                          key=lambda pair: pair['outgoing calls'] if 'outgoing calls' in pair else 0,
                                          reverse=True)):
            if i == limit:
                break

            outgoing_calls = 0
            if 'outgoing calls' in number:
                outgoing_calls = number["outgoing calls"]

            print(f'Name: {number["name"]} Number:{number["phone"]} Outgoing calls: {outgoing_calls}')
