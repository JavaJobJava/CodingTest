package syheo.baekjoon_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * solved.ac
 * 백준
 * 1202
 * 보석 도둑
 * 그리디
 * 아이디어 :
 * 가방과 보석을 무게를 기준으로 오름차순 정렬
 * 현재 가방에 담을 수 있는 보석을 우선순위 큐에 넣고
 * 가장 가치가 높은 보석을 담음.
 * 보석과 가방의 갯수가 300,000, 최대 가치가 1,000,000 이므로  최악의 경우 300,000,000,000 이 되므로 long 타입을 써줘야됨.
 * */

public class Main_1202 {

     static class Info implements Comparable<Info>{
        int weight;
        int value;

        public Info(int weight,int value){
            this.weight = weight;
            this.value = value;
        }

         @Override
         public int compareTo(Info info) {
             if(this.weight > info.weight) {
                 return 1; // weight 에 대해서 내림차순
             }
             return -1;
         }
     }


    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static int N, K; // 보석의 갯수, 가방의 갯수
    static ArrayList<Integer> bagWeights = new ArrayList<>(); //가방 무게 리스트
    static ArrayList<Info> jewels = new ArrayList<>(); // 보석 정보 리스트
    static PriorityQueue<Integer> candidates = new PriorityQueue<>(Collections.reverseOrder()); //가방에 담을 보석 우선순위 큐(최대 힙)
    //보석과 가방의 갯수가 300,000, 최대 가치가 1,000,000 이므로  최악의 경우 300,000,000,000 이 되므로 long 타입을 써줘야됨.
    static long result = 0;


    public static void main(String[] args) throws IOException {

        // 1. input
        tokens = new StringTokenizer(input.readLine());
        N = Integer.parseInt(tokens.nextToken());
        K = Integer.parseInt(tokens.nextToken());

        for (int i = 0; i < N; i++) {
            tokens = new StringTokenizer(input.readLine());
            jewels.add(new Info(Integer.parseInt(tokens.nextToken()),Integer.parseInt(tokens.nextToken())));
        }

        for (int i = 0; i < K; i++) {
            bagWeights.add(Integer.parseInt(input.readLine()));
        }

        // 2. sort
        Collections.sort(jewels); // 무게에 대해서 오름차순
        Collections.sort(bagWeights); // 무게에 대해서 오름차순

        int id = 0;
        // 3. 가방에 보석 담기 -> 현재 가방에 담을 수 있는것을 우선순위 큐에 넣음.
        for (int i = 0; i < K; i++) {
            while(id< jewels.size() && jewels.get(id).weight <= bagWeights.get(i)){
                candidates.add(jewels.get(id).value);
                id++;

            }
            if(!candidates.isEmpty()){
                result += candidates.poll();
            }
        }

        // 4. print
        System.out.println(result);
    }
}
