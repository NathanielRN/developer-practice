class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def timepoints_diff(tp0, tp1):
            h0, m0 = tp0
            h1, m1 = tp1

            return (h1 - h0) * 60 + (m1 - m0)

        # O(n)
        parsed_tp = []
        for tp in timePoints:
            # parse hour + parse minute
            hour = int(tp[:2])
            minute = int(tp[3:])
            parsed_tp.append((hour, minute))

        # O(n log(n))
        # parsed_tp.sort(key=cmp_to_key(timepoints_diff))
        parsed_tp.sort()

        parsed_tp.append((parsed_tp[0][0] + 24, parsed_tp[0][1]))

        min_diff: int = 60 * 24
        # debug = []
        for i, ptp in enumerate(parsed_tp):
            diff = timepoints_diff(parsed_tp[i - 1], ptp)
            # debug.append((parsed_tp[i - 1], ptp, diff))

            if diff < min_diff and diff >= 0:
                min_diff = diff

        # return debug
        return min_diff
