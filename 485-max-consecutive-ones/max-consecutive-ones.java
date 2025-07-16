class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max1 = 0;
        int counter = 0;
        for(int i=0;i<=nums.length-1;i++){
            if(nums[i] == 1){
                counter++;
                max1 = Math.max(max1,counter);
            }else{
                counter = 0;
            }
        }
        return max1;
    }
}