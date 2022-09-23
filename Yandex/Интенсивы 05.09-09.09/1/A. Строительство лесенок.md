[A. Строительство лесенок](https://contest.yandex.ru/contest/39359/problems/A/)

Рассматриваем через формулу суммы арифметической прогрессии и решаем квадратное уравнение
```Java
import java.util.Scanner;

public class Steps {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    long n = sc.nextLong();
    double i = (Math.sqrt(1 + 8 * n) - 1) / 2;
    i = Math.floor(i);
    int ans = (int) i;
    System.out.println(ans);
  }
}
```