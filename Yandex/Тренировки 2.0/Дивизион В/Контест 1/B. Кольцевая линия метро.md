[Кольцевая линия метро](https://contest.yandex.ru/contest/28730/problems/B)

```Java
package trainings.first;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class CircleMetroLine {
  private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws IOException {
    int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    int amountStations = input[0];
    int station1 = input[1];
    int station2 = input[2];

    System.out.println(solution(amountStations, station1, station2));
  }

  public static int solution(int amountStations, int station1, int station2) {
    int diff = Math.abs(station2 - station1);
    return Math.min(diff, amountStations - diff) - 1;
  }
}
```