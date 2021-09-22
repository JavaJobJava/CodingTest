package syheo.baekjoon_java;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * 백준
 * solved.ac
 * 17090
 * 미로 탈출하기
 * 골드 2
 * 아이디어 :
 * 방문하지 않은 노드에 대해서 dfs를 돈다.
 * dfs에서 탈출조건은
 * 1. 범위 밖으로 이탈했을 경우
 * 2. dp[row][col] 이 0보다 클 경우 ( 이전에 탈출 경로를 지나친 경우 )
 * 그외에 싸이클을 발견했을 경우 즉, 방문했던 노드를 또 지나는 경우에
 * 해당 경로의 방문처리를 취소한다.
 * */

//U인 경우에는 (r-1, c)로 이동해야 한다.
//R인 경우에는 (r, c+1)로 이동해야 한다.
//D인 경우에는 (r+1, c)로 이동해야 한다.
//L인 경우에는 (r, c-1)로 이동해야 한다.

public class Main_17090 {

    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static int N,M;
    static String inputStr;
    static char[][] maps;
    static boolean[][] visited;
    static int[][] dp;
    static int cnt = 0;
    static Queue<Point> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        // 1. input
        tokens = new StringTokenizer(input.readLine());
        N = Integer.parseInt(tokens.nextToken());
        M = Integer.parseInt(tokens.nextToken());
        maps = new char[N][M];

        for (int i = 0; i < N; i++) {
            inputStr = input.readLine();
            for (int j = 0; j < M; j++) {
                maps[i][j] = inputStr.charAt(j);
            }
        }

        visited = new boolean[N][M];
        dp = new int[N][M];

        // 2. bfs
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                    if(!visited[i][j]){
                        cnt+=dfs(i,j,0);
                    }
            }
        }

        // 3. print cnt
        System.out.println(cnt);
    }

    private static int dfs(int row, int col,int cnt) {
        // 탈출 체크
        if((row<0 || row>=N) || (col<0 || col>=M) || dp[row][col] >0){
            return cnt;
        }
        // 방문한델 또 방문? -> 싸이클
        if(visited[row][col]){
            return 0;
        }
        // 방문 처리
        else{
            visited[row][col] = true;
        }
        // 방향에 따라 방문
        if(maps[row][col]=='U'){
            cnt=dfs(row-1,col,cnt+1);
        }
        if(maps[row][col]=='D'){
            cnt=dfs(row+1,col,cnt+1);
        }
        if(maps[row][col]=='R'){
            cnt=dfs(row,col+1,cnt+1);
        }
        if(maps[row][col]=='L'){
            cnt=dfs(row,col-1,cnt+1);
        }
        if(cnt == 0)
            visited[row][col] = false;
        else
            dp[row][col] += cnt;



        return cnt;
    }
}
