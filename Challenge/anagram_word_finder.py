"""Challenge: Anagram Finder
Problem Statement
Write a Python function called find_anagrams(word_list) that takes a list of words (word_list) as input and returns a list of lists, where each inner list contains words that are anagrams of each other.

Anagram Definition: Two words are anagrams if they contain the same characters in the same frequency, but in a different order (e.g., "listen" and "silent" are anagrams).

Examples
python
Copy
words = ["listen", "silent", "enlist", "google", "inlets", "banana"]
print(find_anagrams(words))
# Output: [["listen", "silent", "enlist", "inlets"], ["google"], ["banana"]]
Hints
Use a dictionary to group words that are anagrams of each other.

Sort the characters of each word to create a unique key for the dictionary.

Iterate through the list of words and group them based on their sorted character keys."""

def find_anagrams(word_list):
    angrem = {}
    for word in word_list:
        sorted_word = ''.join(sorted(word))

        if sorted_word in angrem:
            angrem[sorted_word].append(word)
        else:
            angrem[sorted_word]=[word]
    return list(angrem.values())    


#words = ["listen", "silent", "enlist", "google", "inlets", "banana"]
words = ["listen", "silent", "enlist", "google", "inlets", "banana"]
print(find_anagrams(words))