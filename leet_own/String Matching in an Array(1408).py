class Solution:
    def stringMatching(self, words):
        l=[]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j] and words[i] not in l:
                    l.append(words[i])
                elif words[j] in words[i] and words[j] not in l:
                    l.append(words[j])
        return l
print(Solution().stringMatching(["mass","as","hero","superhero"]))
#---------------------------------------------------------------------------------
class Solution:
    def stringMatching(self, words):
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break
        return res
print(Solution().stringMatching(["mass","as","hero","superhero"]))
#---------------------------------------------------------------------------------
class Solution:
    def stringMatching(self, words):
        return [word for word in words if any(word in w for w in words if w != word)]
print(Solution().stringMatching(["mass","as","hero","superhero"]))
#---------------------------------------------------------------------------------
class Solution:
    def stringMatching(self, words):
        return sorted({w for word in words for w in words if w != word and w in word})