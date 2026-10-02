import java.time.LocalDate;
import java.time.format.TextStyle;
import java.util.Locale;

class Solution {
    public String dayOfTheWeek(int day, int month, int year) {
        // Create a LocalDate instance for the given date
        LocalDate date = LocalDate.of(year, month, day);
        
        // Get the full day name in English (e.g., "Friday", "Saturday")
        return date.getDayOfWeek().getDisplayName(TextStyle.FULL, Locale.ENGLISH);
    }
}
