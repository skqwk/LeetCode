
[A. Два из трех](https://contest.yandex.ru/contest/39714/problems/A)


```Java
package intensive.secondday;

import java.util.Arrays;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

import static java.util.stream.Collectors.toSet;

public class TwoOutOfThree {

    public static void solution() {
        Map<Integer, Integer> count = new TreeMap<>();
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 3; ++i) {
            sc.nextLine();
            Arrays.stream(sc.nextLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .boxed()
                    .collect(toSet())
                    .forEach(
                            n -> {
                                if (!count.containsKey(n)) {
                                    count.put(n, 0);
                                }
                                count.put(n, count.get(n) + 1);
                            });
        }

        count.keySet().stream().filter(k -> count.get(k) > 1).forEach(k -> System.out.print(k + " "));
    }

  public static void main(String[] args) {
            solution();
  }
}

```