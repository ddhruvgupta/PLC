/*
@Author Dhruv Gupta
Csc 6330 HQ2
 */
object Bags {
  type Bag = Int => Int
  val bound = 99

  // returns true if elem is in b, false otherwise
  // e.g. b1 = {(1,1),(3,2),(5,2)}
  // contains(b1,3) = true, contains(b1,4) = false
  def contains(b: Bag, elem: Int): Boolean =
    b(elem) > 0
  // returns number of occurrences of elem in b
  // e.g. b1 = {(1,1),(3,2),(5,2)}
  // count(b1,3) = 2, count(b1,5) = 2, count(b1,9) = 0, count(b1,88) = 0
  def count(b: Bag, elem: Int): Int =
    b(elem)

  // returns an empty bag
  def emptyBag: Bag =
    x => 0
  // inserts element elem into bag b
  // e.g. b1 = {(1,1),(3,2),(5,2)}, b2 = {(1,3),(4,3),(5,2)}
  // add(b1,3) = {(1,1),(3,3),(5,2)}
  // add(b2,85) = {(1,3),(4,3),(5,2),(85,1))}
  def add(b: Bag, elem: Int): Bag =
    x => if (x == elem) 1 + count(b,x) else count(b,x)

  // returns the union of b1 and b2
  // b1 union b2 = { (x,c) | (x,c1) in b1, (x,c2) in b2, c is larger of c1 and c2 }
  // e.g. b1 = {(1,1),(3,2),(5,2)} b2 = {(1,1),(3,1),(4,1),(5,2)}
  // union(b1,b2) = {(1,1),(3,2),(4,1),(5,2)}
  def union(b1: Bag, b2: Bag): Bag =
    x => if (b1(x) > b2(x)) b1(x) else b2(x)
  // returns the sum of b1 and b2
  // b1 sum b2 = { (x,c) | (x,c1) in b1, (x,c2) in b2, c = c1+c2 }
  // e.g. b1 = {(1,1),(3,2),(5,2)} b2 = {(1,1),(3,1),(4,1),(5,2)}
  // sum(b1, b2) = {(1,2),(3,3),(4,1),(5,4)}
  def sum(b1: Bag, b2: Bag): Bag =
    x => b1(x) + b2(x)
  // returns the intersection of b1 and b2
  // b1 intersect b2 = { (x,c) | (x,c1) in b1, (x,c2) in b2, c is smaller of c1 and c2 }
  // e.g. b1 = {(1,1),(3,2),(5,2)} b2 = {(1,1),(3,1),(4,1),(5,2)}
  // intersect(b1,b2) = {(1,1),(3,1),(5,2)}
  def intersect(b1: Bag, b2: Bag): Bag =
    x => if (b1(x) < b2(x)) b1(x) else b2(x)
  // returns the difference of b1 and b2, b1-b2
  // b1 difference b2 = { (x,c) | (x,c1) in b1, (x,c2) in b2, c=c1-c2 if positive else 0 }
  // e.g. b1 = {(1,1),(3,2),(5,2)} b2 = {(1,1),(3,1),(4,1),(5,2)}
  // difference(b1,b2) = {(3,1)}
  def difference(b1: Bag, b2: Bag): Bag =
    x => b1(x) - b2(x)
  // returns true is b1 is a subbag of b2, false otherwise
  // b1 is a subbag of b2 if every item in b1 appears fewer or equal times in b2
  // e.g. b1 = {(1,1),(3,2),(5,2)} b2 = {(1,1),(3,1),(4,1),(5,2)} b3 = {(1,1),(5,1)}
  // subbag(b3,b1) = true
  // subbag(b1,b2) = false
  def subbag(b1: Bag, b2: Bag): Boolean = {
    def helper(x: Int): Boolean = {
      if (x > bound)
        true
      else if (count(b1,x) > count(b2,x))
        false
      else
        helper(x+1)
    }
    helper(0)
  }

  // returns true if b1 is equal to b2, false otherwise
  // b1 is equal to b2 if every item in universal set appears equally in b1 and b2
  // e.g. b3 = {(1,1),(5,1)} b4 = {(1,1),(5,1)}
  // equal(b3,b4) = true

