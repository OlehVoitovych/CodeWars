import java.util.*;
//https://www.codewars.com/kata/5467e4d82edf8bbf40000155

public class DescendingOrder {
    private Object[] sortedNum;

    public DescendingOrder(final int num) {
        this.sortedNum = Arrays.asList(Integer.toString(num).split("")).stream().sorted(Collections.reverseOrder()).toArray();
    }

    @Override
    public String toString() {
        return "DescendingOrder{" +
                "sortedNum=" + Arrays.toString(sortedNum) +
                '}';
    }

    public static int sortDesc(final int num) {
        return Integer.parseInt(Arrays.toString(Arrays.asList(Integer.toString(num).split("")).stream().sorted(Collections.reverseOrder()).toArray()).replace("[", "").replace("]", "").replace(",", "").replace(" ", ""));
    }
}
