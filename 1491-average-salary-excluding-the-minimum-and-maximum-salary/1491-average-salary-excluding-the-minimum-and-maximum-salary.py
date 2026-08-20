class Solution:
    def average(self, salary: List[int]) -> float:
        mean=0
        max_num=max(salary)
        min_num=min(salary)
        salary.remove(max_num)
        salary.remove(min_num)
        n=len(salary)
        for i in salary:
            mean+=i
        return mean/n
        


        