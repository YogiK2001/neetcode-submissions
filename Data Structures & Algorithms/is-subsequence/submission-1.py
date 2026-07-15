class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        char_indices = {}
        for i, char in enumerate(t):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)

        position = -1
        for char in s:
            if char not in char_indices:
                return False
            indices = char_indices[char]
            idx = self._binarySearch(indices, position)
            if idx == -1:
                return False
            position = indices[idx]
        return True
    
    def _binarySearch(self, arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right)//2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left if left < len(arr) else -1