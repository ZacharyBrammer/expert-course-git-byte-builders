'''
Complete the following exercises with your team!
Then create a new branch with your name.
Add, commit, and push your commit to origin on this new branch.
Finally, create a pull request.
'''

def fizzbuzz():
    '''
    Write a function that prints the numbers from 1 to 100. But for multiples of three
    print "Fizz" instead of the number and for the multiples of five print "Buzz". For
    numbers which are multiples of both three and five print "FizzBuzz".
    '''
    print('')

def is_palindrome(str):
    '''
    Write a function that checks if a given string is a palindrome (i.e. reads the same
    forwards and backwards). For example, "racecar" is a palindrome.
    '''
    return False

def is_anagram(str1, str2):
    '''
    Write a function that checks if two given strings are anagrams (i.e. contain the same
    letters but in a different order). For example, "listen" and "silent" are anagrams.
    '''
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

def count_vowels(str):
    '''
    Write a program that takes a string as input and counts the number of vowels
    (a, e, i, o, u, A, E, I, O, U) in the string.
    '''
    return 0

def reverse_list(lst):
    '''
    Write a function that takes a list as input and returns a new list with the elements
    reversed. For example, [1, 2, 3] should become [3, 2, 1].
    '''
    return lst

if __name__ == '__main__':
    # test and run your functions here
    # fizzbuzz()
    # print(is_palindrome('racecar'))
    # print(is_palindrome('not a palindrome'))
    print(is_anagram('listen', 'silent'))
    # print(is_anagram('not an anagram', 'anagram'))
    # print(count_vowels('there are vowels in HERE'))
    # print(reverse_list([1, 2, 3, 4, 5]))