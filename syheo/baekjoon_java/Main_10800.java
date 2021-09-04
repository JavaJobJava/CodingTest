package syheo.baekjoon_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

/**
 * solved.ac
 * 백준
 * 10800
 * 컬러볼
 * 정렬 , 구현
 * 골드 3
 * 아이디어 :
 * 공의 무게->색깔로 오름차순 정렬 후에
 * 색깔별 공의 무게의 누적합을 저장하는 배열의 값을 통해 정답 배열을 계산하여 채워나간다.
 * 색깔이 바뀌는 경우, 무게가 바뀌는 경우를 분기로 설정하여 현재 무게 및 색깔을 설정한다.
 * **/

public class Main_10800 {

    static class Ball implements Comparable<Ball>{
        int num;
        int weight;
        int color;

        public Ball(int num, int weight, int color) {
            this.num = num;
            this.weight = weight;
            this.color = color;
        }

        @Override
        public int compareTo(Ball o) {
            if(this.weight > o.weight){
                    return 1;
            }
            else if(this.weight < o.weight){
                return -1;
            }
            else{
                return Integer.compare(this.color, o.color);
            }
        }

        @Override
        public String toString() {
            return "Ball{" +
                    "num=" + num +
                    ", weight=" + weight +
                    ", color=" + color +
                    '}';
        }
    }

    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static List<Ball> balls = new ArrayList<Ball>();
    static int N;
    static int[] answers;
    static int[] colorSums;

    public static void main(String[] args) throws IOException {

        // 1. input
        N = Integer.parseInt(input.readLine());
        for (int i = 0; i < N; i++) {
            tokens = new StringTokenizer(input.readLine());
            int color = Integer.parseInt(tokens.nextToken());
            int weight = Integer.parseInt(tokens.nextToken());
            balls.add(new Ball(i,weight,color));
        }

        // 2. sort 오름차순
        Collections.sort(balls);
        balls.stream().forEach(ball -> System.out.println(ball.toString()));

        // 3. Allocate array
        answers = new int[N+1];
        colorSums = new int[N+1];

        //4. save weight sum
        int weightSum = 0;
        int nowWeight = balls.get(0).weight;
        int nowColor = balls.get(0).color;
        int nowColorSum = 0;
        int nowWeightSum = 0;
        boolean isChanged = false;
        for (int i = 0; i < N; i++) {
            isChanged = false;
            //무게가 바뀐 경우
            if(isWeightChanged(nowWeight,balls.get(i).weight)){
                // 현재 무게값 초기화
                weightSum += nowWeightSum;
                nowWeight = balls.get(i).weight;
                nowWeightSum = balls.get(i).weight;
                // 현재 색깔값 초기화
                colorSums[nowColor]+=nowColorSum;
                nowColor = balls.get(i).color;
                nowColorSum = balls.get(i).weight;
                isChanged = true;
            }
            else{
                nowWeightSum += balls.get(i).weight;
            }
            answers[balls.get(i).num] = weightSum - colorSums[balls.get(i).color];
            //무게가 바뀌지 않은 경우에만 체크
            if(!isChanged){
                //색깔이 바뀌었을 경우
                if(isColorChanged(nowColor,balls.get(i).color)){
                    colorSums[nowColor]+=nowColorSum;
                    nowColor = balls.get(i).color;
                    nowColorSum = balls.get(i).weight;
                }
                else{
                    nowColorSum += balls.get(i).weight;
                }
            }

        }

        // 5. print
        for (int i = 0; i < N; i++) {
            System.out.println(answers[i]);
        }


    }

    private static boolean isWeightChanged(int nowWeight, int weight) {
        return nowWeight != weight;
    }

    private static boolean isColorChanged(int nowColor, int color) {
        return nowColor != color;
    }
}
