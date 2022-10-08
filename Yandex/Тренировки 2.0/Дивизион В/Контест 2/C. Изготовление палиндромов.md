[Изготовление палиндромов](https://contest.yandex.ru/contest/28738/problems/С)

```Java
package trainings.second;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class MakingPalindromes {

  private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws IOException {
    String s = br.readLine();
    System.out.println(solution(s));

//    assert solution("a") == 0;
//    assert solution("ab") == 1;
//    assert solution("abc") == 1;
//    assert solution("aba") == 0;
//    assert solution("cognitive") == 4;
//    assert solution("aabbbbcc") == 2;

  }

  public static int solution(String s) {

    int left, right;
    int len = s.length();
    left = len / 2 - 1;
    right = len % 2 == 0 ? len / 2 : len / 2 + 1;

    int cost = 0;
    for (int i = 0; i < len / 2; ++i) {
      cost += s.charAt(left) != s.charAt(right) ? 1 : 0;
      left -= 1;
      right += 1;
    }

    return cost;
  }
}
```