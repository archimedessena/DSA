# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum 
# and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 

class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)   
   
   
   
   

# def average(self, salary: List[int]) -> float:
#         m, M, total = math.inf, -math.inf, 0.0
#         for s in salary:
#             m, M = min(m, s), max(M, s)
#             total += s
#         return (total - m - M) / (len(salary) - 2)