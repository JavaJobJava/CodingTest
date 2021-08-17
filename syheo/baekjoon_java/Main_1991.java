package syheo.baekjoon_java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * solved.ac
 * 백준
 * 1991
 * 트리 순회
 * 트리
 * 실버 1
 *
 * 아이디어 :
 * leftChild, rightChild, id 를 갖는 Node 클래스를 만들어 트리를 구성하고
 * 전위, 중위, 후위 순회에 따라 재귀호출을 통해 방문 처리
 */

public class Main_1991 {

    static int N;
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static StringBuffer sb = new StringBuffer();
    static Node[] nodes = new Node[26];

    static class Node{
        char id;
        Node leftChild;
        Node rightChild;

        public Node(char id) {
            this.id = id;
            this.leftChild = null;
            this.rightChild = null;
        }
    }

    public static void main(String[] args) throws IOException {

        // 1. input
        N = Integer.parseInt(input.readLine());
        for (int i = 0; i < N; i++) {
            nodes[i] = new Node((char)(65+i));
        }
        for (int i = 0; i < N; i++) {
            tokens = new StringTokenizer(input.readLine());
            char parent = tokens.nextToken().charAt(0);
            char left = tokens.nextToken().charAt(0);
            char right = tokens.nextToken().charAt(0);

            if(left != '.'){
                nodes[parent-'A'].leftChild = nodes[left-'A'];
            }
            if(right != '.'){
                nodes[parent-'A'].rightChild = nodes[right-'A'];
            }
        }

        // 2-1.pre
        preVisited('A');

        // 2-2.order
        sb.append("\n");
        orderVisited('A');

        // 2-3.post
        sb.append("\n");
        postVisited('A');

        // 3. result
        System.out.println(sb.toString());

    }

    private static void preVisited(char node) {
        sb.append(node);
        if(nodes[node-'A'].leftChild!=null){
            preVisited(nodes[node-'A'].leftChild.id);
        }
        if(nodes[node-'A'].rightChild!=null){
            preVisited(nodes[node-'A'].rightChild.id);
        }
    }

    private static void orderVisited(char node) {
        if(nodes[node-'A'].leftChild!=null){
            orderVisited(nodes[node-'A'].leftChild.id);
        }
        sb.append(node);
        if(nodes[node-'A'].rightChild!=null){
            orderVisited(nodes[node-'A'].rightChild.id);
        }

    }

    private static void postVisited(char node) {
        if(nodes[node-'A'].leftChild!=null){
            postVisited(nodes[node-'A'].leftChild.id);
        }
        if(nodes[node-'A'].rightChild!=null){
            postVisited(nodes[node-'A'].rightChild.id);
        }
        sb.append(node);
    }

}
