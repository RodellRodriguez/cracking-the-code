'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

'''
    - Create empty string called compressed
    - current_letter = None
    - current_letter_count = 0
    - i = 0
    - while i < len(str):
        - if not current_letter:
            set current_letter = str[i]
            increse current_letter_count by 1
        - elif str[i] != current_letter:
            - compressed += (current_letter + current_letter_count)
            - current_letter = str[i]
            - current_letter_count = 1
        - else current_letter_count ++
        - i++
    - compressed += (current_letter + current_letter_count)
    return min(len(compressed), len(str))
    - Time Complexity: dependent on the string concatenation
    Can we eliminate string concatenation??

TO-DO: Finish this problem
'''
