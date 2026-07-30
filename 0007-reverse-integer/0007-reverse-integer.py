class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31 

        sign = -1 if x < 0 else 1
        x = abs(x)

        reverse_num = 0

        while x != 0:
            digit = x % 10 
            reverse_num = reverse_num * 10 + digit
            x = x // 10

        reverse_num *= sign

        if reverse_num < INT_MIN or reverse_num > INT_MAX:
            return 0

        return reverse_num