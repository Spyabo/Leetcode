def isPalindrome(s):
  s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
  if s == s[::-1]:
    return True
  else:
    return False

isPalindrome(s='"A man, a plan, a canal: Panama"')
