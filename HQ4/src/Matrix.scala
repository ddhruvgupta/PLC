object Matrix {

  type Matrix = List[List[Int]]

  // Given a row and component number, n in the range 1..n,
  // return the nth component of the row
  // e.g. extractComponent(List(4,3,5,7,8),3) = 5
  def extractComponent(row: List[Int], n: Int): Int = {
    if (row.length == 0 ||row.length < n || n < 1) -1
    else row(n-1)
  }

  // Given a matrix m, and column number n in the range 1..n,
  // return the nth column from the matrix
  // e.g. extractColumn(List(List(1,2,3),List(4,5,6)),3) = List(3,6)
  def extractColumn(m: Matrix, n: Int): List[Int] =
    m map (row => row(n-1))

  // Similar to extractComponent except this function returns the row
  // after removing the nth column
  // removeComponent(List(4,3,5,7,8),3) = List(4,3,7,8)
  def removeComponent(row: List[Int], n: Int): List[Int] = row match{
    case Nil => Nil
    case _ => row.take(n-1) ++ row.drop(n)
  }

  // similar to extractColumn except this function returns the matrix
  // after removing the nth column
  // e.g. removeColumn(List(List(1,2,3),List(4,5,6)),1) = List(List(2,3),List(5,6))
  def removeColumn(m: Matrix, n: Int): Matrix = {
    m map (row => removeComponent(row,n))
  }

  // rows become columns and columns become rows
  // e.g. m1 = List(List(1,2,3),List(4,5,6))
  //   transpose(m1) = List(List(1, 4), List(2, 5), List(3, 6))
  def transpose(m: Matrix): Matrix ={

    def helper(m: Matrix): Matrix= m match{
      case Nil::xs => Nil
//      case List(Nil) => Nil
      case _ => extractColumn(m,1) :: helper(removeColumn(m,1))
    }

    helper(m)
  }

  // we have seen this in the slides before!
  // xs = List(3,4,7), ys = List(2,9,10)
  // scalarProduct(xs,ys) = 3*2+4*9+7*10 = 112
  def scalarProduct(xs: List[Int], ys: List[Int]): Int ={
    (for ((x,y) <- (xs zip ys)) yield x * y).sum
  }

//  // Produces one row of the matrix multiplication
  def rowMul(row: List[Int], n: Matrix): List[Int] ={
      n map ( r => scalarProduct(row, r))
  }

  // helper function which does the actual matrix multiplication
  // n would be the transpose of the second matrix in the multiplication
  def mmul(m: Matrix, n: Matrix): Matrix ={
    m map (r => rowMul(r, n))
  }

//  val m2 = List(List(1,2),List(3,4))
//  val m3 = List(List(5,6),List(7,8))
//  mmul(m2,m3) = List(List(19, 22), List(43, 50))
  // m4 = List(List(2,3,4),List(5,6,7))
  // m5 = List(List(1,2,3,4),List(2,3,5,6),List(7,1,2,4))
  // matrixMultiply(m4,m5) = List(List(36, 17, 29, 42), List(66, 35, 59, 84))
  // this function calls mmul with m and transpose(n)
  def matrixMultiply(m: Matrix, n: Matrix): Matrix ={
  mmul(m, transpose(n))
}
  // For extra credit;
  // Look up definition at
  // https://www.mathsisfun.com/algebra/matrix-determinant.html
  // and solve this for any size square matrix
  // determinant(List(List(6,1,1),List(4,-2,5),List(2,8,7)) = -306
//  def determinant(m: Matrix): Int ={
//
//}

}