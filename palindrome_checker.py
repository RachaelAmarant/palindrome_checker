def palindrome_checker():
    word = input('\nEnter a word: ').lower()
    if word == word[::-1]:
        print(f'Palindrome.')
    else:
        print(f'Not a palindrome.')

palindrome_checker()
