class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums1)>len(nums2)):
            nums1, nums2 = nums2, nums1
        
        len1 = len(nums1)
        len2 = len(nums2)

        half = (len1+len2+1)//2

        left = -1
        right = len1-1

        while(left<=right):
            print(left, right)
            mid = (left+right)//2
            left1 = nums1[mid] if mid>=0 else -math.inf
            right1 = nums1[mid+1] if(mid+1<len1) else math.inf
            
            rem_elem = half - (mid+1)
            ind = rem_elem - 1

            left2 = nums2[ind] if(ind>=0) else -math.inf
            right2 = nums2[ind+1] if ind+1<len2 else math.inf
            
            if(left1<=right2 and left2<=right1):
                if((len1+len2)%2==1):
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            
            if(left1>right2): 
                right = mid-1
            else:
                left = mid+1
        return -1

            





