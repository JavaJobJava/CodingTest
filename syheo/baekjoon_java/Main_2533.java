package syheo.baekjoon_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main_2533 {

    static class Node{
        boolean isEarlyAdapter;
        int parent;
        List<Integer> childNodes;

        public Node(boolean isEarlyAdapter, int parent, List<Integer> childNodes) {
            this.isEarlyAdapter = isEarlyAdapter;
            this.parent = parent;
            this.childNodes = childNodes;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "isEarlyAdapter=" + isEarlyAdapter +
                    ", parent=" + parent +
                    ", childNodes=" + childNodes +
                    '}';
        }
    }

    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static Queue<Integer> queue = new LinkedList<>();
    static int headNum;
    static Node[] nodes;
    static int N;
    static int answer = 0;


    public static void main(String[] args) throws IOException {

        // 1. input
        N = Integer.parseInt(input.readLine());

        nodes = new Node[N+1];
        for (int i = 0; i <= N; i++) {
            nodes[i] = new Node(false,-1,new ArrayList<Integer>());
        }
        for (int i = 0; i < N-1; i++) {
            tokens = new StringTokenizer(input.readLine());
            int u = Integer.parseInt(tokens.nextToken());
            int v = Integer.parseInt(tokens.nextToken());
            if(u>v){
                int tmp = v;
                v = u;
                u = v;
            }
            //root 설정
            if(i==0){
                headNum = u;
            }
            //부모 자식 설정
            nodes[v].parent = u;
            nodes[u].childNodes.add(v);
        }

        // 2. solve
        queue.add(headNum);
        int nowNode;
        int cnt = 0;
        while(!queue.isEmpty()){
            cnt++;
            nowNode = queue.poll();
            if(nodes[nowNode].parent!=-1){
                if(!nodes[nodes[nowNode].parent].isEarlyAdapter){
                    nodes[nowNode].isEarlyAdapter = true;
                    answer++;
                }
                else if(nodes[nowNode].childNodes.size()>=2){
                    nodes[nowNode].isEarlyAdapter = true;
                    answer++;
                }
            }
            for (int i = 0; i < nodes[nowNode].childNodes.size(); i++) {
                if(!nodes[nowNode].isEarlyAdapter || nodes[nodes[nowNode].childNodes.get(i)].childNodes.size()!=0)
                    queue.add(nodes[nowNode].childNodes.get(i));
            }
        }
        System.out.println(cnt+"adf");
//        for (int i = 0; i < N; i++) {
//            System.out.println(i+"번 노드: "+nodes[i].toString());
//        }

        // 3. output
        System.out.println(answer);
    }
}
