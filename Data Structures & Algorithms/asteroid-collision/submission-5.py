class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            # We only evaluate collisions when a Right-moving meets a Left-moving
            while stack and stack[-1] > 0 and num < 0:
                if stack[-1] + num < 0:
                    stack.pop()     # Top asteroid destroyed, keep checking
                    continue
                elif stack[-1] + num == 0:
                    stack.pop()     # Both destroyed, stop checking
                break               # New asteroid destroyed, stop checking
            else:
                # This only triggers if the while loop didn't break 
                # (meaning the new asteroid survived)
                stack.append(num)
                
        return stack