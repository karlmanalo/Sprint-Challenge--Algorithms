"""
- Your function should take in a single parameter (a string `word`)
- Your function should return a count of how many occurences of 
***"th"*** occur within `word`. Case matters.
- Your function must utilize recursion. It cannot contain any loops.
"""

def count_th(word):
    
    """
    Base case: word is 0 or 1 characters long. Any string that fits 
    this criteria has 0 instances of "th" in it.
    """
    if len(word) <= 1:
        return 0

    # Now our string is guaranteed to be 2 characters or longer.
    else:
        """
        If the first 2 characters of the string are "th", add 1 to our 
        result and recursively call this function on the string, 
        skipping 2 characters (since we found "th" in the first 2 
        characters of the string)
        """
        if word[:2] == "th":
            return 1 + count_th(word[2:])
        
        """
        Otherwise, recursively call this function, skipping 1 character 
        at a time this time.
        """
        return count_th(word[1:])
        
        
