[D. Сломай палиндром](https://contest.yandex.ru/contest/39359/problems/D)

Поскольку нужно получить минимальную строку - то очевидно, что первый встреченный символ, к-й не равен `'a'`, нужно заменить на `'a'`. Однако, если длина строки нечетная и первый встреченный нами символ не равный `'a'`, окажется в середине, то менять его бесполезно. Поэтому мы разделяем обход справа от середины и обход слева от середины.

Также возможна ситуация, когда вся строка состоит из символов `'a'`, в таком случае надо заменить последний символ.
```Java
package intensive.firstday;

import java.util.Scanner;

public class BreakPalindrome {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String palindrome = sc.nextLine();
    System.out.println(solution(palindrome));
  }

  public static String solution(String palindrome) {
    String result = "";
    if (palindrome.length() == 1 || palindrome.equals("")) {
      return result;
    }

    int len = palindrome.length();
    int rightBound = len / 2;

    for (int i = 0; i < rightBound; i++) {
      char c = palindrome.charAt(i);
      if (c != 'a') {
            result = palindrome.substring(0, i) + 'a' + palindrome.substring(i + 1, len);
            return result;
      }
    }

    int leftBound = len % 2 != 0 ? len / 2 + 1 : len / 2;
    for (int i = leftBound; i < len; i++) {
      char c = palindrome.charAt(i);
      if (c != 'a') {
        result = palindrome.substring(0, i) + 'a' + palindrome.substring(i + 1, len);
        return result;
      }
    }

    result = palindrome.substring(0, len - 1) + "b";

    return result;
  }
}


```