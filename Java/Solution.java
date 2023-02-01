package Java;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class Solution {

    private static void solve(int col, char[][] board, List<List<String>> ans, int leftRow[], int lowDiag[],
            int upDiag[]) {
        if (col == board.length) {
            ans.add(construct(board));
            return;
        }

        for (int row = 0; row < board.length; row++) {
            if (leftRow[row] == 0 && lowDiag[row + col] == 0 && upDiag[board.length - 1 + col - row] == 0) {
                board[row][col] = 'Q';
                leftRow[row] = 1;
                lowDiag[row + col] = 1;
                upDiag[board.length - 1 + col - row] = 1;
                solve(col + 1, board, ans, leftRow, lowDiag, upDiag);
                board[row][col] = '.';
                leftRow[row] = 0;
                lowDiag[row + col] = 0;
                upDiag[board.length - 1 + col - row] = 0;
            }
        }
    }

    private static List<String> construct(char[][] board) {
        List<String> res = new LinkedList<String>();
        for (int i = 0; i < board.length; i++) {
            String s = new String(board[i]);
            res.add(s);
        }
        return res;
    }

    public List<List<String>> solveNQueens(int n) {
        List<List<String>> ans = new ArrayList<List<String>>();
        char[][] board = new char[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                board[i][j] = '.';
        int lRow[] = new int[n];
        int upDiag[] = new int[2 * n - 1];
        int lowDiag[] = new int[2 * n - 1];
        solve(0, board, ans, lRow, lowDiag, upDiag);
        return ans;
    }

    public static void main(String[] args) {
        // int count = new Solution().eraseOverlapIntervals(new int[][] { { 1, 2 }, { 1, 2 }, { 1, 2 } });
        // Map<Character, Character> myMap = new HashMap<>();

        // myMap.g
        int[] my_numbers = new int[] { 4, 5, 6 };


        System.out.println("Done.");
        // System.out.println(String.format("Got these many: %d", count));
    }
}
