import java.util.*;
public class MorseCodeDecoder {
    public static String decode(String morseCode) {
        List<String> s = Arrays.asList(morseCode.split("\\s\\s\\s"));
        List<List<String>> ss = new ArrayList<>();
        s.forEach((w) -> {ss.add(Arrays.asList(w.split(" ")));});
        ss.forEach((w) -> {for (int i = 0; i < w.size(); i++) {w.set(i, getCharFromMorse(w.get(i)));}});
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < ss.size(); i++) {for (String l:ss.get(i)) {res.append(l);}res.append(" ");}
        while (res.charAt(0) == ' ') {res.deleteCharAt(0);}
        res.deleteCharAt(res.length()-1);

        return res.toString();

    }

    //without MorseCode.get(code);
    private static String getCharFromMorse(String inputString){
        Map<String, String> morse = new HashMap<>();
        morse.put("A", ".-");
        morse.put("B", "-...");
        morse.put("C",  "-.-.");
        morse.put("D",  "-..");
        morse.put("E",    ".");
        morse.put("F", "..-.");
        morse.put("G",  "--.");
        morse.put("H", "....");
        morse.put("I",   "..");
        morse.put("J", ".---");
        morse.put("K",   "-.-");
        morse.put("L", ".-..");
        morse.put("M",   "--");
        morse.put("N",   "-.");
        morse.put("O",  "---");
        morse.put("P", ".--.");
        morse.put("Q", "--.-");
        morse.put("R", ".-.");
        morse.put("S",  "...");
        morse.put("T",  "-");
        morse.put("U",  "..-");
        morse.put("V", "...-");
        morse.put("W",  ".--");
        morse.put("X", "-..-");
        morse.put("Y", "-.--");
        morse.put("Z", "--..");
        morse.put("1", ".----");
        morse.put("2","..---");
        morse.put("3", "...--");
        morse.put("4", "....-");
        morse.put("5", ".....");
        morse.put("6", "-....");
        morse.put("7", "--...");
        morse.put("8", "---..");
        morse.put("9", "----.");
        morse.put("0", "-----");
        morse.put("SOS", "...---...");
        morse.put(".", ".-.-.-");
        morse.put("!", "-.-.--");

        for (Map.Entry<String, String> entry : morse.entrySet()) {
            if (entry.getValue().equals(inputString)) {
                return entry.getKey();
            }

        }
        return "";


    }
}
