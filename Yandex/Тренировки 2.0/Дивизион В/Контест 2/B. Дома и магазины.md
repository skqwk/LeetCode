[Дома и магазины](https://contest.yandex.ru/contest/28738/problems/B)

```Java
package trainings.second;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class HousesAndStores {
  private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  private static final int HOUSE = 1;
  private static final int STORE = 2;

  public static void main(String[] args) throws IOException {

    int[] buildings = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

    System.out.println(solution(buildings));

    // assert solution(new int[] {2, 0, 1, 1, 0, 1, 0, 2, 1, 2}) == 3;
  }

  public static int solution(int[] buildings) {
    int maxDistance = -1;
    for (int i = 0; i < buildings.length; i++) {
      if (buildings[i] == HOUSE) {
        int p1 = i;
        int p2 = i;

        while (p1 < buildings.length && buildings[p1] != STORE) {
          p1 += 1;
        }

        while (p2 > -1 && buildings[p2] != STORE) {
          p2 -= 1;
        }

        if (p2 != -1 && p1 != buildings.length) {
          maxDistance = Math.max(maxDistance, Math.min(p1 - i, i - p2));
        } else if (p2 == -1) {
          maxDistance = Math.max(maxDistance, p1 - i);
        } else {
          maxDistance = Math.max(maxDistance, i - p2);
        }
      }
    }

    return maxDistance;
  }
}
```