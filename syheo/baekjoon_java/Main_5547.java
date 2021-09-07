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
 * 5547
 * 일루미네이션
 * 실버1
 * BFS
 * 아이디어 :
 * 처음엔 빌딩을 기준으로 bfs를 돌려서 감싸져 있는 빈 공간에 대한 처리를 하려다가
 * 빈 공간이 1개일 경우만 고려해서 실패
 * 다음 아이디어 :
 * 테두리를 모두 0 으로 초기화 시키고 0,0 위치에서 bfs 를 실행하여
 * 빌딩을 만나면 cnt 를 1 증가시켜서 답을 구함.
 */

public class Main_5547 {

    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static int W,H;
    static int cnt = 0;
    static int[] dx = {-1,-1,0,1,1,0,-1,-1,0,1,1,0}; //row 기준 0~5 홀수 일 떄 , 6~11 짝수 일 때
    static int[] dy = {0,1,1,1,0,-1,-1,0,1,0,-1,-1};
    static int[][] maps;
    static boolean[][] visited;
    static int[][] dp;
    static Queue<Point> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        // 1. input
        tokens = new StringTokenizer(input.readLine());

        W = Integer.parseInt(tokens.nextToken());
        H = Integer.parseInt(tokens.nextToken());

        maps = new int[H+2][W+2];
        for (int j = 0; j <= W+1; j++) {
            maps[0][j] = 0;
        }
        for (int i = 1; i <= H; i++) {
            tokens = new StringTokenizer(input.readLine());
            maps[i][0]=0;
            for (int j = 1; j <= W; j++) {
                maps[i][j] = Integer.parseInt(tokens.nextToken());
            }
            maps[i][W+1]=0;
        }
        for (int j = 0; j <= W+1; j++) {
            maps[H+1][j] = 0;
        }

        dp = new int[H+2][W+2];
        visited = new boolean[H+2][W+2];
        // 2. calculate sum of light by bfS
        //
        bfs(0,0);


        // 3. print
        System.out.println(cnt);

    }

    private static void bfs(int i, int j) {
        Point p;
        int plus = 0;
        queue.add(new Point(i,j));
        visited[i][j]=true;
        while(!queue.isEmpty()){
            p = queue.poll();
            if (p.x % 2 == 0) {
                plus = 6;
            }
            else{
                plus = 0;
            }
            for (int k = plus; k < plus+6; k++) {
                if(p.x+dx[k]>=0 && p.x+dx[k]<=H+1 && p.y+dy[k]>=0 && p.y+dy[k]<=W+1 && !visited[p.x+dx[k]][p.y+dy[k]]){
                    // 빈 공간이면 queue에 넣어줌
                    if(maps[p.x+dx[k]][p.y+dy[k]]==0){
                        queue.add(new Point(p.x+dx[k],p.y+dy[k]));
                        visited[p.x+dx[k]][p.y+dy[k]] = true;
                    }
                    // 건물을 만나면 카운팅
                    if(maps[p.x+dx[k]][p.y+dy[k]]==1){
                        cnt+=1;
                    }
                }
            }
        }
    }
}
