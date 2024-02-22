# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1
        ppl_who_trust = []
        trusted_ppl = {}
        for i in range(len(trust)):
            ppl_who_trust.append(trust[i][0])
            if trust[i][1] in trusted_ppl:
                trusted_ppl[trust[i][1]]+=1
            else:
                trusted_ppl[trust[i][1]] = 1

        for person, trust_count in trusted_ppl.items():
            if trust_count == n - 1 and person not in ppl_who_trust:
                return person

        return -1
        
   

        
