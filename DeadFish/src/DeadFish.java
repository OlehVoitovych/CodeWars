
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
//https://www.codewars.com/kata/51e0007c1f9378fa810002a9

public class DeadFish {
    private int[] res;

    public DeadFish(String data) {
        res = parse(data);
    }

    public static int[] parse(String data) {
        int count = 0;
        List<Integer> resList = new ArrayList<>();

        int i = 0;
        for (char c: data.toCharArray()) {
            switch (c){
                case 'i' -> {i++;}
                case 'd' -> {i--;}
                case 's' -> {i *= i;}
                case 'o' -> {resList.add(i);}

            }
        }

        return resList.stream().mapToInt(Integer::intValue).toArray();
    }

    @Override
    public String toString() {
        return "Deadfish{" +
                "res=" + Arrays.toString(res) +
                '}';
    }
}
