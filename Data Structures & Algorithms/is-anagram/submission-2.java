class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }

        char[] chars = s.toCharArray();
        java.util.Arrays.sort(chars);
        String sortedStr = new String(chars);
        char[] chars2 = t.toCharArray();
        java.util.Arrays.sort(chars2);
        String sortedStr2 = new String(chars2);

        if (sortedStr.equals(sortedStr2)){
            return true;
        }
        return false;
    }
}
