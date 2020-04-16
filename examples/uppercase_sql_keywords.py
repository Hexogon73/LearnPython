import re


def uppercase_sql_keywords(text: str):
    """Convert to uppercase SQL keywords

    :param text: original text
    :return: list converted strings
    """
    strings = text.split('\n')
    strings = [string for string in strings if string]
    result = []
    keywords = ('declare', 'begin', 'end', 'commit',
                'from', 'where', 'on', 'and', 'delete',
                'is', 'null', 'set', 'update', 'like',
                'in', 'select')
    for string in strings:
        for word in keywords:
            pattern = re.compile(fr'\b{word}\b')
            if re.search(pattern, string):
                string = re.sub(pattern, word.upper(), string)
        result.append(string)
    return result


if __name__ == '__main__':
    while True:
        text = input()
        if not text:
            break
        print('\n'.join(uppercase_sql_keywords(text)))
