import tools

print(tools.greet("Araç Kutusu"))
# Herkes kendi fonksiyonunu deneyen bir satırı bu yorumun ALTINA ekler:


print("count_vowels('merhaba') ->"
      , tools.count_vowels("merhaba"))
print("is_palindrome('kayak) -> ",
      tools.is_palindrome("kayak"))
print("is_leap_year(2100) ->"
      , tools.is_leap_year(2100))

print("reverse_words('bugün hava güzel') ->", tools.reverse_words("bugün hava güzel"))
