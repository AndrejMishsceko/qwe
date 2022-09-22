// Console.WriteLine("Введите имя");
// string username = Console.ReadLine();
// Console.Write("Привет,ЗАЛУПА ");
// Console.Write(username);
// Console.WriteLine();

// int numberA = 3;
// int numberB = 1500000;
// int r = numberA + numberB;
// Console.WriteLine(r);



// double numberA = 1200000;
// double numberB = 1500000;
// double r = numberA * numberB;
// Console.WriteLine(r);

// new Random().Next(1,10)        // случайные числа от 1 до 10

// double numberA = new Random().Next(1,10);  // случайные числа от 1 до 10
// Console.WriteLine(numberA);
// double numberB = new Random().Next(10,15);
// Console.WriteLine(numberB);
// double r = numberA - numberB;
// Console.WriteLine(r);


// Console.WriteLine("Введите имя пользователя");
// string username = Console.ReadLine();

// if(username.ToLower() == "андрей")
// {
//     Console.WriteLine("Привет БРАТАН");
// }
// else
// {
//     Console.WriteLine("Соси пипирку !");
// }


// int a = 1;
// int b = 15;
// int c = 5;
// int d = 7;
// int i = 111;
// int w = 12;

// int max = a;

// if ( a > max ) max = a;
// if ( b > max ) max = b;
// if ( c > max ) max = c;
// if ( d > max ) max = d;
// if ( i > max ) max = i;
// if ( w > max ) max = w;
// Console.Write("Max = ");
// Console.WriteLine(max);


Console.Clear();
// Console.SetCursorPosition(10, 4);
// Console.WriteLine("+");

int xa = 40, ya = 1,
    xb = 1, yb = 30,
    xc = 80, yc = 30;
Console.SetCursorPosition(xa, ya);
Console.WriteLine("+");

Console.SetCursorPosition(xb, yb);
Console.WriteLine("+");

Console.SetCursorPosition(xc, yc);
Console.WriteLine("+");


int x = xa, y = xb;

int count = 10;

while(count < 10000)
{
    int what = new Random().Next(0, 3);
    if (what == 0)
    {
        x = (x + xa)/2;
        y = (y + ya)/2;

    }
    if (what == 1)
    {
        x = (x+xb)/2;
        y = (y+yb)/2;
    }
    if (what == 2)
    {
        x= (x + xc)/2;
        y = (y + yc)/2;
    }
    Console.SetCursorPosition(x,y);
    Console.WriteLine("+");
    count++;
}
Console.WriteLine();