import java.io.*;  
import java.util.*;
public class main
{
  public static void main (String[] args)
  {
    public ArrayList<String[]> todo = new ArrayList<String[]>();
    System.out.println("What would you like to add?");
    Scanner kb = new Scanner (System.in);
    String temp = kb.next();
    todo.add(temp);
    System.out.println("here is the list:");
    System.out.println(todo.get(0));
  }
}
        
