class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = 0
        balance = 0
        for value in nums:
            if balance == 0:
                candidate = value
            if value == candidate:
                balance += 1
            else:
                balance -= 1

        return candidate
def main() -> None:
    nums: list[int] = [2, 3, 2, 3, 3, 1, 3, 3]
    sol: Solution = Solution()

    print(sol.majorityElement(nums))
if __name__ == "__main__":
    main()