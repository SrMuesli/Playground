#   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.
#   The letters in the returned list should be unique. For example,
#   common_letters("banana", "cream")
#   should return ['a'].
#   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def common_letters(string_one, string_two):
    common_letter = []
    for y in string_one:
        for x in string_two:
            if x == y and x in common_letter:
                continue
            elif x == y:
                common_letter.append(y)
            else:
                continue
    return common_letter



print(common_letters("manhattan", "san francisco"))
print(common_letters("python", "ruby on rails"))


#   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Esta es la solución que hace CodeCademy:
#   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

print(common_letters("manhattan", "san francisco"))
print(common_letters("python", "ruby on rails"))
