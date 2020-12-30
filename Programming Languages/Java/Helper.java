import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;


public class Helper {

    private static void clearScreen(){
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    private static String input(String prompt) throws IOException {
        System.out.print(prompt);
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        return reader.readLine();
    }

    private static void println(String s){
        System.out.println(s);
    }

    private static void wrong_option() throws InterruptedException {
        System.out.println("Wrong option!");
        Thread.sleep(1500);
    }

    private static void wait_for_user() throws IOException {
        System.out.println("\nPress enter to continue...");
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        reader.readLine();
    }
}
