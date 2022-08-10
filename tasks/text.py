from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    text = text.replace(',', '')

    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')

    text = text.strip()
    text = text.replace('.', '')
    text = text.replace(';', '')
    text = text.replace('!', '')

    text = text.replace('?', '')
    i = 0
    while (i<len(text)):
        if(text[i] == ' ' and text[i+1] == ' '):
            text = text[:i]+text[i+1:]
            i -= 1
        i += 1

    if(len(text) == 0):
        return (None,None)
    all_words = text.split(' ')
    maxx = all_words[0]
    minn = all_words[0]
    for i in all_words:
        if len(i)< len(minn):
            minn = i
        if len(i) > len(maxx):
            maxx = i
    return((minn,maxx))

