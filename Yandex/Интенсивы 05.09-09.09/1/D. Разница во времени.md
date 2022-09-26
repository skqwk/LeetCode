[D. Разница во времени](https://contest.yandex.ru/contest/39359/problems/D)

Сортируем, вычитаем, находим минимум.
```Java
package intensive.firstday;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

import static java.lang.Math.abs;

/**
 * Каждые сутки на вокзал прибывает n электричек. По заданному расписанию прибытия электричек
 * определите минимальное время между прибытием двух разных электричек.
 */
public class TimeDifference {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    String schedule = sc.nextLine();
    solution(schedule, n);
  }

  public static long diff(String t1, String t2) {
    int h1 = Integer.parseInt(t1.substring(0,2));
    int m1 = Integer.parseInt(t1.substring(3,5));

    int h2 = Integer.parseInt(t2.substring(0,2));
    int m2 = Integer.parseInt(t2.substring(3,5));

    int minutes1 = h1 * 60 + m1;
    int minutes2 = h2 * 60 + m2;

    int diff = abs(minutes2 - minutes1);
    diff = (diff > 720) ? 1440 - diff : diff;

    return diff;
  }

  public static void solution(String schedule, int n) {
    List<String> times =
        Arrays.stream(schedule.split(" "))
            .sorted()
            .collect(Collectors.toList());

    long minDiff = diff(times.get(0), times.get(n - 1));
    for (int i = 1; i < times.size(); i++) {
      minDiff = Math.min(minDiff, diff(times.get(i), times.get(i - 1)));
    }
    System.out.println(minDiff);
  }
}

```