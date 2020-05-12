object Driver extends App {
  import Matrix._

  val m1 = List(List(1,2,3),List(4,5,6))
  val m2 = List(List(1,2),List(3,4))
  val m3 = List(List(5,6),List(7,8))
  val m4 = List(List(2,3,4),List(5,6,7))
  val m5 = List(List(1,2,3,4),List(2,3,5,6),List(7,1,2,4))
  val m6 = List(List(4,6),List(3,8))
  val m7 = List(List(99))

  println(extractColumn(m1,3))
  println(removeColumn(m1,1))
  println(transpose(m1))
  println(matrixMultiply(m2,m3))
  println(matrixMultiply(m4,m5))
//
//  println(determinant(List(List(6,1,1),List(4,-2,5),List(2,8,7))))
//  println(determinant(m6))
//  println(determinant(m7))
//  println(determinant(List()))

}