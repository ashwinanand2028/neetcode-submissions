class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        sorted_cars = sorted(zip(position, speed))
        stack = []

        for pos, sped in sorted_cars:
            time = (target - pos) / sped
            while(stack and time >= stack[-1]):
                stack.pop()
            stack.append(time)
        
        return len(stack)