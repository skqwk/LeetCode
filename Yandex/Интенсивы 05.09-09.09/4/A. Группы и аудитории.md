[A. Группы и аудитории](https://contest.yandex.ru/contest/40183/problems/A/)


Используем два указателя
```Java
package intensive.fourthday;

import java.util.Arrays;
import java.util.Scanner;

public class GroupsAndAuditories {
  private static final Scanner sc = new Scanner(System.in);

  public static void main(String[] args) {
    sc.nextLine();
    int[] groups =
        Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    sc.nextLine();
    int[] auditories = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    System.out.println(solution(auditories, groups));
  }

  public static int solution(int[] auditories, int[] groups) {
    Arrays.sort(auditories);
    Arrays.sort(groups);
    int countGroups = 0;
    int p = 0;
    for (int i = 0; i < groups.length; i++) {

      while (p < auditories.length - 1 && groups[i] > auditories[p]) {
        p++;
      }
      if (p == auditories.length) {
        break;
      }

      if (groups[i] <= auditories[p]) {
        countGroups++;
        p++;
      }
    }

    return countGroups;
  }
}

```