class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        new = []

        for i in range(len(position)):
            curr = (position[i], speed[i])
            new.append(curr)

        new = sorted(new, key=lambda x : x[0])

        stack = []

        for key in new:
            time = (target - key[0]) / key[1]
            while stack and time > stack[-1]:
                stack.pop()
            stack.append(time)

        return len(set(stack))