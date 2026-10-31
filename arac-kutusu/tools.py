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

def is_pwd_strong(password: str) -> bool:
    """Parola güçlü mü? ör. is_pwd_strong('hsdANKARA06') -> True, is_pwd_strong('abc123') -> False"""
    if len(password) < 8:
        return False

    has_upper = False
    has_number = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_number = True

    return has_upper and has_number