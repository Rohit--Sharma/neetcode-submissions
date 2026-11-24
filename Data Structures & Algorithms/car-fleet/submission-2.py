class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speeds = []
        for p, s in zip(position, speed):
            pos_speeds.append((p, s))
        pos_speeds.sort(key=lambda x: x[0], reverse=True)
        # print(pos_speeds)

        ans = 0
        prev_time = -1
        for p, s in pos_speeds:
            time_to_tgt = (target - p) / s
            # print(p, s, time_to_tgt, prev_time)
            if prev_time >= time_to_tgt:
                # Part of the same fleet
                pass
            else:
                # Count new fleet
                prev_time = time_to_tgt
                ans += 1

        return ans