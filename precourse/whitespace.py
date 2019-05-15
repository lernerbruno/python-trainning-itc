def remove_whitespace(string):
    while string.endswith(" ") or string.endswith("\n") or string.endswith("\t"):
        string = string[:-1]

    while string.startswith(" ") or string.startswith("\n") or string.startswith("\t"):
        string = string[1:]

    return string

def remove_whitespace_revised(string):
     return  string.strip()

if __name__ == '__main__':
    print(remove_whitespace('  '
                            's d f      '
                            ''))
    print(remove_whitespace_revised('  '
                            's d f      '
                            ''))