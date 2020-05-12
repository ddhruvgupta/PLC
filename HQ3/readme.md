Place all functions for problems 1,2,3,7,8, and 9 in hq3.scala; Also include any other definitions that your code uses (such as Bag type, bound, etc.)

Implement the following function for the Bags data structure of hq2:
// This function adds n instances of elem into b and returns the new bag
def addN(b: Bag, elem: Int, n: Int): Bag =

Write a Scala function to decode a run-length encoded list. For example
decode(List(("a",3),("b",4),("c",2)))
should evaluate to
List("a","a","a","b","b","b","b","c","c")

def decode(xs: List[(String,Int)]): List[String] = 

Write a Scala function that takes as input a list of integers xs and a positive integer k and returns a new list obtained from xs by removing every kth element. For example,
dropKth(List(1,2,3,4,5,6,7,8,9,10), 3)
should evaluate to
List(1,2,4,5,7,8,10)

def dropKth(xs: List[Int], k: Int): List[Int] =

What the following function do?
def f[T](xs: List[T]): List[T] =
  if (xs.isEmpty)
    xs
  else
    xs.head :: f(for(x <- xs.tail if (x != xs.head)) yield x)
What does the following function do?
def g(n: Int): List[Int] =
  for (i <- List.range(1,n+1) if n%i == 0) yield i
What are the values for the following Scala expressions?
List(1,7,2,9).reduceLeft(_-_)



List(1,7,2,9).foldLeft(0)(_-_)



List(1,7,2,9).reduceRight(_-_)



List(1,7,2,9).foldRight(0)(_-_)

Complete the following definition of finding the maximum value of a list of integers using only foldLeft:
def maxList(xs: List[Int]): Int =

Complete the definition of factorial using foldLeft and 1 to n (no recursion/loop)
def factorial(n: Int): Int =

Complete the definitions of the following two functions:
def convertNum2Binary(num: Int): String =

def convertFraction2Binary(num: Double): String =

Here are sample calls to these functions:
convertNum2Binary(100) = "1100100"
convertFraction2Binary(0.375) = ".011"
convertFraction2Binary(0.8) = ".11001100110011001100110"
In case of repeating patterns, stop at length 23