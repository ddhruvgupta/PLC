object test {
  def extractDigits(num: Int): Set[Int] =
    if (num == 0) Set[Int]()
    else extractDigits(num / 10) + (num % 10)

  def noRepeatingDigits(num: Int): Boolean = {
    if (num == 0)
      true
    else if (extractDigits(num / 10) contains num % 10)
      false
    else
      noRepeatingDigits(num / 10)

  }

  def numBulls(num1: Int, num2: Int): Int ={

    if (num1 == 0 || num2 == 0) 0
    else if (num1%10 == num2%10)  1+numBulls(num1/10,num2/10)
    else numBulls(num1/10,num2/10)


  }

  def numCows(num1: Int, num2: Int): Int ={
    if (num1 == 0 || num2 == 0)  return 0
    else if(extractDigits(num1) contains num2%10)
      1 + numCows(num1,num2/10)
    else
      numCows(num1,num2/10)

  }

    def main(args: Array[String]): Unit ={
      println(noRepeatingDigits(1000))
      println(numBulls(2367,132))
      println(numCows(9852,8926))
    }

}