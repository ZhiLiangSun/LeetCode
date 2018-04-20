
class PalindromeNumber:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 作法參考Reverse Integer，將x mod 10得到最後一位數字，加入至陣列中
        # 再將x除以10取商。依此類推，最後會得到反轉數字之陣列
        # 陣列之最左邊比對最右邊，第二個比對倒數第二個。依此類推，迴圈次數為陣列長度/2
        sol = []
        if x < 0:
            return False
        while x > 0:
            sol.append(x % 10)
            x //= 10
        for i in range(len(sol) // 2):
            if sol[i] != sol[len(sol) - 1 - i]:
                return False
        return True

        # if x < 0:
        #     return False
        #
        # ranger = 1
        # while x / ranger >= 10:
        #     ranger *= 10
        #
        # while x:
        #     left = x // ranger
        #     right = x % 10
        #     if left != right:
        #         return False
        #
        #     x = (x % ranger) // 10
        #     ranger /= 100
        #
        # return True


ans = PalindromeNumber()
print(ans.isPalindrome(12321))
