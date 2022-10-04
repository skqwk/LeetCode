[D. Коровы в стойла](https://contest.yandex.ru/contest/40146/problems/D/)

```Java
import java.util.Arrays;
import java.util.Scanner;

public class Cows {
  private static final Scanner sc = new Scanner(System.in);

  public static void main(String[] args) {
    int[] amount = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    int cows = amount[1];

    int[] stalls = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

    System.out.println(solution(stalls, cows));
  }


  public static int countCowsInStallsWithDistance(int[] stalls, int distance) {
    int prevCow = 0;
    int cows = 1;
    for (int i = 0; i < stalls.length; i++) {
      if ((stalls[i] - stalls[prevCow]) >= distance) {
        cows += 1;
        prevCow = i;
      }
    }

    return cows;
  }


  public static int solution(int[] stalls, int cows) {
    int l = 0;
    int r = stalls[stalls.length - 1];

    while (l < r) {
      int m = (l + r + 1) / 2;
      if (countCowsInStallsWithDistance(stalls, m) >= cows) {
        l = m;
      } else {
        r = m - 1;
      }

    }


    return l;
  }
}
```


