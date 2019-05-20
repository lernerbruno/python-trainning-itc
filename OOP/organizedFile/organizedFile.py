from datetime import datetime


class OrganizedFile:
    DATE_FORMAT = "%m/%d/%Y, %H:%M"
    SUMMARY_FORMAT = '\nLine count: %d; Last updated: %s'

    def __init__(self, path):
        self.org_file_object = open(path, 'a+')

    def read(self):
        self.org_file_object.seek(0)
        return self.org_file_object.read()

    def readline(self):
        self.org_file_object.seek(0)
        return self.org_file_object.readline()

    def write(self, content):
        self.org_file_object.truncate(0)
        return self.org_file_object.write(content)

    def append(self, content):
        return self.org_file_object.write(content)

    def _get_files_sizes(self, other):
        file1_content = self.read()
        file2_content = other.read()

        size_1 = file1_content.count('a')
        size_2 = file2_content.count('a')

        return size_1, size_2

    def __lt__(self, other):
        size_1, size_2 = self._get_files_sizes(other)
        return size_1 < size_2

    def __gt__(self, other):
        size_1, size_2 = self._get_files_sizes(other)

        return size_1 > size_2

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        file_content = self.read()
        number_of_lines = 1 + file_content.count('\n')
        time = datetime.now().strftime(self.DATE_FORMAT)

        self.append(self.SUMMARY_FORMAT % (number_of_lines, time))
        self.org_file_object.close()


print(OrganizedFile('first.txt') > OrganizedFile('second.txt'))
print(OrganizedFile('second.txt') > OrganizedFile('first.txt'))

with OrganizedFile('first.txt') as file:
    file.append('\nc')
