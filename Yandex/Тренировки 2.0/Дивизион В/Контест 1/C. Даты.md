[Даты](https://contest.yandex.ru/contest/28730/problems/C)

```Java
package trainings.first;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Dates {
  private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws IOException {
    int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    int d = input[0];
    int m = input[1];
    int y = input[2];
    System.out.println(solution(d, m, y));

    //    // TEST
    //    assert solution(1, 1, 2000) == 1;
    //    assert solution(1, 12, 2000) == 0;
    //    assert solution(12, 12, 2000) == 1;
    //    assert solution(13, 12, 2000) == 1;
    //    assert solution(12, 13, 2000) == 1;
    //    assert solution(31, 12, 2000) == 1;
    //    assert solution(10, 12, 2000) == 0;
    //    assert solution(6, 5, 2000) == 0;
    //    assert solution(6, 6, 2000) == 1;
    //    assert solution(1, 2, 2003) == 0;
    //    assert solution(2, 29, 2008) == 1;
  }

  public static int solution(int d, int m, int y) {

    if (d > 12 || m > 12) {
      return 1;
    } else if (d == m) {
      return 1;
    } else {
      return 0;
    }
  }
}
```