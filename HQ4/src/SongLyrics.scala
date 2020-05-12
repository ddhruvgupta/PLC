import scala.io.Source
import scala.collection.mutable.Map


object SongLyrics {

  def readLines(fname: String  ): List[(List[String],Int)] = {
    val s = Source.fromFile(fname).getLines
    val lines =
      for (line <- s) yield (line.toUpperCase().split("[.;! ]").toList,line.split("[.;! ]").length)
    lines.toList
//    print(lines)
  }

  def constructMap(lines: List[(List[String],Int)]): Map[String,List[Int]] = {


    def helper(lines : List[String], index: Int , m :Map[String,List[Int]]) ={

      for( a <- 0 until lines.length -1){
        if (m contains lines(a)) m(lines(a)) = m(lines(a)) ++ List(index + a +1)
        else m(lines(a)) = List(index + a+1)

//        print(lines(a), " ", index, " ", a)
      }

      if (m contains lines(lines.length -1))
        m(lines(lines.length -1)) = m(lines(lines.length -1)) ++ List(-(index +lines.length ))
      else
        m(lines(lines.length -1)) = List(-(index +lines.length))


    }

    var fc = Map[String,List[Int]]() withDefaultValue List()

    var end = List[Int]()
    lines.foreach(line => {end = end ++ List(line._2) })
    val temp = end.scan(0)(_ + _)
//    print(temp)
    val lines_withindex = lines.zipWithIndex


    lines_withindex map ( line => {
//      print(line._2)
      helper(line._1._1,temp(line._2), fc)
    })

    fc
  }

  def printMap(m: Map[String,List[Int]]): Unit = {
    def ilist_to_string(xs: List[Int]): String = xs match {
      case Nil => "[]"
      case y::Nil => y.toString
      case y::ys => y.toString+", "+ilist_to_string(ys)
    }
    for ((k,v) <- m) println(k + "\t["+ilist_to_string(v)+"]")
  }

  def displaySong(m: Map[String,List[Int]]): Unit = {
    var temp = m map (i => i._2 map (j => (j,i._1)))

    var a = temp.flatten.toArray
    var b = Array[(Int, String)]()
    var breaks = List[Int]()
    a.foreach(i => {
      if (i._1<0){
        breaks = breaks ++ List(Math.abs(i._1))
        b = b :+ (Math.abs(i._1),i._2)
      }else{
        b = b :+ (Math.abs(i._1),i._2)
      }

    })
    b = b.sortBy(_._1)
    var out = new StringBuilder();
    b.foreach( t => {
      if (breaks contains(t._1))
        out ++= s"${t._2}\n"
      else
        out ++= s"${t._2} "

    })

    print(out)
  }
//
  def numUniqueWords(m: Map[String, List[Int]]): Int = {
    m.size
  }

  def mostFrequentWord(m: Map[String, List[Int]]): String = {
    var max = 0
    var out = ""
    val k = m.keys

    k.foreach(i => if (m(i).length > max){ max = m(i).length; out = i})

    out
  }

  def main(args: Array[String]): Unit = {
    val m = constructMap(readLines(args(0)))
    //val m = constructMap(readLines( "song1.txt"))


    println("\nMap:\n")
    printMap(m)
    println("\nSong:\n")
    displaySong(m)
    println("")
    println("The number of unique words in the lyric is: "+ numUniqueWords(m).toString)
    println("")
    println("Most frequent word: "+mostFrequentWord(m))
    println("")
  }

}