  def equal(b1: Bag, b2: Bag): Boolean =
    {
      def helper(x : Int): Boolean = {
        if(x > bound)
          return true
        else if(contains(b1,x) && contains(b2,x))
          if (b1(x) == b2(x))
            helper(x+1)
          else
            false
        else if(contains(b1,x) && !contains(b2,x))
          false
        else if(!contains(b1,x) && contains(b2,x))
          false
        else
          helper(x+1)

      }

      helper(0)
    }

    // returns the unique elements in b as a bag with all counts set to 1
    // basically return a bag with all counts reset to 1
    // b2 = {(1,1),(3,1),(4,1),(5,2)}
    // support(b2) = {(1,1),(3,1),(4,1),(5,1)}
    def support(b: Bag): Bag = {
      def helper(x: Int, cbag: Bag): Bag = {
        if (x > bound)
          cbag
        else if (contains(b,x))
          helper(x+1,add(cbag,x))
        else
          helper(x+1,cbag)
      }
      helper(0,emptyBag)
    }

    // returns a subset of elements of b that satisfy the predicate p
    // and their counts satisfy predicate q
    // b5 = {(1,3),(4,3),(5,2)}
    // filter(b5,x => x%2!=0, x => x > 2) = {(1,3)}

    def filter(b: Bag, p: Int => Boolean, q: Int => Boolean): Bag ={
      def add_2(b: Bag, elem: Int , v : Int): Bag =
        x => if (x == elem) v + count(b,x) else count(b,x)

      def helper(x: Int, cbag: Bag): Bag = {
        if (x > bound)
          cbag
        else if (p(x) && q(b(x)) )
          helper(x+1,add_2(cbag, x, b(x)))
        else
          helper(x+1,cbag)
      }

      helper(0,emptyBag)
    }


    // returns true if all elements of b satisfy predicate p
    // and their counts satisfy predicate q
    // b5 = {(1,3),(4,3),(5,2)}
    // forall(b5,x => x < 10,x = > x < 3) = false
    // forall(b5,x => x < 10,x = > x < 4) = true
    def forall(b: Bag, p: Int => Boolean, q: Int => Boolean): Boolean ={

      def helper(x: Int): Boolean = {
        if (x > bound)
          true
        else if(contains(b,x))
          if(p(x) && q(b(x)))
            helper(x+1)
          else
          false
        else
          helper(x+1)
      }

      helper(0)
  }

    // returns true if at least one element of b satisfies predicate p
    // and its count satisfes predicate q
    // b5 = {(1,3),(4,3),(5,2)}
    // exists(b5,x => x>4, x => x < 3) = true
    // exists(b5,x => x>4, x => x > 4) = false
    def exists(b: Bag, p: Int => Boolean, q: Int => Boolean): Boolean ={


    def helper(x : Int): Boolean = {
        if(x > bound)
          false
        else if (p(x) && q(b(x)))
          true
        else helper(x+1)
    }

      helper(0)
  }

    // returns a new bag obtained by applying f to each element of b
    // and g to the count of the element and forming a bag of the results
    // e.g. b = {(1,5),(2,3),(3,9)}, f = (x => x*x), g = (x => 2*x)
    // map(b,f,g) = {(1,10),(4,6),(9,18)}
    def map(b: Bag, f: Int => Int, g: Int => Int): Bag ={

      def add_2(b: Bag, elem: Int , v : Int): Bag =
        x => if (x == elem) v + count(b,x) else count(b,x)

      def helper(x: Int, cBag: Bag): Bag ={
      if (x > bound)
        cBag
      else if(contains(b,x)) {
        helper(x+1, add_2(cBag, f(x), g(b(x))))
      } else{
        helper(x+1, cBag)
      }

    }

      helper(0,emptyBag)
  }

    def toString(b: Bag): String = {
      val xs = for (i  <-  0 to bound if contains(b, i)) yield (i,count(b,i))
      xs.mkString("{", ",", "}")
    }

    def printBag(b: Bag): Unit = {
      println(toString(b))
    }

  }