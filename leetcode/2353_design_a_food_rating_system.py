from sortedcontainers import SortedSet


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_raiting = {}
        self.cuisine_food = defaultdict(SortedSet)
        self.food_cuisine = {}

        for i in range(len(foods)):
            self.food_raiting[foods[i]] = ratings[i]
            self.cuisine_food[cuisines[i]].add((-ratings[i], foods[i]))
            self.food_cuisine[foods[i]] = cuisines[i]

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        self.cuisine_food[cuisine].remove((-self.food_raiting[food], food))
        self.cuisine_food[cuisine].add((-newRating, food))
        self.food_raiting[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_food[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
