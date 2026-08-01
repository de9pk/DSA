class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo={}

        def get_best(l:int,r:int)->int:
            if l>r:
                return 0
            if l==r:
                return nums[l]
            if (l,r) in memo:
                return memo[(l,r)]

            
            left_pick=nums[l]+min(get_best(l+2,r),get_best(l+1,r-1))

            right_pick=nums[r]+min(get_best(l+1,r-1),get_best(l,r-2))

            memo[(l,r)]=max(left_pick,right_pick)
            return memo[(l,r)]

        p1_score=get_best(0,len(nums)-1)
        total_score=sum(nums)

        return p1_score>=total_score-p1_score