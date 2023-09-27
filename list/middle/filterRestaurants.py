# 餐厅过滤器
# https://leetcode.cn/problems/filter-restaurants-by-vegan-friendly-price-and-distance/description/?envType=daily-question&envId=2023-09-27
from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        restaurants.sort(key=lambda x:(-x[1], -x[0]))
        result = []
        for id, _, vegan, price, distance in restaurants:
            if vegan >= veganFriendly and price <= maxPrice and distance <= maxDistance:
                result.append(id)
        return result


restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]]
veganFriendly = 1
maxPrice = 50
maxDistance = 10

s = Solution()
assert s.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance) == [3, 1, 5]
