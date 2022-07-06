#Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
    


class Solution:
    def countOdds(self, low: int, high: int) -> int:
      return (high-low+1)//2+(high%2+low%2)//2



test = Solution()
test1 = test.countOdds(3, 7)
print(test1)