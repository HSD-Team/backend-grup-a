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