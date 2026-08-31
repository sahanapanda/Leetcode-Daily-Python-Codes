class Solution {
    public boolean rotateString(String s, String goal) {
        // Must be the same length, and goal must be a substring of s + s
        return s.length() == goal.length() && (s + s).contains(goal);
    }
}
