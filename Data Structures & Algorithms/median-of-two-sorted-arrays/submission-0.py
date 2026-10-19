class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        n = len(nums1)
        m = len(nums2)

        right = m
        A, B = nums2,nums1
        if m > n:
            A,B = nums1,nums2
            right = n

        left = 0
        
        while left <= right:

            count_of_A = (left+right)//2

            count_of_B = ((m+n+1)//2) - count_of_A

            ALeft = A[count_of_A - 1] if count_of_A!=0 else float('-inf')
            ARight = A[count_of_A] if count_of_A != len(A) else float('inf')

            BLeft = B[count_of_B - 1] if count_of_B!=0 else float('-inf')
            BRight = B[count_of_B] if count_of_B != len(B) else float('inf')

            if ALeft <=BRight and BLeft<=ARight:
                if (m+n)%2 ==0:
                   return (max(ALeft,BLeft) + min(ARight,BRight))/2

                return max(ALeft,BLeft)

            elif ALeft > BRight:
                right = count_of_A -1

            else:
                left = count_of_A + 1

        return -1



