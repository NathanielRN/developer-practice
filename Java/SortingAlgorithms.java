package Java;

import java.util.ArrayList;
import java.util.List;

public class SortingAlgorithms {
    public static void quickSort(List<Integer> my_list) {
        quickSort(my_list, 0, my_list.size() - 1);
    }

    public static void quickSort(List<Integer> my_list, int start, int end) {
        if (start >= end) {
            return;
        }

        int left = start;
        int right = end;
        int pivot_index = (left + right) / 2;
        int pivot = my_list.get(pivot_index);

        while (left < right) {
            while (my_list.get(left) < pivot) {
                left++;
            }

            while (my_list.get(right) > pivot) {
                right--;
            }

            if (left != right) {
                Integer tmp = my_list.get(right);
                my_list.set(right, my_list.get(left));
                my_list.set(left, tmp);
            }
        }

        quickSort(my_list, start, pivot_index);
        quickSort(my_list, pivot_index + 1, end);
    }

    public static List<Integer> mergeSort(List<Integer> my_list) {
        if (my_list.size() == 1) {
            return my_list;
        }

        int split = my_list.size() / 2;
        List<Integer> left = mergeSort(my_list.subList(0, split));
        List<Integer> right = mergeSort(my_list.subList(split + 1, my_list.size()));

        List<Integer> newList = new ArrayList<>();

        int i = 0;
        int j = 0;

        while (i < left.size() && j < right.size()) {
            if (left.get(i) < right.get(j)) {
                newList.add(left.get(i));
                i++;
            } else {
                newList.add(right.get(j));
                j++;
            }
        }

        while (i < left.size()) {
            newList.add(left.get(i));
            i++;
        }

        while (j < right.size()) {
            newList.add(right.get(j));
            j++;
        }

        return my_list;
    }

    public static void main(String[] args) {
        ArrayList<Integer> test1 = new ArrayList<>(List.of(9, 8, 7, 6, 5, 1, 2, 3, 4));
        quickSort(test1);
        System.out.println(test1.toString());
    }
}
