class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(subs):
            if len(subs) > 3 or len(subs) == 0:
                return False
            if len(subs) > 1 and subs[0] == '0':
                return False
            if len(subs) >= 3 and int(subs) > 255:
                return False
            return True
        
        def backtrack(current,start,dot_count):
            if dot_count == 3:
                if isValid(s[start:]):
                    answer.append(current+s[start:])
                return
            
            for i in range(start,min(start+3,len(s))):
                if isValid(s[start:i+1]):
                    backtrack(current+s[start:i+1]+".",i+1,dot_count + 1)
                    
        
        answer = []
        backtrack("",0,0)
        return answer