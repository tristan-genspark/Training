

class Test
{
    public static void main(String[] args)
    {

        // Loop 5 times
        for (int i=0;i<=5;i++)
        {
              System.out.println(Integer.toString(i));
        }

        // loop until stop is true
        Boolean stop = false;
        while (!stop)
        {
          System.out.println("Looping until stop is true");
          stop = false; // loops once because we set stop to true
        }

        // loop forever
        while (true)
        {
              System.out.println("Looping Forever");
        }


        // Do an action first and then check if it should exit the loop
        // Do while loops do not exsist in python

        int i = 0;
        do
        {
          System.out.println("Hello World");

          i++;
        }
        while (i > 5);


    }
}
