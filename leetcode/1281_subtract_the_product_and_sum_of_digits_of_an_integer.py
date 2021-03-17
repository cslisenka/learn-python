class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_digits = 1
        sum_digits = 0

        for digit in str(n):
            int_digit = int(digit)
            product_digits *= int_digit
            sum_digits += int_digit

        return product_digits - sum_digits


s = Solution()
print(s.subtractProductAndSum(234))
print(s.subtractProductAndSum(4421))
