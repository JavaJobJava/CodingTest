package syheo.baekjoon_java;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

/**
 * solved.ac
 * 백준
 * 1541
 * 잃어버린 괄호
 * 그리디
 */

public class Main_1541 {

    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static ArrayList<Character> operators = new ArrayList<>();
    static Queue<Integer> numbers = new LinkedList<>();
    static int result;

    public static void main(String[] args) throws IOException {
        // 1. input
        String str = input.readLine();

        int startswith = 0;
        // 2. operators , numbers 추출
        for (int i = 0; i < str.length(); i++) {
            // operator case
            if ('0' > str.charAt(i) || str.charAt(i) > '9') {
                numbers.add(Integer.parseInt(str.substring(startswith,i)));
                operators.add(str.charAt(i));
                startswith = i+1;
            }
        }

        // 2-1. 마지막 숫자 add
        numbers.add(Integer.parseInt(str.substring(startswith,str.length())));

        // 3. 그리디
        // 3-1. 첫 숫자로 초기화.
        result = numbers.poll();

        // 3-2. 연산자 갯수만큼 반복 -> '-'가 분기, '-'를 만나면 다음 '-'를 만나기 전까지 뺌
        int sum = 0;
        boolean isMinus = false;
        for (int i = 0; i < operators.size(); i++) {
            if(operators.get(i)=='-'){
                if(!isMinus){
                    result += sum;
                }
                else{
                    result -= sum;
                }
                isMinus = true;
                sum = numbers.poll();
            }
            else{
                sum += numbers.poll();
            }
        }
        if(!isMinus){
            result += sum;
        }
        else {
            result -= sum;
        }

        //4. print
        System.out.println(result);

    }
}
