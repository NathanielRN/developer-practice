// class Solution {

//     public int minCut(String s) {
//         private Integer cutsDp[];
//         private boolean palindromeDp[][];
//         cutsDp = new Integer[s.length()];
//         palindromeDp = new boolean[s.length()][s.length()];
//         // build the palindrome cutsDp for all susbtrings
//         buildPalindromeDp(s, s.length());

//         for (int end = 0; end < s.length(); end++) {
//             int minimumCut = end;
//             for (int start = 0; start <= end; start++) {
//                 if (palindromeDp[start][end]) {
//                     minimumCut = start == 0 ? 0 : Math.min(minimumCut, cutsDp[start - 1] + 1);
//                 }
//             }
//             cutsDp[end] = minimumCut;
//         }
//         return cutsDp[s.length() - 1];
//     }

//     private void buildPalindromeDp(String s, int n) {
//         for (int end = 0; end < s.length(); end++) {
//             for (int start = 0; start <= end; start++) {
//                 if (s.charAt(start) == s.charAt(end) && (end - start <= 2 ||
//                     palindromeDp[start + 1][end - 1])) {
//                     palindromeDp[start][end] = true;
//                 }
//             }
//         }
//     }
// }