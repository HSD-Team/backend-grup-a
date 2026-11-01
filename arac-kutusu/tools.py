"""Araç Kutusu: grubun ortak yardımcı fonksiyonları.

Kural: Herkes kendi fonksiyonunu bu dosyanın EN ALTINA ekler.
"""


def greet(name: str) -> str:
    """Örnek (mentor): verilen isme selam verir. ör. greet('Ata') → 'Merhaba, Ata!'"""
    return f"Merhaba, {name}!"



def count_vowels(text:str) -> int:
    """Metindeki sesli harflerin sayısını döndürür. Örnek: count_vowels('Merhaba') → 3"""
    count = 0
    for letter in text.lower():
        if letter in "aeiıoöuü":
            count += 1
    return count        

def is_palindrome(word:str) ->bool:
    """Kelime tersten de aynı mı okunuyor? ör. is_palindrome('kek') → True, is_palindrome('elma') → False"""
    clean=word.lower()
    return clean==clean[::-1]

def longest_word(sentence:str)->str:
    """Cümledeki en uzun kelimeyi döndürür. Örnek longest_word('en uzun kelime')-> kelime"""
    words=sentence.split()
    max_word=  max(words,key=len)
    return max_word