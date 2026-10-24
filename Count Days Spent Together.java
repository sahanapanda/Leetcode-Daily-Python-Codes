class Solution {
    // Array storing the number of days in each month for a non-leap year
    private final int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        // Convert all arrival and departure dates to the day of the year (1 - 365)
        int aliceStart = dateToDayOfYear(arriveAlice);
        int aliceEnd = dateToDayOfYear(leaveAlice);
        int bobStart = dateToDayOfYear(arriveBob);
        int bobEnd = dateToDayOfYear(leaveBob);

        // Find the intersection of the two intervals
        int overlapStart = Math.max(aliceStart, bobStart);
        int overlapEnd = Math.min(aliceEnd, bobEnd);

        // Calculate total days in the overlapping interval
        if (overlapStart <= overlapEnd) {
            return overlapEnd - overlapStart + 1;
        }
        
        return 0;
    }

    // Helper method to convert "MM-DD" to a single day number out of 365
    private int dateToDayOfYear(String date) {
        int month = Integer.parseInt(date.substring(0, 2));
        int day = Integer.parseInt(date.substring(3, 5));

        int totalDays = 0;
        // Sum up days of all previous months
        for (int i = 0; i < month - 1; i++) {
            totalDays += daysInMonth[i];
        }
        // Add the days of the current month
        totalDays += day;

        return totalDays;
    }
}
