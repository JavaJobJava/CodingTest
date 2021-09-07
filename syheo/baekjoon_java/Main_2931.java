package syheo.baekjoon_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

/**
 * 백준
 * solved.ac
 * 2931
 * 가스관
 * 골드 3
 * 구현
 * 아이디어 : 진짜 쌉구현 문제..
 * 일단 아이디어는 '.'인 곳 중 상하좌우에 1~7 에 해당하는 파이프가 directionMap 을 통해 연결되어 있는 상태로 존재하는지 확인함.
 * 만약 위 경우가 있을 경우 어떤 파이프를 둬야 하는지 확인후 출력 후 종료.
 * */

public class Main_2931 {

    static Map<Integer,List<Integer>> pipes;
    // 1-하,우 2-상,우 3-좌,상 4-좌,하 5-상,하 6-좌,우 7-상,하,좌,우, 8-m, 9-z
    static Map<Integer, List<Integer>> directionMap;
    static int[] dx = {-1,0,1,0};
    static int[] dy = {0,1,0,-1};
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static int R, C;
    static int[][] maps;
    static List<Integer> result = new ArrayList<>();

    public static void main(String[] args) throws IOException {

        // 1. input
        tokens = new StringTokenizer(input.readLine());

        R = Integer.parseInt(tokens.nextToken());
        C = Integer.parseInt(tokens.nextToken());

        maps = new int[R][C];
        for (int i = 0; i < R; i++) {
            String nowRow = input.readLine();
            for (int j = 0; j < C; j++) {
                if (nowRow.charAt(j) == '|') {
                    maps[i][j] = 5;
                } else if (nowRow.charAt(j) == '-') {
                    maps[i][j] = 6;
                } else if (nowRow.charAt(j) == '+') {
                    maps[i][j] = 7;
                } else if (nowRow.charAt(j) == 'M') {
                    maps[i][j] = 8;
                } else if (nowRow.charAt(j) == 'Z') {
                    maps[i][j] = 9;
                } else if (nowRow.charAt(j) == '.') {
                    maps[i][j] = 0;
                } else {
                    maps[i][j] = nowRow.charAt(j) - '0';
                }
            } // for
        } // for

        // 2-1. set directionMap
        directionMap = new HashMap<>();
        directionMap.put(0, Arrays.stream(new int[]{1, 4, 5, 7})
                .boxed()
                .collect(Collectors.toList()));
        directionMap.put(1, Arrays.stream(new int[]{3,4,6,7})
                .boxed()
                .collect(Collectors.toList()));
        directionMap.put(2, Arrays.stream(new int[]{2, 3, 5, 7})
                .boxed()
                .collect(Collectors.toList()));
        directionMap.put(3, Arrays.stream(new int[]{1, 2,6, 7})
                .boxed()
                .collect(Collectors.toList()));

        // 2-2. set pipes
        pipes = new HashMap<>();

        pipes.put(1, Arrays.stream(new int[]{1,2})
                .boxed()
                .collect(Collectors.toList()));
        pipes.put(2, Arrays.stream(new int[]{0,1})
                .boxed()
                .collect(Collectors.toList()));
        pipes.put(3, Arrays.stream(new int[]{0,3})
                .boxed()
                .collect(Collectors.toList()));
        pipes.put(4, Arrays.stream(new int[]{2,3})
                .boxed()
                .collect(Collectors.toList()));
        pipes.put(5, Arrays.stream(new int[]{0,2})
                .boxed()
                .collect(Collectors.toList()));
        pipes.put(6, Arrays.stream(new int[]{1,3})
                .boxed()
                .collect(Collectors.toList()));
        pipes.put(7, Arrays.stream(new int[]{0,1,2,3})
                .boxed()
                .collect(Collectors.toList()));

        // 3. find
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (maps[i][j]==0){
                    result = new ArrayList<>();
                    // 상하좌우 탐색
                    for (int k = 0; k < 4; k++) {
                        int row = i+dx[k];
                        int col = j+dy[k];
                        if(0<=row && row<R && 0<=col && col<C){
                            // 열려있는 파이프 구멍이 있나?
                            if(directionMap.get(k).contains(maps[row][col])){
                                result.add(k);
                            }
                        }
                    }
                    // 정답일 경우
                    if(!result.isEmpty()){
                        // 어떤 파이프인지 고름
                        for (int k = 1; k <= 7; k++) {
                            if(result.equals(pipes.get(k))){
                                char answer='0';
                                if(k<=4){
                                    answer = Integer.toString(k).charAt(0);
                                }
                                else{
                                    if(k==5){
                                        answer = '|';
                                    }
                                    if(k==6){
                                        answer = '-';
                                    }
                                    if(k==7){
                                        answer = '+';
                                    }
                                }
                                System.out.println((i+1)+" "+(j+1)+" "+answer);
                                return ;
                            }
                        }
                    }
                }
            }
        }

    }
}
