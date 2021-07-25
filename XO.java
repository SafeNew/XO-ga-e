import java.io.Console;

public class XO {
    public static char[] board = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
    public static int board_space = 0;
    public static void main(String[] args) {
        boolean X_start = true;
        setUp();
        Display();
        while (checkWining()[0]) {
            UserInput(X_start);
            Display();
            X_start = !X_start;
        }
        if (checkWining()[1]) {
            System.out.println("Draw");
        } else if (!X_start) {
            System.out.println("Winner is x");
        } else {
            System.out.println("Winner is o");
        }
    }
    static void setUp() {
        System.out.println("Please Input number between 1 - 9 \n");
        System.out.println(" 1 | 2 | 3");
        System.out.println("-----------");
        System.out.println(" 4 | 5 | 6");
        System.out.println("-----------");
        System.out.println(" 7 | 8 | 9 \n");
        System.out.println("-- game start --\n");
    }
    static void Display() {
        System.out.println(" "+board[0]+" | "+board[1]+" | "+board[2]);
        System.out.println("-----------");
        System.out.println(" "+board[3]+" | "+board[4]+" | "+board[5]);
        System.out.println("-----------");
        System.out.println(" "+board[6]+" | "+board[7]+" | "+board[8]+'\n');
    }
    static void UserInput(boolean X_start) {
        Console console = System.console();
        if (X_start) {
            System.out.print("X turn input : ");
        } else {
            System.out.print("O turn input : ");
        }
        try {
            String consoleInput = console.readLine();
            int i = Integer.parseInt(consoleInput);
            if (inputCheck(i)) {
                if (board[i - 1] == ' '){
                    if (X_start) {
                        board[i - 1] = 'X';
                    } else {
                        board[i - 1] = 'O';
                    }
                    board_space += 1;
                    return;
                } else {
                    System.out.println("Can not put the mark on same tile \n");
                }
            } else {
                System.out.println("Please input number between 1 - 9 \n");
            } 
        } catch (Exception e) {
            System.out.println("Please input number between 1 - 9 \n");
        }      
        Display();
        UserInput(X_start);
    }
    static boolean inputCheck(int x) {
        int[] board_range = {1,2,3,4,5,6,7,8,9};
        for (int i = 0;i < 9; i++) {
            if (x == board_range[i]){
                return true;
            }
        }
        return false;
    }
    static boolean[] checkWining() {
        boolean[] ans = new boolean[2];
        // แนวนอน
        if (board[0] == board[1] && board[0] == board[2] && board[0] != ' '){
            ans[0] = false; ans[1] = false;
            return ans;
        }
        if (board[3] == board[4] && board[3] == board[5] && board[3] != ' '){
            ans[0] = false; ans[1] = false;
            return ans;
        }
        if (board[6] == board[7] && board[6] == board[8] && board[6] != ' '){
            ans[0] = false; ans[1] = false;
            return ans;
        }
        // แนวตั้ง
        if (board[0] == board[3] && board[0] == board[6] && board[0] != ' '){
            ans[0] = false; ans[1] = false;
            return ans;
        }
        if (board[1] == board[4] && board[1] == board[7] && board[1] != ' '){
            ans[0] = false; ans[1] = false;
            return ans;
        }
        if (board[2] == board[5] && board[2] == board[8] && board[2] != ' '){
            ans[0] = false; ans[1] = false;
            return ans;
        }
        // แนวทแยง
        if (board[0] == board[4] && board[0] == board[8] && board[0] != ' '){
            ans[0] = false; ans[1] = false;
            return ans;
        }
        if (board[2] == board[4] && board[2] == board[6] && board[2] != ' '){
            ans[0] = false; ans[1] = false;
            return ans;
        }
        if (board_space == 9) {
            ans[0] = false; ans[1] = true;
            return ans;
        }
        ans[0] = true; ans[1] = false;
        return ans;
    }
}