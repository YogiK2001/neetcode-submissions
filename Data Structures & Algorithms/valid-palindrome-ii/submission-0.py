class Solution:
    def validPalindrome(self, s: str) -> bool:
        new_s = [char.lower() for char in s if char.isalnum()]

        def is_palindrome(i,j):
            while i < j:
                if new_s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        left , right  = 0, len(new_s)-1
        while left < right:
            if new_s[left] != new_s[right]:
                return is_palindrome(left+1, right) or is_palindrome(left, right-1)
            left += 1
            right -= 1
        return True

