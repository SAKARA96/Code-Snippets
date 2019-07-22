import java.math.BigInteger;
import java.util.Scanner;

public class FactorialStack{
    static int num;
    private static Scanner inp;
    static BigInteger result;
    BigInteger temp,digit;
    BigInteger answer;

    static BigInteger s1[]=new BigInteger[3000]; static int t1=-1;
    static BigInteger s2[]=new BigInteger[3000]; static int t2=-1;
    static BigInteger s3[]=new BigInteger[3000]; static int t3=-1;
    static BigInteger s4[]=new BigInteger[3000]; static int t4=-1;
    static BigInteger s5[]=new BigInteger[3000]; static int t5=-1;



    void factorial(int number){

        BigInteger output=BigInteger.valueOf(number);

        // initialising all stack values to zero
        for (int x= number-1; x>=1; x--){
//            System.out.println("Multiplying "+output+" and "+x);
            //resetting the stack array
            for (int i=0; i<3000; i++){
                s1[i]=BigInteger.valueOf(0);
                s2[i]=BigInteger.valueOf(0);
                s3[i]=BigInteger.valueOf(0);
                s4[i]=BigInteger.valueOf(0);
                s5[i]=BigInteger.valueOf(0);
            }
            output=multiply(output,x);
        }
        System.out.println("Factorial output :"+output);
    }

    BigInteger multiply(BigInteger num1, int num2){
        BigInteger temp1=num1;
        int l2=(int)(Math.log10(num2)+1);
        int arr2[]= new int[l2];
        int p2=0;

        while(num2!=0 && l2>0)
        {
            arr2[p2]=(num2%10);
            num2=num2/10;
            p2++;
        }

        for (int y=0; y<l2; y++){
            if (y==0){
                temp=temp1.multiply(BigInteger.valueOf(arr2[y]));
                while(!temp.equals(BigInteger.valueOf(0)))
                {   ++t1;
                    s1[t1]=(temp.mod(BigInteger.valueOf(10)));
                    temp=temp.divide(BigInteger.valueOf(10));
                }
//                System.out.println("S1");
//                print_array(s1);
            }

            if (y==1){
                temp=(temp1.multiply(BigInteger.valueOf(arr2[y]))).multiply(BigInteger.valueOf(10));
                while(!temp.equals(BigInteger.valueOf(0)))
                {   ++t2;
                    s2[t2]=(temp.mod(BigInteger.valueOf(10)));
                    temp=temp.divide(BigInteger.valueOf(10));
                }
//                System.out.println("S2");
//                print_array(s2);
            }

            if (y==2){
                temp=(temp1.multiply(BigInteger.valueOf(arr2[y]))).multiply(BigInteger.valueOf(100));
                while(!temp.equals(BigInteger.valueOf(0)))
                {   ++t3;
                    s3[t3]=(temp.mod(BigInteger.valueOf(10)));
                    temp=temp.divide(BigInteger.valueOf(10));
                }
//                System.out.println("S3");
//                print_array(s3);
            }

            if (y==3){
                temp=(temp1.multiply(BigInteger.valueOf(arr2[y]))).multiply(BigInteger.valueOf(1000));
                while(!temp.equals(BigInteger.valueOf(0)))
                {   ++t4;
                    s4[t4]=(temp.mod(BigInteger.valueOf(10)));
                    temp=temp.divide(BigInteger.valueOf(10));
                }
//                System.out.println("S4");
//                print_array(s4);
            }
        }

        s5=add(s1,s2,s3,s4);
        answer=get_value_array(s5);

        //reset stack pointers to top
        t1=-1;
        t2=-1;
        t3=-1;
        t4=-1;
        t5=-1;
        return answer;
    }

    BigInteger [] add(BigInteger s1[],BigInteger s2[],BigInteger s3[],BigInteger s4[]){
        BigInteger carry = BigInteger.valueOf(0);
        int x;
        BigInteger temp_sum;

        for (x=0;x<3000;x++){
            // add all biginteger values at x position
            temp_sum=((((s1[x]).add(s2[x])).add(s3[x])).add(s4[x])).add(carry);
            carry=temp_sum.divide(BigInteger.valueOf(10));
            s5[x]=temp_sum.mod(BigInteger.valueOf(10));
        }
        return s5;
    }

    BigInteger get_value_array(BigInteger test[]){
        BigInteger temp_result= BigInteger.valueOf(0);
        for (int x=0; x<3000; x++){
            temp_result=temp_result.add ((BigInteger.valueOf(10).pow(x)).multiply(test[x]));
        }
        return  temp_result;
    }

    void print_array(BigInteger test[]){
        System.out.println("Printing Array");
        int c=0;
        for (int x=0; x<14; x++){
            System.out.print(test[x]);
        }
        System.out.println();
    }


    public static void main(String[] args)
    {
        FactorialStack obj=new FactorialStack();
        inp = new Scanner(System.in);
        System.out.println("Input:");
        num=inp.nextInt();
        obj.factorial(num);


    }
}