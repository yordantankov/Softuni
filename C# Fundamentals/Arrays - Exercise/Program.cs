using System;
using System.Linq;

namespace Array_Rotation
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int [] arr= Console.ReadLine()
                .Split(' ', StringSplitOptions.RemoveEmptyEntries)
                .Select(int.Parse)
                .ToArray();
            int rotationCount = int.Parse(Console.ReadLine());

           
            for (int rot = 1; rot <= rotationCount; rot++)
            {
                int firstEl = arr[0];
                for (int i = 0; i <= arr.Length - 2; i++)
                {
                    arr[i] = arr[i + 1];
                }
                arr[arr.Length - 1] = firstEl;
            }
            Console.WriteLine(String.Join(" ", arr));
           

        }
    }
}
