class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x >= 0 else -1
        x_str = str(x)[::-1] if x >= 0 else str(-x)[::-1]
        x_int = flag * int(x_str)
        if -2147483648 <= x_int < 2147483648:
            return x_int
        else:
            return 0
