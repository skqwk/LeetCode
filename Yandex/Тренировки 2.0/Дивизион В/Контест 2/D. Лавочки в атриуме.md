[Лавочки в атриуме](https://contest.yandex.ru/contest/28738/problems/D)
package trainings.second;

```Java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BenchesInTheAtrium {
  private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws IOException {
    int[] input = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    int benchLength = input[0];

    int[] selectedBlocks =
        Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

    int[] ans = solution(benchLength, selectedBlocks);

    if (ans.length == 2) {
      System.out.printf("%s %s\n", ans[0], ans[1]);
    } else {
      System.out.println(ans[0]);
    }

    //    System.out.println(Arrays.toString(solution(5, new int[] {0, 2})));
    //    System.out.println(Arrays.toString(solution(13, new int[] {1, 4, 8, 11})));
    //    System.out.println(Arrays.toString(solution(14, new int[] {1, 6, 8, 11, 12, 13})));
  }

  public static int[] solution(int benchLength, int[] selectedBlocks) {
    int[] blocks = new int[benchLength];
    for (int selectedBlock : selectedBlocks) {
      blocks[selectedBlock] = 1;
    }

    int left = (blocks.length - 1) / 2;
    int right = blocks.length / 2;
    int chosenLeft = 0;
    int chosenRight = 0;
    boolean isLeftChosen = false;
    boolean isRightChosen = false;
    for (int i = 0; i < blocks.length / 2; ++i) {
      if (blocks[left] == 1 && !isLeftChosen) {
        chosenLeft = left;
        isLeftChosen = true;
      }
      if (blocks[right] == 1 && !isRightChosen) {
        chosenRight = right;
        isRightChosen = true;
      }

      left -= 1;
      right += 1;
    }

    return chosenLeft == chosenRight ? new int[] {chosenLeft} : new int[] {chosenLeft, chosenRight};
  }
}
```
