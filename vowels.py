def countvowels(strings):
   vowel = "aeiou"
   list_vowels = 0
   print ([letter for letter in strings if letter in vowel])
   print (len([letter for letter in strings if letter in vowel]))
countvowels('drink water')


