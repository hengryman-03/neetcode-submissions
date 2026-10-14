class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        

        n = len(boxes)

        ans = [0] * n

        balls = 0
        moves = 0

        for i in range(len(boxes)):
            ans[i] += moves

            if boxes[i] == "1":
                balls += 1

            moves += balls
        
        print(ans)

        balls = 0   
        moves = 0

        for i in range (len(boxes)-1, -1, -1):
            ans[i] += moves
            if boxes[i] == "1":
                balls += 1

            moves += balls

        return ans