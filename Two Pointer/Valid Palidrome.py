def isPalindrome(s):
    string = s.lower()

    import re
    string = re.sub(r'[^a-zA-Z0-9]', '', string)

    if string == string[::-1]:
        return True
    else:
        return False

isPalindrome(s='"A man, a plan, a canal: Panama"')