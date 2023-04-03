class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)

        i, j = 0, len(people) - 1
        num_boats = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                i += 1

            num_boats += 1

        return num_boats
