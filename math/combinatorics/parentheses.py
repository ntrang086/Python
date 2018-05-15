def _permute_parentheses(s, open_count, close_count):
    """Accept open_count number of open parentheses, and close_count of close
    parentheses and print out all possible permutations. For 2 parentheses, 
    there are 2 permutations: ()() and (()).
    """
    if open_count == close_count == 0:
        print(s)
    if open_count > 0:
        _permute_parentheses(s + "(", open_count - 1, close_count + 1)
    if close_count > 0:
        _permute_parentheses(s + ")", open_count, close_count - 1)

def permute_parentheses(n):
    """A wrapper function for _permute_parentheses. Accept a number n and call 
    _permute_parentheses to print out all possible permutations. Initialize
    open_count to n.
    """
    _permute_parentheses("", n, 0)

if __name__ == "__main__":
    print ("1 pair")
    permute_parentheses(1)
    print ("2 pairs")
    permute_parentheses(2)
    print ("3 pairs")
    permute_parentheses(3)