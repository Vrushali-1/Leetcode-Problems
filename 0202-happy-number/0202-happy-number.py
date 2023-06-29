class Solution:

    def getNextNum(self,n:int) -> int:
        product = 1
        addition = 0
        while n:
            temp = n%10
            product = temp * temp
            addition += product
            n = n//10
        return addition

            
    def isHappy(self, n: int) -> bool:
        seen = set()
        number = self.getNextNum(n)
        while number != 1 and number not in seen:
            seen.add(number)
            number = self.getNextNum(number)
            
        return number == 1

        