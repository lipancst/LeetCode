class Solution(object):
    def is_palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        tmp = 0
        while x > tmp:
            tmp = tmp * 10 + x % 10
            x = x / 10
        if x == tmp or x == tmp / 10:
            return True
        else:
            return False
