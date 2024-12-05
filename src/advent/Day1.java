package advent;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Day1 {

    long one(String args) {
        var lines = args.split("\n");

        var left = Arrays.stream(lines).map(l -> l.split("\\s+")[0])
                .map(Integer::parseInt).sorted().toList();
        var right = Arrays.stream(lines).map(l -> l.split("\\s+")[1])
                .map(Integer::parseInt).sorted().toList();

        long res = 0;
        for (int i = 0; i < left.size(); i++) {
            res += Math.abs(left.get(i) - right.get(i));
        }
        return res;
    }

    long two(String args) {
        var lines = args.split("\n");
        var counter = new CounterMap();
        Arrays.stream(lines).map(l -> l.split("\\s+")[1])
                .map(Integer::parseInt)
                .forEach(l -> counter.addNumber(l));

        return Arrays.stream(lines).map(l -> l.split("\\s+")[0])
                .mapToInt(Integer::parseInt)
                .map(l -> counter.keepr.getOrDefault(l, 0)* l)
                .sum();



    }

    class CounterMap {
        Map<Integer, Integer> keepr = new HashMap<>();

        void addNumber(int val) {
            keepr.put(val, keepr.getOrDefault(val, 0) + 1);
        }
    }
}
