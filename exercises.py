'''
Complete the following exercises with your team!
Then create a new branch with your name.
Add, commit, and push your commit to origin on this new branch.
Finally, create a pull request.
'''

def fizzbuzz():
    for i in range(100):
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)

def is_palindrome(str):
    reversedstring = str[::-1]
    if reversedstring == str:
        print("It's a palindrome")
    else:
        return False


def is_anagram(str1, str2):
    # anagram checker
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)

def count_vowels(str):
    '''
    Write a program that takes a string as input and counts the number of vowels
    (a, e, i, o, u, A, E, I, O, U) in the string.
    '''
    vowels = 0
    vowelList = 'aeiou'
    for ch in str:
        if ch.lower() in vowelList:
            vowels+=1
    return vowels

def reverse_list(lst):
    lst1 = lst.reverse()
    
    '''
    Write a function that takes a list as input and returns a new list with the elements
    reversed. For example, [1, 2, 3] should become [3, 2, 1].
    '''
    return lst

if __name__ == '__main__':
    # test and run your functions here
    fizzbuzz()
    print(is_palindrome('racecar'))
    print(is_palindrome('not a palindrome'))
    # print(is_anagram('listen', 'silent'))
    # print(is_anagram('not an anagram', 'anagram'))
    print(reverse_list([1, 2, 3, 4, 5]))
    print(count_vowels('there are vowels in HERE'))
    # print(reverse_list([1, 2, 3, 4, 5]))
