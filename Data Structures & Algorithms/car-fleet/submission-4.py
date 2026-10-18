class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        sorted_pos = sorted(zip(position, speed), reverse=True)
        fleet =0
        slowest = 0
        for pos,speed in sorted_pos:
            remain = target - pos
            time = remain/speed

            if time>slowest:
                
                fleet = fleet +1
                slowest = time

        return fleet