class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A,B = B,A

        left, right = 0, len(A) - 1

        while True:
            Amid = (left + right) // 2
            Bmid = half - Amid - 2

            Aleft = A[Amid] if Amid >= 0 else float('-inf')
            Aright = A[Amid + 1] if Amid + 1 < len(A) else float('inf')
            Bleft = B[Bmid] if Bmid >= 0 else float('-inf')
            Bright = B[Bmid + 1] if Bmid + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Bright,Aright)
                return (max(Aleft,Bleft) + min(Bright,Aright)) / 2
            elif Aleft > Bright:
                right = Amid - 1
            else:
                left = Amid + 1
        


