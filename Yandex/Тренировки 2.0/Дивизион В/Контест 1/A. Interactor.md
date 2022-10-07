[Interactor](https://contest.yandex.ru/contest/28730/problems/A)

```Java
package trainings.first;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Interactor {
  private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws IOException {
    int programmCode = Integer.parseInt(br.readLine());
    int interactorCode = Integer.parseInt(br.readLine());
    int checkerCode = Integer.parseInt(br.readLine());

    System.out.println(solution(programmCode, interactorCode, checkerCode));
  }

  public static int solution(int programmCode, int interactorCode, int checkerCode) {

    int result;
    if (interactorCode == 4) {
      result = programmCode != 0 ? 3 : 4;
    } else if (interactorCode == 6) {
      result = 0;
    } else if (interactorCode == 7) {
      result = 1;
    } else if (interactorCode == 0) {
      result = programmCode != 0 ? 3 : checkerCode;
    } else if (interactorCode == 1) {
      result = checkerCode;
    } else {
      result = interactorCode;
    }

    return result;
  }
}
```