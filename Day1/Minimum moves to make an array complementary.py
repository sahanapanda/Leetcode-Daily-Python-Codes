#Minimum moves to make an array complementary

class Solution:
    def minMoves(self, nums, limit):

        n = len(nums)

        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):

            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            pair_sum = a + b

            # default = 2 moves
            diff[2] += 2

            # 1 move range starts
            diff[low] -= 1

            # 0 move at exact sum
            diff[pair_sum] -= 1
            diff[pair_sum + 1] += 1

            # back to 2 moves
            diff[high + 1] += 1

        ans = float('inf')
        curr = 0

        for s in range(2, 2 * limit + 1):

            curr += diff[s]
            ans = min(ans, curr)

        return ans
