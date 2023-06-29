class Solution:
    def getdigitSum(self,num) -> int:
        answer = 0
        while num:
            answer += num % 10
            num = num//10
        return answer        

    def maximumSum(self, nums: List[int]) -> int:
        count = defaultdict(int)
        answer = -1

        for num in nums:
            digitSum = self.getdigitSum(num)
            if digitSum in count:
                answer = max(answer,num+count[digitSum])
            count[digitSum] = max(num,count[digitSum])
        return answer