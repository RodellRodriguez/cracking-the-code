'''
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
'''

'''
pale: p:1, a:1 , l:1, e:1
ple: p:1, l:1, e:1
missing: a:1

Create two hash tables that counts the letters of each string
So we if we compare the hash tables to each other, only 1 letter's counts should be off by 1
This addresses 1 insert/remove away but what about one replacement away?

pale: p:1, a:1, l:1, e:1
bale: b:1, a:1, l:1, e:1


Solution:
    - Return False if the lengths of both strings differ by more than 1
    - If the legnths of both strings differ by 1 then we're looking for a insert/remove operation
        - Loop through the smaller string and check the value of the chars in both strings for each index
            - If the chars are ever different then compare the smaller_string[i:end] == longer_string[i+1:end]
                - if not equal then return False otherwise return True
    - Else if the lengths of both strings are the same then we're looking for a replacement
        - If the chars are ever different then compare the smaller_string[i+1:end] == longer_string[i+1:end]
            - if not equal then return False otherwise return True


TO-DO: Finish this problem
'''
