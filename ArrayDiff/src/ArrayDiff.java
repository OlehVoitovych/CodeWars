import java.util.*;
import java.util.stream.Collectors;
//https://www.codewars.com/kata/523f5d21c841566fde000009

public class ArrayDiff {

    public static int[] arrayDiff(int[] a, int[] b) {
        /*List<Integer> res = new ArrayList<>();
        if (a.length != 0 && b.length != 0) {
            for (int i = 0; i < b.length; i++) {
                for (int j = 0; j < a.length; j++) {
                    if (b[i] != a[j]) {
                        res.add(a[j]);
                    }
                }
                System.out.println(b[i]);
                System.out.println(res.toString());
            }


            *//*a = new int[res.size()];
            int count = 0;
            for (int i : res) {
                a[count] = i;
                count++;
            }*//*
            return a;
        }
        else {
            return a;
        }*/
        /*if (b.length != 0) {
            if (a.length != 0) {
                List<String> a1 = new ArrayList<>(Arrays.asList((Arrays.toString(a).replaceAll("\\p{Punct}", "")).split(" ")));
                List<String> b1 = new ArrayList<>(Arrays.asList((Arrays.toString(b).replaceAll("\\p{Punct}", "")).split(" ")));
                a1.removeAll(b1);
                if (a1.size() == 0) {
                    return new int[] {};
                } else {
                    return a1.stream().mapToInt(Integer::parseInt).toArray();
                }
            }
            else {return new int[] {};}
        }
        else{return a;}
    }*/
        if (b.length == 0) {return a;}
        if (a.length == 0) {return new int[] {};}
        List<String> a1 = new ArrayList<>(Arrays.asList((Arrays.toString(a).replaceAll("\\p{Punct}", "")).split(" ")));
        List<String> b1 = new ArrayList<>(Arrays.asList((Arrays.toString(b).replaceAll("\\p{Punct}", "")).split(" ")));
        a1.removeAll(b1);
        if (a1.size() == 0) {return new int[] {};}
        return a1.stream().mapToInt(Integer::parseInt).toArray();
    }
}
