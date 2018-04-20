class ReverseInteger:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sol = 0
        if x > 0:
            sign = 1
        else:
            sign = -1

        x = abs(x)
        while x > 0:
            sol = sol * 10 + x % 10
            # "/"：浮點數除法  "//"：整數除法(取商)
            x //= 10
        ans = sol * sign
        return ans if ans.bit_length() < 32 else 0


answer = ReverseInteger()
print(answer.reverse(-123))
