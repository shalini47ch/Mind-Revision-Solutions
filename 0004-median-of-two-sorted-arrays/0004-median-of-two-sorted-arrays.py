class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums1)>len(nums2)):
            #so here we perform the swap
            nums1,nums2=nums2,nums1
        A=nums1
        B=nums2
        n=len(A)
        m=len(B)
        half=(n+m+1)//2
        left=0
        right=n
        while(left<=right):
            i=left+(right-left)//2
            j=half-i
            #Left is for max value and right is for minval
            Aleft=A[i-1] if i>0 else -sys.maxsize
            Aright=A[i] if i<n else sys.maxsize
            Bleft=B[j-1] if j>0 else -sys.maxsize
            Bright=B[j] if j<m else sys.maxsize
            #now deciding the half and calculating the median accordingly
            if(Aleft<=Bright and Bleft<=Aright):
                if(n+m)%2==1:
                    return max(Aleft,Bleft)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2.0
            elif(Aleft>Bright):
                right=i-1
            else:
                left=i+1
        


        