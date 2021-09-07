package syheo.baekjoon_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * solved.ac
 * 백준
 * 12927
 * 배수 스위치
 * 그리디
 * 실버 4
 * 아이디어 :
 * 켜진 전구 중 번호가 제일 작은 전구부터 끈다.
 * 의문 :
 * 근데 이거 무조건 다 끌 수 있지 않나? 못 끄는 경우는 없는 것 같다.
 */

public class Main_12927 {

    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static String inputLights;
    static int answer = 0;
    static int minIdx = 1;
    static boolean[] lights;

    public static void main(String[] args) throws IOException {

        //1. input
        inputLights = input.readLine();
        lights = new boolean[inputLights.length()+1];
        for (int i = 0; i < inputLights.length(); i++) {
            if (inputLights.charAt(i) == 'N') {
                lights[i+1] = false;
            } else {
                lights[i+1] = true;
            }
        }

        //2. 제일 작은 숫자부터 스위치 끄기
        while(minIdx < lights.length){
            if(lights[minIdx]==true){
                for (int i = minIdx; i < lights.length; i+=minIdx) {
                    lights[i] = !lights[i];
                }
                answer++;
            }
            minIdx++;
        }

        System.out.println(answer);

    }
}
