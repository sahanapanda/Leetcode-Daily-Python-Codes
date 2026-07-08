class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        m = len(s)
        
        # Precompute powers of 10 modulo MOD
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        # Prefix sum of digits and prefix concatenated values
        digit_sums = [0] * (m + 1)
        P = [0] * (m + 1)
        
        # Track the index/count of non-zero digits
        nz_count = [0] * (m + 1)
        
        for i in range(m):
            d = int(s[i])
            digit_sums[i + 1] = digit_sums[i] + d
            if d != 0:
                P[i + 1] = (P[i] * 10 + d) % MOD
                nz_count[i + 1] = nz_count[i] + 1
            else:
                P[i + 1] = P[i]
                nz_count[i + 1] = nz_count[i]
                
        # nxt[i] stores the index of the first non-zero digit >= i
        nxt = [m] * (m + 1)
        last = m
        for i in range(m - 1, -1, -1):
            if s[i] != '0':
                last = i
            nxt[i] = last
            
        # prv[i] stores the index of the last non-zero digit <= i
        prv = [-1] * m
        last = -1
        for i in range(m):
            if s[i] != '0':
                last = i
            prv[i] = last

        ans = []
        for l, r in queries:
            # Find the actual boundaries of non-zero elements within [l, r]
            l_prime = nxt[l]
            r_prime = prv[r]
            
            if l_prime > r_prime or l_prime == m or r_prime == -1:
                ans.append(0)
                continue
            
            # 1. Total sum of digits in the range
            total_sum = digit_sums[r + 1] - digit_sums[l]
            
            # 2. Number of non-zero digits in the range [l_prime, r_prime]
            cnt = nz_count[r_prime + 1] - nz_count[l_prime]
            
            # 3. Form integer x modulo MOD
            x = (P[r_prime + 1] - P[l_prime] * pow10[cnt]) % MOD
            
            # 4. Final answer for the query
            ans.append((x * total_sum) % MOD)
            
        return ans
