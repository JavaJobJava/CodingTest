package syheo.baekjoon_java;

/**
 * 2 2 0 0 0 7
 * 3 0 0 5 0 7
 * 3 1 1 5 0 7
 * 3 0 0 0 0 0
 * 4 0 0 0 8 8
 * 4 0 6 6 6 0
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 문제 번역
 * Rush Hour는 1970년대 Nob Yoshigahara가 개발한 퍼즐 게임입니다. 현재 ThinkFun에서 제조하고 있습니다.
 * 보드는 차량이 미끄러질 수 있도록 타일에 홈이 있는 6 × 6 그리드입니다. 자동차와 트럭은 모두 너비가 1제곱이지만
 * 자동차는 길이가 2제곱이고 트럭은 길이가 3제곱입니다. 차량은 그리드의 직선을 따라 앞이나 뒤로만 이동할 수 있습니다.
 * 게임의 목표는 다른 차량을 방해하지 않도록 이동하여 보드의 출구를 통해 유일한 빨간 자동차를 완전히 제거하는 것입니다.
 * 그림 1은 러시아워 퍼즐의 예를 보여줍니다.
 * <p>
 * 우리는 퍼즐의 각 차량에 1부터 차량 수까지 번호가 매겨진 고유한 ID를 부여합니다. 여기서 빨간 자동차의 ID는 1입니다.
 * 퍼즐의 보드 정보는 보드 매트릭스라는 6 × 6 매트릭스로 표시됩니다. 보드 행렬의 각 항목은 해당 홈에 배치된 차량의 ID이며
 * 해당 홈에 차량이 없으면 항목은 0으로 채워집니다. 보드의 출구는 3열의 오른쪽 끝에 있습니다. 그림 2는 그림 1의 퍼즐에
 * 해당하는 보드 매트릭스를 보여줍니다.
 * <p>
 * 조각(자동차 또는 트럭)을 한 단위(그루브) 이동하는 것을 단계라고 합니다. 퍼즐은 10단계 이내로 풀 수 있다면 쉽습니다.
 * 퍼즐이 쉬운지 아닌지를 판단하는 프로그램을 작성해 주세요.
 */

/**
 * 출력
 * 퍼즐이 쉬우면 입력된 퍼즐을 풀기 위한 최소 단계 수를 출력하고, 그렇지 않으면 -1을 출력합니다.
 */

public class Main_18139 {

    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;
    static int[][] maps = new int[6][6];
    static Vehicle[] vehicles;
    static int vehicleCnt = 0;
    static Queue<Info> queue = new LinkedList<>(); // vehicles의 vehicle들이 +방향,-방향으로 얼마나 갔는지 저장.
    static HashSet<String> visited = new HashSet<>();

    static class Info {
        int[] moves;
        int cnt;

        public Info(int[] moves, int cnt) {
            this.moves = moves;
            this.cnt = cnt;
        }
    }

    static class Vehicle {
        boolean isHorizon;
        boolean isCar;
        int row1, row2, row3;
        int col1, col2, col3;

    }

    static class Car extends Vehicle {

        public Car(int row1, int col1, int row2, int col2, boolean isHorizon) {
            this.row1 = row1;
            this.col1 = col1;
            this.row2 = row2;
            this.col2 = col2;
            this.isHorizon = isHorizon;
            this.isCar = true;
        }
    }

    static class Truck extends Vehicle {

        public Truck(int row1, int col1, int row2, int col2, int row3, int col3, boolean isHorizon) {
            this.row1 = row1;
            this.col1 = col1;
            this.row2 = row2;
            this.col2 = col2;
            this.row3 = row3;
            this.col3 = col3;
            this.isHorizon = isHorizon;
            this.isCar = false;
        }
    }


