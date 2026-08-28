
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> results = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int compli = target - nums[i];
            
            if (results.containsKey(compli)) {
                // Return a primitive int array containing the two indices
                return new int[]{ results.get(compli), i };
            } else {
                results.put(nums[i], i);
            }
        }
        
        // Default return if no solution is found
        return new int[]{};
    }
}