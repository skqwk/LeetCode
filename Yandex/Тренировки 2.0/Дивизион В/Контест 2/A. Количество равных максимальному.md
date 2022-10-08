[Количество равных максимальному](https://contest.yandex.ru/contest/28738/problems/A)

```Java
package trainings.second;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class AmountEqualsMax {
  private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws IOException {
    int num = Integer.parseInt(br.readLine());
    List<Integer> nums = new ArrayList<>();
    while (num != 0) {
      nums.add(num);
      num = Integer.parseInt(br.readLine());
    }

    System.out.println(solution(nums));
  }

  public static int solution(List<Integer> nums) {
    int max = -1;
    for (Integer num : nums) {
      max = Math.max(max, num);
    }

    int count = 0;
    for (Integer num : nums) {
      count += num == max ? 1 : 0;
    }

    return count;
  }
}
```