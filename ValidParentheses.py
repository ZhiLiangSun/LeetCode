class ValidParentheses:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 先建立一個括號的字典集（重要！可以減少程式碼行數及可讀性）
        # 運用Stack的概念，若遇到右開口push stack
        # 遇到左開口時，先檢查Stack是否為空，若不為空則pop stack，檢查pop出來之物件是否為其對應之符號
        # 字串讀取完後，檢查stack內是否為空，若為空則True，不為空則False
        stack = []
        dic = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dic.values():
                stack.append(char)
            elif char in dic.keys():
                if stack == [] or dic[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


answer = ValidParentheses()
print(answer.isValid("[{}]()"))
