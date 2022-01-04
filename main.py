import zipfile
import os


class Statistics:

    def __init__(self, file_name):
        self.file_name = os.path.normpath(file_name)
        self.stat = {}
        self.total = 0

    def __enter__(self):
        print('Начал работу!')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return 'Завершил работу!'

    # Метод который вызывается если на вход даётся архив .zip
    def unzip(self):
        """Method for unpacking .zip archives"""
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collapse(line)

    def _collapse(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat.keys():
                    self.stat[char] += 1
                    self.total += 1
                else:
                    self.stat[char] = 1

    def frequency_descending(self):
        """Order by frequency - descending"""
        with open(self.file_name, 'r', encoding='cp1251') as file:
            print(f'+{"+":-^31}+')
            print(f'|{"Буква":^15}|{"Частота":^15}|')
            print(f'+{"+":-^31}+')

            for line in file:
                self._collapse(line)

            list_d = list(self.stat.items())
            list_d.sort(key=lambda i: i[1], reverse=True)

            for i in list_d:
                print('|{0:^15}|{1:^15d}|'.format(i[0], i[1]))

            print(f'+{"+":-^31}+')
            print(f'|{"Итого":^15}|{self.total:^15d}|')
            print(f'+{"+":-^31}+')

    def frequency_ascending(self):
        """Order by frequency - ascending"""
        with open(self.file_name, 'r', encoding='cp1251') as file:
            print(f'+{"+":-^31}+')
            print(f'|{"Буква":^15}|{"Частота":^15}|')
            print(f'+{"+":-^31}+')

            for line in file:
                self._collapse(line)

            list_d = list(self.stat.items())
            list_d.sort(key=lambda i: i[1])

            for i in list_d:
                print('|{0:^15}|{1:^15d}|'.format(i[0], i[1]))

            print(f'+{"+":-^31}+')
            print(f'|{"Итого":^15}|{self.total:^15d}|')
            print(f'+{"+":-^31}+')

    def key_alphabetically(self):
        """Sorting by key - alphabetically"""
        with open(self.file_name, 'r', encoding='cp1251') as file:
            print(f'+{"+":-^31}+')
            print(f'|{"Буква":^15}|{"Частота":^15}|')
            print(f'+{"+":-^31}+')

            for line in file:
                self._collapse(line)

            for key, value in sorted(self.stat.items()):
                print('|{0:^15}|{1:^15d}|'.format(key, value))

            print(f'+{"+":-^31}+')
            print(f'|{"Итого":^15}|{self.total:^15d}|')
            print(f'+{"+":-^31}+')

    def key_alphabetically_reverse(self):
        """Sorting by key - alphabetically (reverse)"""
        with open(self.file_name, 'r', encoding='cp1251') as file:
            print(f'+{"+":-^31}+')
            print(f'|{"Буква":^15}|{"Частота":^15}|')
            print(f'+{"+":-^31}+')

            for line in file:
                self._collapse(line)

            for key, value in sorted(self.stat.items(), reverse=True):
                print('|{0:^15}|{1:^15d}|'.format(key, value))

            print(f'+{"+":-^31}+')
            print(f'|{"Итого":^15}|{self.total:^15d}|')
            print(f'+{"+":-^31}+')


work = Statistics(file_name='voyna-i-mir.txt.zip')
work.unzip()
work.collect()
work.key_alphabetically()
