[Строительство школы](https://contest.yandex.ru/contest/28730/problems/D)


```Java
package trainings.first;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class SchoolConstruction {
  private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws IOException {
    int amount = Integer.parseInt(br.readLine());
    int[] pupils = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

    System.out.println(solution(amount, pupils));

    //        // TEST
    //        assert solution(4, new int[] {1, 2, 3, 4}) == 3;
    //        assert solution(3, new int[] {-1, 0, 1}) == 0;
    //        assert solution(4, new int[] {-1, -2, -3, -4}) == -3;
  }

  public static int solution(int amount, int[] pupils) {
    return pupils[amount / 2];
  }
}
```
