import java.util.*;

class Solution {
    public List<List<Integer>> mergeSimilarItems(int[][] items1, int[][] items2) {
        // Use a TreeMap to keep values automatically sorted in ascending order
        Map<Integer, Integer> map = new TreeMap<>();
        
        // Add all weights from the first list of items
        for (int[] item : items1) {
            map.put(item[0], map.getOrDefault(item[0], 0) + item[1]);
        }
        
        // Accumulate weights from the second list of items
        for (int[] item : items2) {
            map.put(item[0], map.getOrDefault(item[0], 0) + item[1]);
        }
        
        // Convert the sorted map entries into the required result format
        List<List<Integer>> result = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            result.add(Arrays.asList(entry.getKey(), entry.getValue()));
        }
        
        return result;
    }
}
