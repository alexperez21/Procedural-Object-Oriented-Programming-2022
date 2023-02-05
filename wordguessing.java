import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) { 

    ArrayList<String> words = new ArrayList<String>();
    try{
      File myObj = new File("input.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        words.add(data);
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occured.");
      e.printStackTrace();
    }

    Random rnd = new Random();
    int wordIndex = rnd.nextInt(words.size());
    String word = words.get(wordIndex);

    int numGuesses = 6;
    ArrayList<String> guesses = new ArrayList<String>();
    String[] guessed = new String[word.length()];
    for(int i = 0; i < word.length(); i++){guessed[i] = "_";}

  Scanner sc = new Scanner(System.in);
    while(numGuesses > 0 &&
!word.equals(String.join("", guessed))) {
      System.out.println("\nYou have " + numGuesses + "remaining.");
      System.out.println("Guessed Letters:" + String.join(" ", guessed));

      System.out.println("Guess a Letter: ");
      String guess = sc.nextLine();
      while(guess.length() != 1 || !guess.matches("[a-zA-Z]") || guesses.contains(guess)) {
        if(guesses.contains(guess)){
          System.out.println("You already guessed that, try again.");
        } else {
          System.out.println("Guess a letter:");
          guess = sc.nextLine();
        }
        System.out.print("\033[H\033[2J");
        System.out.flush();

        guesses.add(guess);

        if(word.contains(guess)) {
          int index = 0; 
          while(word.indexOf(guess, index) != -1){
            index = word.indexOf(guess, index);
            if(index < 0) {index = word.length() + index;}
            guessed[index] = guess;
            index += 1;
          }
        } else {
          numGuesses -= 1;
        }
      }
      if(word.equals(String.join("", guessed))){
        System.out.println("The word was " + word);
        System.out.println("\nGame Over!");
      } else {
        System.out.println("\nGame Over!");
        System.out.println("The word was " + word);
      }
    }
  }
}
    
