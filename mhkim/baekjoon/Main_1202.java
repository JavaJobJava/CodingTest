import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 일이공이 보석 도둑
 */
public class Main_1202 {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        Integer n = Integer.parseInt(st.nextToken());
        Integer k = Integer.parseInt(st.nextToken());

        List<Jewel> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(bf.readLine());
            list.add(new Jewel(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        Integer[] bags = new Integer[k];
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(bf.readLine());
            bags[i] = Integer.parseInt(st.nextToken());
        }

        Comparator<Jewel> reverseComparator = Comparator.comparing(Jewel::getV).reversed();
        list.sort(Comparator.comparing(Jewel::getW).thenComparing(reverseComparator));
        Arrays.sort(bags);

        long answer = 0;
        int j = 0;
        Queue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < k; i++) {
            while (j < n && list.get(j).getW() <= bags[i]) {
                pq.offer(list.get(j).getV());
                j++;
            }

            if (!pq.isEmpty()) {
                answer += pq.poll();
            }
        }

        System.out.println(answer);
    }

    public static class Jewel {
        private Integer w;
        private Integer v;

        public Jewel(Integer w, Integer v) {
            this.w = w;
            this.v = v;
        }

        public Integer getV() {
            return v;
        }

        public Integer getW() {
            return w;
        }
    }
}