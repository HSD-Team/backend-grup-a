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

def is_leap_year(year: int) -> bool:
    # is_leap_year: yil artik yil mi? (2024 → True, 1900 → False)
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def reverse_words(metin:str) ->str:
    """kelimelerin sırasını ters çevirir (bugün hava güzel → güzel hava bugün)"""
    return ' '.join(metin.split()[::-1])#.join() metodu ile ters çevrilmiş kelimeleri birleştiriyoruz.
    #.split() metodu ile metni kelimelere ayırıyoruz ve [::-1] ile ters çeviriyoruz.

def fibonacci(n:int) -> int:
    """returns the nth number in the fibonacci sequence."""
    s=[0,1,1,0]
    for i in range(0,n):
        s[3] = s[1] + s[2]
        s[0:3] = s[1:4]
    return s[0]
