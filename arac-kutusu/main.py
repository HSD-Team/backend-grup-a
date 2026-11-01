import tools

print(tools.greet("Araç Kutusu"))
# Herkes kendi fonksiyonunu deneyen bir satırı bu yorumun ALTINA ekler:


print("count_vowels('merhaba') ->"
      , tools.count_vowels("merhaba"))
print("is_palindrome('kayak) -> ",
      tools.is_palindrome("kayak"))

print("longest_word('en uzun kelimeli cümle')->",tools.longest_word("en uzun kelimeli cümle"))