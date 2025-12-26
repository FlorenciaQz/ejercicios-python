class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visitados = {}

        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in visitados:
                return [visitados[complemento], i]
            visitados[num] = i

        