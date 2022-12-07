class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        if start > destination:
            return self.distanceBetweenBusStops(distance, destination, start)

        return min(sum(distance[start:destination]), sum(distance[destination:]) + sum(distance[:start]))
