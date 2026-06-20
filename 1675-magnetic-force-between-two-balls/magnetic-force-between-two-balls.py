class Solution:
    def maxDistance(self, position: List[int], m: int):

        position.sort()

        def isPossible(position, m, dist):

            balls = 1
            last = position[0]

            for i in range(1, len(position)):

                if position[i] - last >= dist:
                    balls += 1
                    last = position[i]

                if balls >= m:
                    return True

            return False

        s = 1
        e = position[-1] - position[0]

        ans = 0

        while s <= e:

            mid = (s + e) // 2

            if isPossible(position, m, mid):
                ans = mid
                s = mid + 1
            else:
                e = mid - 1

        return ans