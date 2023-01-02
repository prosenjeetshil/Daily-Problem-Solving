class Solution(object):
    def lengthOfLastWord(self, s):
        wordslist = s.split()
        lastword = wordslist[-1]
        return len(lastword)
