class Solution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        TreeSet<Integer> available = new TreeSet<>();
        for (int i = 0; i < k; i++) {
            available.add(i);
        }
        
        PriorityQueue<int[]> busy = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int[] requestsHandled = new int[k];
        int maxHandled = 0;
        
        for (int i = 0; i < arrival.length; i++) {
            int arrivalTime = arrival[i];
            int endTime = arrivalTime + load[i];
            
            while (!busy.isEmpty() && busy.peek()[0] <= arrivalTime) {
                available.add(busy.poll()[1]);
            }
            
            if (available.isEmpty()) {
                continue;
            }
            
            Integer server = available.ceiling(i % k);
            if (server == null) {
                server = available.first();
            }
            
            available.remove(server);
            busy.offer(new int[]{endTime, server});
            requestsHandled[server]++;
            maxHandled = Math.max(maxHandled, requestsHandled[server]);
        }
        
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            if (requestsHandled[i] == maxHandled) {
                result.add(i);
            }
        }
        
        return result;
    }
}
