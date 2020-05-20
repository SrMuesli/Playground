#_________________________________________________________________________________________________________________________________________________________________


#Create a function named "divisible_by_ten()" that takes a list of numbers named nums as a parameter.
#Return the count of how many numbers in the list are divisible by 10.

#Write your function here
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))


#_________________________________________________________________________________________________________________________________________________________________


#Create a function named "add_greetings()" which takes a list of strings named names as a parameter.
#In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.
#Return the new list containing the greetings.

#Write your function here
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


#_________________________________________________________________________________________________________________________________________________________________


#Write a function called delete_starting_evens() that has a parameter named lst.
#The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
#For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
#Make sure your function works even if every element in the list is even!

#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


#_________________________________________________________________________________________________________________________________________________________________
