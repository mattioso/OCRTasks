using System;
using System.Collections.Generic;
using System.Linq;

namespace NumberTable
{
	class Program
	{
		static void Main(string[] args)
		{
			string operation;
			string num;

			Console.Write("Operation: ");
			operation = Console.ReadLine();
			if (!IsOperation(operation))
			{
				Console.WriteLine("Operation Invalid");
				Environment.Exit(0);
			}
			Console.Write("Number: ");
			num = Console.ReadLine();

			if (!IsNumber(num))
			{
				Console.WriteLine("Number Invalid");
				Environment.Exit(0);
			}

			int number = int.Parse(num);

			Console.WriteLine(GetTable(operation, number));

		}

		static string GetTable(string operation, int number) 
		{

			string result = operation + " |";

			for (int i = 0; i != number + 1; i++)
			{
				result += " " + i;
			}

			int length = result.Length;
			result += "\n";

			for(int i = 0; i != length; i++)
			{
				result += "-";
			}
			result += "\n";

			for (decimal i = 0; i != number + 1; i++)
			{
				result += i + " |";
				for (decimal x = 0; x != number + 1; x++)
				{
					if (operation == "+") result += " " + (i + x);
					if (operation == "-") result += " " + (i - x);
					if (operation == "*") result += " " + (i * x);
					if (operation == "/") 
					{	
						if(x != 0) {
							decimal y = i / x;
							result += " " + Math.Round(y, 2);
						}
						else 
						{
							result += " NA";
						}
					}
				}
				result += "\n";
			}

			return result;
		}

		static bool IsOperation(string operation) {
			string[] operations = {"+","-","*","/"};
			if (operations.Contains(operation))
			{
				return true;
			}
			return false;
		}

		static bool IsNumber(string number)
		{
			try
			{
				int result = Int32.Parse(number);
				return result > 0;
			}
			catch
			{
				return false;
			}
		}
	}
}
