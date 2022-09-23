[C. Купить и продать](https://contest.yandex.ru/contest/39359/problems/C)

Здесь нельзя рассматривать цены как абсолютные величины, поскольку мы покупаем на все деньги, удельно. Поэтому надо рассматривать все относительно
```Java
package intensive.firstday;

import java.util.Scanner;

/**
 * У вас есть 1000$, которую вы планируете эффективно вложить. Вам даны цены за 1000 кубометров газа
 * за n дней. Можно один раз купить газ на все деньги в день i и продать его в один из последующих
 * дней j, i < j.
 *
 * <p>Определите номера дней для покупки и продажи газа для получения максимальной прибыли.
 */
public class BuySellStocks {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    int n = Integer.parseInt(sc.nextLine());
    int[] prices = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

    System.out.println(solution(prices, n));
  }

  public static String solution(int[] prices, int n) {
    int buy = 0;
    double profit = 0;

    double maxGas = (double) 1 / prices[0];

    int[] res = new int[] {-1, -1};
    for (int i = 0; i < n; ++i) {
      if (prices[i] * maxGas - 1 > profit) {
        profit = prices[i] * maxGas - 1;
        res[0] = buy;
        res[1] = i;
      }
      if (maxGas < (double) 1 / prices[i]) {
        buy = i;
        maxGas = (double) 1 / prices[i];
      }
    }

    return String.format("%s %s%n", res[0] + 1, res[1] + 1);
  }
}

```