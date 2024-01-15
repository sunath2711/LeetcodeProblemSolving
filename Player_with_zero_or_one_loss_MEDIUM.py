class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_dict = {}
        answer = [[],[]]
        first_elements_set = {item[0] for item in matches}
        for i in range(len(matches)):
            if matches[i][1] in lost_dict:
                lost_dict[matches[i][1]]+=1
            else:
                lost_dict[matches[i][1]] = 1
                
        answer[1] = sorted([key for key,value in lost_dict.items() if value == 1])         
        answer[0] = sorted([value for value in first_elements_set if value not in lost_dict.keys()])

        return answer
