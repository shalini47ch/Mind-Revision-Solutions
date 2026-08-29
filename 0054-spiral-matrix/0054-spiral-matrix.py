class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        top=0
        bottom=n-1
        left=0
        right=m-1
        ans=[]
        while(left<=right and top<=bottom):
            #move from left to right
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            #now move from top to bottom
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1
            #now move from right to left
            if(top<=bottom):
                for i in reversed(range(left,right+1)):
                    ans.append(matrix[bottom][i])
            bottom-=1
            #now at last move from bottom to top
            if(left<=right):
                for i in reversed(range(top,bottom+1)):
                    ans.append(matrix[i][left])
            left+=1
        return ans


       