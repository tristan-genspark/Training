import java.util.ArrayList;

class Test
{
    public static void main(String[] args)
    {


    ArrayList<Integer> array1 = new ArrayList<Integer>();
    array1.add(1);
    array1.add(2);
    array1.add(3);

    System.out.println(Integer.valueOf(array1.get(0)));
    System.out.println(Integer.valueOf(array1.get(1)));
    System.out.println(Integer.valueOf(array1.get(2)));

    array1.set(1, 9); // assign second value within the list to 9

    System.out.println(Integer.valueOf(array1.get(1))); // display to see it has changed




    }
}
