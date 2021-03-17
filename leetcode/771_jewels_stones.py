class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set()

        for jewel in jewels:
            jewels_set.add(jewel)

        count = 0

        for stone in stones:
            if stone in jewels_set:
                count += 1

        return count


s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))
print(s.numJewelsInStones("z", "ZZ"))
