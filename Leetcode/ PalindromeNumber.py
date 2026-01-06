class Solution(object):
    def isPalindrome(self, x):
        cstr = str(x)
        rcstr = cstr[::-1]
        if cstr == rcstr:
            return True
        else:
            return False