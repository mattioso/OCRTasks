package com.Mattioso;

public class Main {

    public static void main(String[] args) {

        String year = "1998";
        int yearLength = year.length();
        int count = 0;

        int[] nums = new int[10];

        while (!(count == yearLength)){
            char ch = year.charAt(count);
            int num = Integer.parseInt(String.valueOf(ch));
            nums[num]++;
            count++;
        }

        count = 0;
        while(count < 10){
            if (nums[count] > 1){
                System.out.println("Number of " + count + "'s is " + nums[count]);
            }
            count++;
        }


    }
}
