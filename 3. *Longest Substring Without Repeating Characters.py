
#http://chaoren.is-programmer.com/posts/42744.html
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l,res,lastAppear=-1,0,[-1]*128
        for r, char in enumerate(s):
            pos=ord(char)
            if lastAppear[pos] >l:
                l = lastAppear[pos]
            else:
                res = max(res,r-l)
            lastAppear[pos]=r
        return res
