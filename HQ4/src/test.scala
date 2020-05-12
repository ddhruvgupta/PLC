class test {

  case class Date(month: Int, day: Int, year: Int)

  def leapYear(d: Date): Boolean =
    (d.year % 4 == 0) && !(d.year % 100 == 0 && d.year % 400 != 0)

  def to_string(d: Date): String = {
    val sMonths = "01January:02February:03March:04April:05May:06June:" ++
      "07July:08August:09September:10October:11November:12December:"
    val index1 = sMonths.indexOf(if (d.month < 10) "0" + d.month.toString
    else "" + d.month.toString)
    val index2 = sMonths.indexOf(":", index1)
    val sMonth = sMonths.substring(index1 + 2, index2)
    d.day.toString + " " + sMonth + ", " + d.year.toString
  }

  def tomorrow(d: Date): Date = {
    val leap = leapYear(d)
    val l1 = List(1, 3, 5, 7, 8, 10, 12)
    val l2 = List(4, 6, 9, 11)
    var day = d.day
    var month = d.month
    var year = d.year

    if (l1.contains(d.month)) {

      day = (d.day + 1) % 31

      if (day == 0) {
        day = 1
        month = (d.month + 1) % 12
        if (month == 1) {
          year = d.year + 1
        }
      }
      Date(month, day, year)
    } else if (l2.contains(d.month)) {
      day = (d.day + 1) % 30


      if (day == 0) {
        day = 1
        month = d.month + 1
      }

      Date(month, day, year)
    } else {

      if (leap) {
        day = (d.day + 1) % 29
        if (day == 0) {
          day = 1
          month = 3
        }

      } else {
        day = (d.day + 1) % 28
        if (day == 0) {
          day = 1
          month = 3
        }

      }

      Date(month, day, year)

    }


  }

  def main(args: Array[String]): Unit = {
    println(to_string(tomorrow(Date(12, 31, 2019))))
  }

}