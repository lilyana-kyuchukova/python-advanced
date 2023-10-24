# adding a non required parameter right_index

def palindrome(word, index, right_index=-1):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] != word[right_index]:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1, right_index - 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
