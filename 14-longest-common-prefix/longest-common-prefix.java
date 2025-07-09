
    class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        int minLen = Integer.MAX_VALUE;
        for (String s : strs) {
            if (s.length() < minLen) minLen = s.length();
        }
        if (minLen == 0) return "";
        int low = 0, high = minLen;
        while (low < high) {
            int mid = (low + high + 1) / 2;  
            if (isCommonPrefix(strs, mid)) {
                low = mid;  
            } else {
                high = mid - 1;  
            }
        } 
        return strs[0].substring(0, low);
    }
    private boolean isCommonPrefix(String[] strs, int len) {
        String prefix = strs[0].substring(0, len);
        for (int i = 1; i < strs.length; i++) {
            if (!strs[i].startsWith(prefix)) return false;
        }
        return true;
    }
}
