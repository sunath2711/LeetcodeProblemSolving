class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        Stack = []
        for p,s in sorted(pair)[::-1]:
            Stack.append((target - p)/s)
            if len(Stack) >= 2 and Stack[-1] <= Stack[-2]:
                Stack.pop()
        return len(Stack)
        
