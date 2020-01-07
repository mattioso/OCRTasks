package com.Mattioso;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

        String inputString = "Hello there";
        inputString = inputString.toLowerCase();
        String[] converted;
        converted = new String[inputString.length()];

        char[] alphabet;
        alphabet = new char[26];
        alphabet[0] = 'a';
        alphabet[1] = 'b';
        alphabet[2] = 'c';
        alphabet[3] = 'd';
        alphabet[4] = 'e';
        alphabet[5] = 'f';
        alphabet[6] = 'g';
        alphabet[7] = 'h';
        alphabet[8] = 'i';
        alphabet[9] = 'j';
        alphabet[10] = 'k';
        alphabet[11] = 'l';
        alphabet[12] = 'm';
        alphabet[13] = 'n';
        alphabet[14] = 'o';
        alphabet[15] = 'p';
        alphabet[16] = 'q';
        alphabet[17] = 'r';
        alphabet[18] = 's';
        alphabet[19] = 't';
        alphabet[20] = 'u';
        alphabet[21] = 'v';
        alphabet[22] = 'w';
        alphabet[23] = 'x';
        alphabet[24] = 'x';
        alphabet[25] = 'z';

        String[] morse;
        morse = new String[26];
        morse[0] = ".-"; //a
        morse[1] = "-..."; //b
        morse[2] = "-.-."; //c
        morse[3] = "-.."; //d
        morse[4] = "."; //e
        morse[5] = "..-."; //f
        morse[6] = "--."; //g
        morse[7] = "...."; //h
        morse[8] = ".."; //i
        morse[9] = ".---"; //j
        morse[10] = "-.-"; //k
        morse[11] = ".-.."; //l
        morse[12] = "--"; //m
        morse[13] = "-."; //n
        morse[14] = "---"; //o
        morse[15] = ".--."; //p
        morse[16] = "--.-"; //q
        morse[17] = ".-."; //r
        morse[18] = "..."; //s
        morse[19] = "-"; //t
        morse[20] = "..-"; //u
        morse[21] = "...-"; //v
        morse[22] = ".--"; //w
        morse[23] = "-..-"; //x
        morse[24] = "-.--"; //y
        morse[25] = "--.."; //z

        int count = 0;

        while(count != inputString.length()) {

            if (inputString.charAt(count) == ' ') {
                converted[count] = "|";
            }else {
                converted[count] = morse[getPos(alphabet, inputString.charAt(count))] + " ";

            }

            count++;
        }

        String output = "";

        count = 0;
        while(count != converted.length) {
            output = output + converted[count];
            count += 1;
        }
        System.out.println(output);

    }

    public static int getPos(char[] array, char letter) {
        int count = 0;
        while (count != array.length) {
            if (array[count] == letter) {
                return count;
            }
            count++;
        }
        return -1;
    }
}
