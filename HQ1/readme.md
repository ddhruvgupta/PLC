
3. Complete the definition of the following function:
def singleDigit(num: Int): Int =
This function takes a positive integer, num, as input and returns a digit between 0 and 9 as the output. The output is
computed as follows: sum all the digits in num to obtain a result; if this result is less than 10 then result is the answer;
otherwise take the result and apply the same procedure (i.e. sum its digits and compute a result, …). For example,

singleDigit(37425) => (3+7+4+2+5) = 21 => (2+1) = 3
singleDigit(9876543) => (9+8+7+6+5+4+3) = 42 => (4+2) = 6

You probably will need to write a helper function to sum the digits.



4. Given the following function:

def extractDigits(num: Int): Set[Int] =
	if (num == 0) Set[Int]()
	else extractDigits(num/10) + (num%10)

which extracts the individual digits of a positive number and returns these in a Scala Set. Complete Scala function
definitions for the following:

	def noRepeatingDigits(num: Int): Boolean =
	
	def numBulls(num1: Int, num2: Int): Int =
	
	def numCows(num1: Int, num2: Int): Int =

	In this problem, num, num1, and num2 are positive integers with all having the same number of digits. The
noRepeatingDigits function is self-explanatory. It takes num as input and returns true if num has no repeating digits
and false otherwise. For example

	noRepeatingDigits(12345) = true
	noRepeatingDigits(12452) = false

The remaining two functions take two numbers, num1 and num2 as inputs and returns the output as follows:

BULLS = number of digits that appear in the same positions in the two numbers.
COWS = number of digits that appear in both the numbers, but at different positions.

For example, if the two numbers were 2367 and 1327, we have 2 BULLS (for the exact matches for digits 3 and 7) and 1 COW (for the remaining common digit 2 which is in different positions in the two numbers). If the numbers were 9852 and 8926, we have 0 BULLS and 3 COWS and if the numbers were 1234 and 4321, we have 0 BULLS and 4 COWS. It is quite clear that if the two numbers are the same, we have 4 BULLS and 0 COWS.