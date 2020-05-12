
object Driver extends App{
import hq3._

  val b1 = addN(emptyBag, 1 , 5)
  print("b1 = ")
  printBag(b1)

  val b2 = decode(List(("a",3),("b",4),("c",2),("d",0)))
  println(b2)

  println(dropKth(List(1,2,3,4,5,6,7,8,9,10), 3))

  val a = List(1,2,3,4,5,6,7,8,9,10)
  println(maxList(a))

  println(factorial(3))
  println(convertNum2Binary(100))
  println(convertFraction2Binary(.8))
}
