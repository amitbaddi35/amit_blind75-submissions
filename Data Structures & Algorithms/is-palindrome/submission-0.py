class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s)-1
        palindrome = True

        while left <= right:
            print(left, right)
            if not self.is_valid_char(s[left]):
                left += 1
                continue
            
            if not self.is_valid_char(s[right]):
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                continue
            else:
                palindrome = False
                break
        if palindrome:
            print(f'Given String : {s} is palindrome')
            return True
        return False

    def is_valid_char(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')
        )
        

            

        