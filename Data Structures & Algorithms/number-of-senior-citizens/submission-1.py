class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0
        for info in details:
            age = info[11:13]
            print(age)
            age = int(age)
            if age > 60:
                count += 1

        return count