import java.util.Arrays;

class Solution {
    public int minimumPushes(String word) {
        // Step 1: Count frequencies of each character
        int[] freq = new int[26];
        for (char c : word.toCharArray()) {
            freq[c - 'a']++;
        }
        
        // Step 2: Sort frequencies in ascending order
        Arrays.sort(freq);
        
        int totalPushes = 0;
        int distinctLettersProcessed = 0;
        
        // Step 3: Iterate backwards from the highest frequency
        for (int i = 25; i >= 0; i--) {
            if (freq[i] == 0) {
                break; // No more characters left
            }
            
            // Calculate how many pushes this character needs based on its rank
            int multiplier = (distinctLettersProcessed / 8) + 1;
            totalPushes += freq[i] * multiplier;
            
            distinctLettersProcessed++;
        }
        
        return totalPushes;
    }
}
