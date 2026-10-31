"""Araç Kutusu: grubun ortak yardımcı fonksiyonları.

Kural: Herkes kendi fonksiyonunu bu dosyanın EN ALTINA ekler.
"""


def greet(name: str) -> str:
    """Örnek (mentor): verilen isme selam verir. ör. greet('Ata') → 'Merhaba, Ata!'"""
    return f"Merhaba, {name}!"


def is_palindrome(word:str) ->bool:
    """Kelime tersten de aynı mı okunuyor? ör. is_palindrome('kek') → True, is_palindrome('elma') → False"""
    clean=word.lower()
    return clean==clean[::-1]