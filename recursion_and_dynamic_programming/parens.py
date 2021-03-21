'''
Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
of n pairs of parentheses.
EXAMPLE
Input: 3
Output: ( ( () ) ) , ( () () ) , ( () ) () , () ( () ) , () () ()
'''
'''
1. What defines a pair of parentheses?
2. What does it mean for a combination to be valid?

A pair of parentheses means there is an open paren and then a matching closing paren
A valid parentheses means that:
    1. '(' must have a corresponding ')'. Therefore there can't be a '(' left open
    2. You can't have a ')' if there isn't a corresponding '(' already printed

How do we ensure this "correspondence"?

Example: ( ( () ) )   n = 3 so there will be 3 '(' and 3 ')' characters available. What's left is determining the order
open_paren_counter = 3 and closed_paren_counter = 3
((())), ( ( ) () ), ( () ) ()

Success means:
    - open and closed paren counters are both 0
Failure means:
    - attempting to close paren when no opens are available meaning closed_counter < open_counter

1. Start with 1 variable: empty array string. Call helper recursive function w/ following params (valid_parens=[], current_paren='(', open_counter=n-1, closed_counter=n)

Recursive function: 3 params. valid_paren, open_paren_counter, and closed_paren_counter
1. Check base cases:
    - If closed_paren < 0 or open_paren < 0 or closed_paren_counter < open_paren_counter return
    - If closed_paren_counter == open_paren_counter == 0 then append current_paren to valid_parens then return
2. Call recursive func (valid_parens, current_paren+='(', open_counter -=1, closed_counter) if open > 0 and open <= closed
3. Call recursive func (valid_parens, current_paren+=')', open_counter, closed_counter-=1)
'''


def parens(n):
    valid_parens = []
    if n > 0:
        _find_valid_parens(valid_parens, '(', n-1, n)
    return valid_parens

def _find_valid_parens(valid_parens, current_paren, num_open_parens_remaining, num_closed_parens_remaining):
    if num_open_parens_remaining == num_closed_parens_remaining == 0:
        valid_parens.append(current_paren)
        return
    if num_open_parens_remaining > 0:
        _find_valid_parens(valid_parens, current_paren+'(', num_open_parens_remaining-1, num_closed_parens_remaining)
    if num_closed_parens_remaining > 0 and num_closed_parens_remaining > num_open_parens_remaining:
        _find_valid_parens(valid_parens, current_paren+')', num_open_parens_remaining, num_closed_parens_remaining-1)


assert set(parens(3)) == set(['((()))', '(()())','(())()', '()(())', '()()()'])
