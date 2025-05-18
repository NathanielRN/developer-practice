import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Solution {
  private static final Comparator<int[]> cmp =
      new Comparator<int[]>() {
        @Override
        public int compare(int[] a, int[] b) {
          return a[0] == b[0] ? (a[1] - b[1]) : (a[0] - b[0]);
        }
      };

  public int[][] employeeFreeTime(int[][][] schedule) {

    List<int[]> list = new ArrayList<>();

    for (int[][] person : schedule) { // O(N), N is the total number of intervals
      for (int[] interval : person) list.add(interval);
    }

    if (list.size() == 0) return new int[0][2];

    Collections.sort(list, cmp); // O(NlgN)
    List<int[]> res = new ArrayList<>();
    int end = list.get(0)[1];

    for (int i = 1; i < list.size(); i++) { // O(N)

      int[] cur = list.get(i);

      if (cur[0] > end) {
        res.add(new int[] {end, cur[0]});
      }

      end = Math.max(end, cur[1]);
    }

    return res.toArray(new int[0][2]);
  }
}
