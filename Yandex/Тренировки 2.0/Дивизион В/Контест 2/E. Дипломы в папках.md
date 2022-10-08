[Дипломы в папках](https://contest.yandex.ru/contest/28738/problems/E)

```Java
package trainings.second;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class DiplomasInFolders {
  private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws IOException {
    br.readLine();
    int[] folders = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    System.out.println(solution(folders));
    //    System.out.println(solution(new int[] {2, 1}));
    //    System.out.println(solution(new int[] {80, 5, 7, 5}));
  }

  public static int solution(int[] folders) {
    int time = 0;
    Arrays.sort(folders);
    for (int i = 0; i < folders.length - 1; i++) {
      time += folders[i];
    }

    return time;
  }
}
```