import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);

        return kSum(nums, 0, 4, target);
    }

    public List<List<Integer>> kSum(int[] nums, int start, int k, int target) {
        List<List<Integer>> res = new ArrayList<>();

        if (start == nums.length || nums[start] * k > target || nums[nums.length - 1] * k < target) {
            return res;
        }

        if (k == 2) {
            return twoSum(nums, target, start);
        }

        for (int i = start; i < nums.length; ++i) {
            if (i == start || nums[i - 1] != nums[i]) {
                for (var set : kSum(nums, i + 1, k - 1, target - nums[i])) {
                    res.add(new ArrayList<>(Arrays.asList(nums[i])));
                    res.get(res.size() - 1).addAll(set);
                }
            }
        }
        return res;
    }

    public List<List<Integer>> twoSum(int[] nums, int target, int start) {
        List<List<Integer>> res = new ArrayList<>();

        int low = start, high = nums.length - 1;

        while (low < high) {
            int sum = nums[low] + nums[high];

            if (sum < target || (low > start && nums[low] == nums[low - 1])) {
                ++low;
            } else if (sum > target || (high < nums.length - 1 && nums[high] == nums[high + 1])) {
                --high;
            } else {
                res.add(Arrays.asList(nums[low], nums[high]));
                ++low;
                --high;
            }
        }
        return res;
    }
}