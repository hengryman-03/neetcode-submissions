class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> set1 = new HashSet<>();
        
        for (int num : nums) {
            // set.add() returns false if the element is already present
            if (!set1.add(num)) {
                return true;
            }
        }
        
        return false;
    }
}