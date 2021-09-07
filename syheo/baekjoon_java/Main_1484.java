package syheo.baekjoon_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.LinkedList;

/**
 * solved.ac
 * 백준
 * 1484
 * 다이어트
 * 투 포인터
 * 골드 4
 * 아이디어 :
 * 일단 문제를 보고 어느 뽀인트에서 투 포인터 알고리즘을 생각해야 될까?
 * G 의 정의가 현재 몸무게의 제곱에서 이전 몸무게의 제곱을 뺀 값이다.
 * 그렇다면 현재 몸무게의 후보군(범위)과 이전 몸무게의 후보군(범위)에 대해서 모두 완전 탐색해야 될 것이다.
 * 하지만 그러면 너무 비용이 크다. 비용을 줄이기 위해
 * O(N) 시간 복잡도를 가지는 투 포인터를 통해서 접근하면 문제를 쉽게 해결 할 수 있을 것이다.
 * 그리고 몸무게의 범위를 알아야 한다. 일단 최솟값은 1일 테고(몸무게니깐 ; )
 * 최댓값은 (50000^2-49999^2)=99999 의 경우인데 이거를 어떻게 찾을까 ㅋ
 */

public class Main_1484 {

    static int G; //100,000 보다 작거나 같은 자연수
    static final int MinWeight = 1;
    static final int MaxWeight = 100000;
    static int start;
    static int end;
    static int value;
    static LinkedList<Integer> weights = new LinkedList<>();
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    static int calculate(int start, int end) {
        return (int) (Math.pow(end, 2) - Math.pow(start, 2));
    }

    public static void main(String[] args) throws IOException {
        // 1. input
        G = Integer.parseInt(input.readLine());

        // 2. start two pointer algorithm
        start = MaxWeight - 1;
        end = MaxWeight;

        // end가 MinWeight 이 될때까지
        while (end != MinWeight) {
            value = calculate(start, end); // 계산 결과
            if(start == end){ //같아지면 start --
                start--;
                continue;
            }

            if (value == G) { // 정답 조건
                weights.add(end);
                start--;
                end--;
            } else if (value > G) {
                end--;
            } else {
                if (start > MinWeight) start--;
                else break; // start 가 MinWeight인데도 value가 작다? 이제 답 없음.
                // else end--; // 이거 안해도될듯?
            }
        }

        Collections.sort(weights);

        if(weights.isEmpty()){
            System.out.println(-1);
        }
        for (int i = 0; i < weights.size(); i++) {
            System.out.println(weights.get(i));
        }


    }
}
