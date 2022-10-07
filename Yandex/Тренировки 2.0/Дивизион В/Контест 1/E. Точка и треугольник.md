[Точка и треугольник](https://contest.yandex.ru/contest/28730/problems/E)

```Java
package trainings.first;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class PointAndTriangle {
  private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

  public static void main(String[] args) throws IOException {
    int d = Integer.parseInt(br.readLine());
    int[] point = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

    System.out.println(solution(d, point[0], point[1]));

//    // TESTS
//    assert solution(5, 1, 1) == 0;
//    assert solution(3, -1, -1) == 1;
//    assert solution(4, 4, 4) == 2;
//    assert solution(4, 2, -1) == 1;
//    assert solution(4, -1, 2) == 1;
//    assert solution(4, 0, 5) == 3;
//    assert solution(4, 2, 2) == 0;
  }

  public static int solution(int d, int xp, int yp) {
    if ((xp >= 0) && (yp >= 0) && (yp <= d - xp)) {
      return 0;
    } else {
      Point p = new Point(xp, yp, 0);

      Point a = new Point(0, 0, 1);
      Point b = new Point(d, 0, 2);
      Point c = new Point(0, d, 3);

      Point[] points = new Point[] {a, b, c};
      Distance[] distances = new Distance[points.length];
      for (int i = 0; i < points.length; i++) {
        distances[i] = calcDistance(p, points[i]);
      }
      Arrays.sort(distances);
      return distances[0].to.name;
    }
  }

  private static Distance calcDistance(Point p1, Point p2) {
    double value = Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));

    return new Distance(p1, p2, value);
  }

  public static class Point {
    int x;
    int y;
    int name;

    public Point(int x, int y, int name) {
      this.x = x;
      this.y = y;
      this.name = name;
    }
  }

  public static class Distance implements Comparable<Distance> {
    Point from;
    Point to;
    double value;

    public Distance(Point from, Point to, double value) {
      this.from = from;
      this.to = to;
      this.value = value;
    }

    @Override
    public int compareTo(Distance o) {
      if (o.value == this.value) {
        return Integer.compare(this.to.name, o.to.name);
      }
      return Double.compare(this.value, o.value);
    }
  }
}
```