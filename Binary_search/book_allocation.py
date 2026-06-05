class Solution:

    def can_allocate(self,A, B, mid):
        count = 0
        book_page = 0
        max_val = 0

        for i in A:
            book_page += i  
            if book_page>= mid:
                count += 1
                max_val = max(max_val,book_page)
                book_page = 0
            if count == B:
                return max_val
        return 0
                
                
    def books(self, A, B):
        
        A.sort()
        left = max(A)
        right = sum(A)
        
        res = -1
        
        while left <= right:
            mid = (left + right)//2
            
            if self.can_allocate(A,B,mid):
                res = self.can_allocate(A,B,mid)
                left = mid + 1
            else:
                right = mid - 1
        return res
    
A = [15, 10, 19, 10, 5, 18, 7]
B = 5

x = Solution()
print(x.books(A,B))