
object hq3 {
  type Bag = Int => Int
  val bound = 99

  def emptyBag: Bag =
    x => 0
  def count(b: Bag, elem: Int): Int =
    b(elem)

  def contains(b: Bag, elem: Int): Boolean =
    b(elem) > 0

  def add(b: Bag, elem: Int): Bag =
    x => if (x == elem) 1 + count(b,x) else count(b,x)

  // This function adds n instances of elem into b and returns the new bag
  def addN(b: Bag, elem: Int, n: Int): Bag = {
    x => if (x == elem) n + count(b,x) else count(b,x)

  }

  def toString(b: Bag): String = {
    val xs = for (i  <-  0 to bound if contains(b, i)) yield (i,count(b,i))
    xs.mkString("{", ",", "}")
  }

  def printBag(b: Bag): Unit = {
    println(toString(b))
  }

  def decode(xs: List[(String, Int)]):List[String] = {

    // get a list of tuples, recurse through each list item
    def _expand(res: List[String], rem:(String, Int)):List[String] = rem match {
        //
      case (_, 0) => res
      case (h, n) => _expand(res:::List(h), (h, n -1))
    }

    xs flatMap { e => _expand(List(),e) }
  }


  def dropKth(xs: List[Int], k: Int): List[Int] = xs match {
    case Nil => Nil
    case _ =>
      val a = xs.take(k-1)
      val b = xs.drop(k)
      a ++ dropKth(b,k)
  }


  def maxList(xs: List[Int]): Int ={
      xs.foldLeft(Integer.MIN_VALUE)(_ max _)
  }

  def factorial(n: Int): Int ={
    if ( n>0 ){
      val a = List.range(n,0,-1)
      a.foldLeft(1)(_ * _)
    }else 1

  }

  def convertNum2Binary(num: Int): String = num.toBinaryString

//  def convertFraction2Binary(num: Double): String = {
//    val temp = num.toInt
//    val i = convertNum2Binary(temp)
//    val frac = num - i.toDouble
//
//
//
//    val a = List.tabulate(24)(x => ((frac * math.pow(2,x)).toInt % 2))
//
//    i +"."+ a.mkString
//  }



  def convertFraction2Binary(num: Double): String = {
    def helper(x: Double, y: String): String = {
      if (x==1.0 || y.length >= 23)
        y
      else
      if(2*x > 1.0)
          helper(2*x-1, y+"1")
        else
          helper(2*x, y+"0")
    }
    helper(num, ".")
  }

}
