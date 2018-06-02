"""Given a large number as string s and an integer k (k <= string length) which
denotes the number of breakpoints we must put in the number, find maximum 
segment value after putting exactly k breakpoints.
Examples:
Input : s = "8754", k = 2
Output : Maximum number = 87
Explanation : After putting the breakpoints, we get
8 75 4
87 5 4
8 5 54

Input : s = "999", k = 1 
Output : Maximum Segment Value = 99
Explanation : After putting the breakpoint, we either get 99,9 or 9,99.

Observations: The max segment value always has len(s) - k integers.
There are (len(s) - (len(s) - k) + 1) or (k + 1) segments to evaluate.
"""

def max_segment_value(s, k):
    if k > len(s):
        return None
    # We need to make sure that the input string contains a valid integer.
    try:
        int(s)
    except ValueError:
        print("The input string does not contain a valid integer. Try again!")
        return None
    seq_len = len(s) - k
    max_value = int(s[: seq_len])
    for i in range(1, len(s) - seq_len + 1):
        current_value = int(s[i : seq_len + i])
        if max_value < current_value:
            max_value = int(s[i : seq_len + i])
    return max_value

if __name__ == "__main__":
    assert max_segment_value("8754", 2) == 87
    assert max_segment_value("999", 1) == 99
    assert max_segment_value("17546898", 3) == 75468