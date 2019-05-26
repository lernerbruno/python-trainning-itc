import re
import zipfile

path = '/Users/brunolerner/workspace/python-trainning-itc/python_challenges/channel/'
filename = '90052.txt'
files_in_order = ['90052.txt']
while True:
    f = open(path + filename, 'r')
    content = f.read()
    print(content)
    match = re.search(r'[0-9]+', content)
    if match is None:
        break
    number = match.group()
    filename = number + filename[filename.index("."):]
    files_in_order.append(filename)

archive = zipfile.ZipFile('/Users/brunolerner/Downloads/channel.zip', 'r')
comments = ""
for file in files_in_order:
    comment = archive.getinfo(file).comment.decode('utf-8')
    if comment != " ":
        comments += comment
    print(comments)


