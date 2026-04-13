class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        fleets = 0

        cars = [] # [position, speed]

        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars.sort(key=lambda x: x[0], reverse=True)

        for car in cars:
            time = (target - car[0]) / car[1]

            if stack and time <= stack[-1]:
                continue
            elif not stack or time > stack[-1]:
                stack.append(time)
                fleets += 1
        
        return fleets


