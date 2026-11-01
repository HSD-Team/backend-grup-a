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

def factorial(number:int) ->int:
    """Girilen sayının faktöriyelini hesaplar. Örnek: 4! =24"""
    factorial_1=1
    for i in range(1,number+1):
        factorial_1*=i
    return factorial_1
    

