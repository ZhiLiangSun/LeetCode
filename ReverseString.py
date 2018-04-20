class ReverseString:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Extended Slices
        # [start : stop : step]
        # a = list(range(0,10))
        # >>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # a[5:10:2]
        # >>> [5,7,9]
        # 如果step = -1，則反轉iterable物件

        return s[::-1]

        # list = []
        # sol = ""
        # for i in s:
        #     list.append(i)
        # for j in range(len(list)):
        #     sol = sol + list[len(list) - 1 - j]
        # return sol

        # return "".join(list(reversed(s)))


answer = ReverseString()
print(answer.reverseString("hello"))
