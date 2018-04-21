class LongestSubstring:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Sliding Window
        # 由左到右偵測是否有重複字元，若有重複則找出重複字元之位置(index)，並儲存當前子字串到dictionary
        # 而新的Window將會由index+1開始，依此類推，最後回傳最大之子字串長度
        dic = {}
        tmp = ""
        i = 0
        left = 0
        for key, value in enumerate(s):
            if value not in tmp:
                tmp = tmp + value
            else:
                dic[i] = tmp
                left = left + tmp.index(value) + 1
                tmp = s[left:key + 1]
                i += 1
        dic[i] = tmp
        return len(max(dic.values(), key=len))


ans = LongestSubstring()
print(ans.lengthOfLongestSubstring("abcabcbb"))  # 3
print(ans.lengthOfLongestSubstring("bbbbb"))  # 1
print(ans.lengthOfLongestSubstring("pwwkew"))  # 3
print(ans.lengthOfLongestSubstring("anviaj"))  # 5
print(ans.lengthOfLongestSubstring("abcb"))  # 3
print(ans.lengthOfLongestSubstring("dvdf"))  # 3
print(ans.lengthOfLongestSubstring("asjrgapa"))  # 3
