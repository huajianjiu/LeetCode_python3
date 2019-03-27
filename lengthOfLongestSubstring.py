“”“
并不需要找出所有的substring, 只要找不含重复字符的最长substring
可以通过在没有重复字符的时候重复扩展window来截取
并且，在window右端碰到重复字符的时候，将左端修正在这个字符上一次出现的位置后面
并且，并不需要重新建立window
”“”
# 68ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        longest = 0
        seen = {} #char:pos
        while start < len(s) and end < len(s):
            if s[end] in seen:
                if seen[s[end]] > start:
                    start = seen[s[end]]
            length = end - start + 1
            if length > longest:
                longest = length
            seen[s[end]] = end + 1
            end += 1
        return longest
        
"""
56ms by q463746583
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substr = ""
        for c in s:
            if c not in substr:
                substr += c
            else:
                if len(substr) > longest:
                    longest = len(substr) 
                substr = substr[(substr.find(c) + 1):] + c
        if len(substr) > longest:
                    longest = len(substr) 
        return(longest)
"""
