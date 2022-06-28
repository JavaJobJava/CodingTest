import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_1541 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split("-");

        int answer = 0;

        // 첫 번째 - 보기전까지 다 더하기
        String[] sFirst = input[0].split("\\+");
        for (int i = 0; i < sFirst.length; i++) {
            answer += Integer.parseInt(sFirst[i]);
        }

        for (int i = 1; i < input.length; i++) {
            String[] strings = input[i].split("\\+");
            for (int j = 0; j < strings.length; j++) {
                answer -= Integer.parseInt(strings[j]);
            }
        }

        System.out.println(answer);
    }
}