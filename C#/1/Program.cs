// // Console.WriteLine("Введите имя");
// // string username = Console.ReadLine();
// // Console.Write("Привет,ЗАЛУПА ");
// // Console.Write(username);
// // Console.WriteLine();

// // int numberA = 3;
// // int numberB = 1500000;
// // int r = numberA + numberB;
// // Console.WriteLine(r);



// // double numberA = 1200000;
// // double numberB = 1500000;
// // double r = numberA * numberB;
// // Console.WriteLine(r);

// // new Random().Next(1,10)        // случайные числа от 1 до 10

// // double numberA = new Random().Next(1,10);  // случайные числа от 1 до 10
// // Console.WriteLine(numberA);
// // double numberB = new Random().Next(10,15);
// // Console.WriteLine(numberB);
// // double r = numberA - numberB;
// // Console.WriteLine(r);


// // Console.WriteLine("Введите имя пользователя");
// // string username = Console.ReadLine();

// // if(username.ToLower() == "андрей")
// // {
// //     Console.WriteLine("Привет БРАТАН");
// // }
// // else
// // {
// //     Console.WriteLine("Соси пипирку !");
// // }


// // int a = 1;
// // int b = 15;
// // int c = 5;
// // int d = 7;
// // int i = 111;
// // int w = 12;

// // int max = a;

// // if ( a > max ) max = a;
// // if ( b > max ) max = b;
// // if ( c > max ) max = c;
// // if ( d > max ) max = d;
// // if ( i > max ) max = i;
// // if ( w > max ) max = w;
// // Console.Write("Max = ");
// // Console.WriteLine(max);


// // Console.Clear();
// // // Console.SetCursorPosition(10, 4);
// // // Console.WriteLine("+");

// // int xa = 40, ya = 1,
// //     xb = 1, yb = 30,
// //     xc = 80, yc = 30;
// // Console.SetCursorPosition(xa, ya);
// // Console.WriteLine("+");

// // Console.SetCursorPosition(xb, yb);
// // Console.WriteLine("+");

// // Console.SetCursorPosition(xc, yc);
// // Console.WriteLine("+");


// // int x = xa, y = xb;

// // int count = 10;

// // while(count < 10000)
// // {
// //     int what = new Random().Next(0, 3);
// //     if (what == 0)
// //     {
// //         x = (x + xa)/2;
// //         y = (y + ya)/2;

// //     }
// //     if (what == 1)
// //     {
// //         x = (x + xb)/2;
// //         y = (y + yb)/2;
// //     }
// //     if (what == 2)
// //     {
// //         x= (x + xc)/2;
// //         y = (y + yc)/2;
// //     }
// //     Console.SetCursorPosition(x,y);
// //     Console.WriteLine("+");
// //     count++;
// // }
// // Con  sole.WriteLine();

// int Max(int arg1, int arg2, int arg3, int arg4, int arg5, int arg6, int arg7, int arg8, int arg9, int arg10, int arg11, int arg12)
// {
//     int resalt = arg1;
//     if(arg1 > resalt) resalt = arg1;
//     if(arg2 > resalt) resalt = arg2;
//     if(arg3 > resalt) resalt = arg3;
//     if(arg4 > resalt) resalt = arg4;
//     if(arg5 > resalt) resalt = arg5;
//     if(arg6 > resalt) resalt = arg6;
//     if(arg7 > resalt) resalt = arg7;
//     if(arg8 > resalt) resalt = arg8;
//     if(arg9 > resalt) resalt = arg9;
//     if(arg10 > resalt) resalt = arg10;
//     if(arg11 > resalt) resalt = arg11;
//     if(arg12 > resalt) resalt = arg12;
//     return resalt;
// }
// int a = -111;
// int a1 = -12;
// int b = -14;
// int b1 = -15;
// int c = -50;
// int c1 = -55;
// int d = -1711;
// int d1 = -70001;
// int i = -101;
// int i1 = -11;
// int w = -13;
// int w1 = -19;

// int max = Max(a, a1, b, b1, c, c1, d, d1, i, i1, w, w1);



// // if(a > max) max = a;
// // if(a1 > max) max = a1;
// // if(b > max) max = b;
// // if(b1 > max) max = b1;
// // if(c > max) max = c;
// // if(c1 > max) max = c1;
// // if(d > max) max = d;
// // if(d1 > max) max = d1;
// // if(i > max) max = i;
// // if(i1 > max) max = i1;
// // if(w > max) max = w;
// // if(w1 > max) max = w1;

// Console.Write("max =  ");
// Console.WriteLine(max);
// Console.WriteLine();



// МАССИВЫ

// int Max(int arg1, int arg2, int arg3, int arg4, int arg5, int arg6, int arg7, int arg8, int arg9, int arg10, int arg11, int arg12)
// {
//     int resalt = arg1;
//     if (arg1 > resalt) resalt = arg1;
//     if (arg2 > resalt) resalt = arg2;
//     if (arg3 > resalt) resalt = arg3;
//     if (arg4 > resalt) resalt = arg4;
//     if (arg5 > resalt) resalt = arg5;
//     if (arg6 > resalt) resalt = arg6;
//     if (arg7 > resalt) resalt = arg7;
//     if (arg8 > resalt) resalt = arg8;
//     if (arg9 > resalt) resalt = arg9;
//     if (arg10 > resalt) resalt = arg10;
//     if (arg11 > resalt) resalt = arg11;
//     if (arg12 > resalt) resalt = arg12;
//     return resalt;
// }

// int[] array = { 14, 12, 131, 45, 53, 76, 75, 8, -99999, 1550, 1451, 1452 };

// // array[0] = 9999;
// Console.WriteLine(array[0]);

// int max = Max(array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], array[10], array[11]);



// Console.Write("max =  ");
// Console.WriteLine(max);
// Console.WriteLine();

// int[] array = { 1, 2, 3, 4, 5, 6, 7, 9, 9 };
// int n = array.Length;
// int find = 9;
// int index = 0;
// while (index < n)
// {
//     if (array[index] == find)
//     {

//         Console.WriteLine(index);
//         break;



//     }
//     index++;
// }




// (Метод)

void FillArray(int[] collection)
{
    int Length = collection.Length;
    int index = 0;
    while ( index < Length)
    {
      collection[index] = new Random().Next(1, 10);
      index++;
    }
}
void PrintArray(int[] col)
{
    int count = col.Length;
    int position = 0;
    while(position<count)
    {
        Console.WriteLine(col[position]);
        position++;
    }
   
}

int IndexOf(int[]collection, int find)
{
    int count = collection.Length;
    int index = 0;
    int position = -1;
    while(index<count)
    {
        if(collection[index]==find)
        {
            position=index;
            break;
        }
        index++;
    }
    return position;
}
int[] array = new int[10];

FillArray(array);
PrintArray(array);
Console.WriteLine();

int pos = IndexOf(array, 4);
Console.WriteLine(pos);


