class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int num1 = 0;
        int num2 = numbers.length - 1;

        while (num1 < num2){
            if (numbers[num1] + numbers[num2] == target && num1 != num2){
                return new int[]{num1 + 1, num2 + 1};
            } 
            else if (numbers[num1] + numbers[num2] > target ){
                num2--;
            }else{
                num1++;
            }
        }
        return new int[]{};
    }
}