    public static void main(String[] args) throws IOException {

        // 1. input
        for (int i = 0; i < 6; i++) {
            tokens = new StringTokenizer(input.readLine());
            for (int j = 0; j < 6; j++) {
                maps[i][j] = Integer.parseInt(tokens.nextToken());
                vehicleCnt = Math.max(vehicleCnt, maps[i][j]);
            }

        }

        vehicles = new Vehicle[vehicleCnt + 1];

        // 2. 차 정보 입력 : 가로 방향이면 우측만 탐색, 세로 방향이면 아래만 탐색
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                if (maps[i][j] != 0 && vehicles[maps[i][j]] == null) {
                    if (i < 5 && maps[i + 1][j] == maps[i][j]) { //세로 방향일 경우
                        if (i < 4 && maps[i + 2][j] == maps[i][j]) { //트럭일 경우
                            vehicles[maps[i][j]] = new Truck(i, j, i + 1, j, i + 2, j, false);
                        } else { // 자동차일 경우
                            vehicles[maps[i][j]] = new Car(i, j, i + 1, j, false);
                        }
                    } else { //가로 방향일 경우
                        if (j < 4 && maps[i][j + 2] == maps[i][j]) { //트럭일 경우
                            vehicles[maps[i][j]] = new Truck(i, j, i, j + 1, i, j + 2, true);
                        } else { // 자동차일 경우
                            vehicles[maps[i][j]] = new Car(i, j, i, j + 1, true);
                        }
                    }
                }
            }
        } // for()

        // 3. bfs -> 이동할 수 있는지 검사후 queue 에 삽입
        queue.add(new Info(new int[vehicleCnt + 1], 0));
        while (!queue.isEmpty()) {
            Info info = queue.poll();

            //3-0. map 생성
            maps = new int[6][6];
            for (int i = 1; i <= vehicleCnt; i++) {
                if (vehicles[i].isCar) {
                    if (vehicles[i].isHorizon) {
                        maps[vehicles[i].row1][vehicles[i].col1 + info.moves[i]] = i;
                        maps[vehicles[i].row2][vehicles[i].col2 + info.moves[i]] = i;
                    } else {
                        maps[vehicles[i].row1 + info.moves[i]][vehicles[i].col1] = i;
                        maps[vehicles[i].row2 + info.moves[i]][vehicles[i].col2] = i;
                    }
                }
                if (!vehicles[i].isCar) {
                    if (vehicles[i].isHorizon) {
                        maps[vehicles[i].row1][vehicles[i].col1 + info.moves[i]] = i;
                        maps[vehicles[i].row2][vehicles[i].col2 + info.moves[i]] = i;
                        maps[vehicles[i].row3][vehicles[i].col3 + info.moves[i]] = i;
                    } else {
                        maps[vehicles[i].row1 + info.moves[i]][vehicles[i].col1] = i;
                        maps[vehicles[i].row2 + info.moves[i]][vehicles[i].col2] = i;
                        maps[vehicles[i].row3 + info.moves[i]][vehicles[i].col3] = i;
                    }
                }
            }

            for (int i = 1; i <= vehicleCnt; i++) {
                // 3-1. 정답 체크 : Red Car Check, cnt Check
                if (i == 1) {
                    boolean isPossible = true;
                    int endRedPos = vehicles[1].col2 + info.moves[i];
                    for (int j = 2; j <= vehicleCnt; j++) {
                        if (vehicles[j].isCar) {
                            if (vehicles[j].isHorizon) {
                                if (vehicles[j].row1 != 2) {
                                    continue;
                                }
                                if (endRedPos < vehicles[j].col2 + info.moves[j]) {
                                    isPossible = false;
                                    break;
                                }
                            } else {
                                if (vehicles[j].col1 > endRedPos) {
                                    if (vehicles[j].row1 + info.moves[j] == 2) {
                                        isPossible = false;
                                        break;
                                    }
                                }
                                if (vehicles[j].col2 > endRedPos) {
                                    if (vehicles[j].row2 + info.moves[j] == 2) {
                                        isPossible = false;
                                        break;
                                    }
                                }
                            }
                        }
                        if (!vehicles[j].isCar) {
                            if (vehicles[j].isHorizon) {
                                if (vehicles[j].row1 != 2) {
                                    continue;
                                }
                                if (endRedPos < vehicles[j].col3 + info.moves[j]) {
                                    isPossible = false;
                                    break;
                                }
                            } else {
                                if (vehicles[j].col1 > endRedPos) {
                                    if (vehicles[j].row1 + info.moves[j] == 2) {
                                        isPossible = false;
                                        break;
                                    }
                                }
                                if (vehicles[j].col2 > endRedPos) {
                                    if (vehicles[j].row2 + info.moves[j] == 2) {
                                        isPossible = false;
                                        break;
                                    }
                                }
                                if (vehicles[j].col3 > endRedPos) {
                                    if (vehicles[j].row3 + info.moves[j] == 2) {
                                        isPossible = false;
                                        break;
                                    }
                                }
                            }
                        }
                    }

                    if (isPossible) {
                        if(info.cnt + (7 - endRedPos)>10){
                            System.out.println(-1);
                        }
                        else {
                            System.out.println(info.cnt + (7 - endRedPos));
                        }
                        return;
                    }
                } // 3-1. Red Car Check End
                if (info.cnt == 9) {
                    System.out.println(-1);
                    return;
                }
                // 3-2. moves to queue
                if (i != 1) {
                    if (vehicles[i].isCar) {
                        if (vehicles[i].isHorizon) {
                            if (vehicles[i].col2 + info.moves[i] + 1 < 6 && maps[vehicles[i].row2][vehicles[i].col2 + info.moves[i] + 1] == 0) {
                                int[] nextMoves = info.moves.clone();
                                nextMoves[i] += 1;
                                if (!visited.contains(Arrays.toString(nextMoves))) {
                                    queue.add(new Info(nextMoves, info.cnt + 1));
                                    visited.add(Arrays.toString(nextMoves));
                                }
                            }
                            if (vehicles[i].col1 + info.moves[i] - 1 >= 0 && maps[vehicles[i].row2][vehicles[i].col1 + info.moves[i] - 1] == 0) {
                                int[] nextMoves = info.moves.clone();
                                nextMoves[i] -= 1;
                                if (!visited.contains(Arrays.toString(nextMoves))) {
                                    queue.add(new Info(nextMoves, info.cnt + 1));
                                    visited.add(Arrays.toString(nextMoves));
                                }
                            }
                        } else {
                            if (vehicles[i].row2 + info.moves[i] + 1 < 6 && maps[vehicles[i].row2 + info.moves[i] + 1][vehicles[i].col2] == 0) {
                                int[] nextMoves = info.moves.clone();
                                nextMoves[i] += 1;
                                if (!visited.contains(Arrays.toString(nextMoves))) {
                                    queue.add(new Info(nextMoves, info.cnt + 1));
                                    visited.add(Arrays.toString(nextMoves));
                                }
                            }
                            if (vehicles[i].row1 + info.moves[i] - 1 >= 0 && maps[vehicles[i].row1 + info.moves[i] - 1][vehicles[i].col2] == 0) {
                                int[] nextMoves = info.moves.clone();
                                nextMoves[i] -= 1;
                                if (!visited.contains(Arrays.toString(nextMoves))) {
                                    queue.add(new Info(nextMoves, info.cnt + 1));
                                    visited.add(Arrays.toString(nextMoves));
                                }
                            }
                        }
                    }
                    if (!vehicles[i].isCar) {
                        if (vehicles[i].isHorizon) {
                            if (vehicles[i].col3 + info.moves[i] + 1 < 6 && maps[vehicles[i].row2][vehicles[i].col3 + info.moves[i] + 1] == 0) {
                                int[] nextMoves = info.moves.clone();
                                nextMoves[i] += 1;
                                if (!visited.contains(Arrays.toString(nextMoves))) {
                                    queue.add(new Info(nextMoves, info.cnt + 1));
                                    visited.add(Arrays.toString(nextMoves));
                                }
                            }
                            if (vehicles[i].col1 + info.moves[i] - 1 >= 0 && maps[vehicles[i].row2][vehicles[i].col1 + info.moves[i] - 1] == 0) {
                                int[] nextMoves = info.moves.clone();
                                nextMoves[i] -= 1;
                                if (!visited.contains(Arrays.toString(nextMoves))) {
                                    queue.add(new Info(nextMoves, info.cnt + 1));
                                    visited.add(Arrays.toString(nextMoves));
                                }
                            }
                        } else {
                            if (vehicles[i].row3 + info.moves[i] + 1 < 6 && maps[vehicles[i].row3 + info.moves[i] + 1][vehicles[i].col2] == 0) {
                                int[] nextMoves = info.moves.clone();
                                nextMoves[i] += 1;
                                if (!visited.contains(Arrays.toString(nextMoves))) {
                                    queue.add(new Info(nextMoves, info.cnt + 1));
                                    visited.add(Arrays.toString(nextMoves));
                                }
                            }
                            if (vehicles[i].row1 + info.moves[i] - 1 >= 0 && maps[vehicles[i].row1 + info.moves[i] - 1][vehicles[i].col2] == 0) {
                                int[] nextMoves = info.moves.clone();
                                nextMoves[i] -= 1;
                                if (!visited.contains(Arrays.toString(nextMoves))) {
                                    queue.add(new Info(nextMoves, info.cnt + 1));
                                    visited.add(Arrays.toString(nextMoves));
                                }
                            }
                        }
                    }
                }
            }

        }
        System.out.println(-1);
    }
}
