class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(string, left, right):
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return check_palindrome(s, i + 1, j) or check_palindrome(s, i, j - 1)
                
        return True