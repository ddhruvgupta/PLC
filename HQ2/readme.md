This is a programming assignment. You will complete various functions in the following implementation of the "Bag" data structure.

  type Bag = Int => Int
  val bound = 99
Bag is a data structure similar to a Set, but in which duplicates are allowed, i.e. a particular element may be present in the bag any number of times. Some examples of bags are given below:
  b1 = { 1, 3, 5, 3, 5 }
  b2 = { 1, 5, 1, 4, 1, 4, 4, 5 }
Another way to show these bags (with element and number of occurrences as a 2-tuple) is:
  b1 = { (1,1), (3,2), (5,2) }
  b2 = { (1,3), (4,3), (5,2) }
The above two notations are for human consumption. Internally, in our implementation, a bag is defined as a function from Int to Int, which records the number of occurrences for each item in the bag. We will assume that bags can contain any number of occurrences of positive integers from 0 to 99 inclusive, i.e. the universal set of items is bounded. The number 99 is an arbitrary choice.
The bag b1 above can be represented by the function that maps 0 to 0, 1 to 1, 2 to 0, 3 to 2, 4 to 0, 5 to 2, 6 to 0, and so on.

Similarly, bag b2 can be represented by the function that maps 0 to 0, 1 to 3, 2 to 0, 3 to 0, 4 to 3, 5 to 2, 6 to 0, and so on.

Here are the functions that you will have to implement (solutions to a few are given):

object Bags {
  type Bag = Int => Int
  val bound = 99

  // returns true if elem is in b, false otherwise
  // e.g. b1 = {(1,1),(3,2),(5,2)}
  // contains(b1,3) = true, contains(b1,4) = false
  def contains(b: Bag, elem: Int): Boolean = 

  // returns number of occurrences of elem in b
  // e.g. b1 = {(1,1),(3,2),(5,2)}
  // count(b1,3) = 2, count(b1,5) = 2, count(b1,9) = 0, count(b1,88) = 0
  def count(b: Bag, elem: Int): Int = 

  // returns an empty bag
  def emptyBag: Bag = 

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

  // returns the sum of b1 and b2
  // b1 sum b2 = { (x,c) | (x,c1) in b1, (x,c2) in b2, c = c1+c2 }
  // e.g. b1 = {(1,1),(3,2),(5,2)} b2 = {(1,1),(3,1),(4,1),(5,2)}
  // sum(b1, b2) = {(1,2),(3,3),(4,1),(5,4)}
  def sum(b1: Bag, b2: Bag): Bag = 

  // returns the intersection of b1 and b2
  // b1 intersect b2 = { (x,c) | (x,c1) in b1, (x,c2) in b2, c is smaller of c1 and c2 }
  // e.g. b1 = {(1,1),(3,2),(5,2)} b2 = {(1,1),(3,1),(4,1),(5,2)}
  // intersect(b1,b2) = {(1,1),(3,1),(5,2)}
  def intersect(b1: Bag, b2: Bag): Bag = 

  // returns the difference of b1 and b2, b1-b2
  // b1 difference b2 = { (x,c) | (x,c1) in b1, (x,c2) in b2, c=c1-c2 if positive else 0 }
  // e.g. b1 = {(1,1),(3,2),(5,2)} b2 = {(1,1),(3,1),(4,1),(5,2)}
  // difference(b1,b2) = {(3,1)}
  def difference(b1: Bag, b2: Bag): Bag =

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
  def equal(b1: Bag, b2: Bag): Boolean = {

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
  def filter(b: Bag, p: Int => Boolean, q: Int => Boolean): Bag = 

  // returns true if all elements of b satisfy predicate p 
  // and their counts satisfy predicate q
  // b5 = {(1,3),(4,3),(5,2)}
  // forall(b5,x => x < 10,x = > x < 3) = false
  // forall(b5,x => x < 10,x = > x < 4) = true
  def forall(b: Bag, p: Int => Boolean, q: Int => Boolean): Boolean = 

  // returns true if at least one element of b satisfies predicate p 
  // and its count satisfes predicate q
  // b5 = {(1,3),(4,3),(5,2)}
  // exists(b5,x => x>4, x => x < 3) = true
  // exists(b5,x => x>4, x => x > 4) = false
  def exists(b: Bag, p: Int => Boolean, q: Int => Boolean): Boolean = 

  // returns a new bag obtained by applying f to each element of b
  // and g to the count of the element and forming a bag of the results
  // e.g. b = {(1,5),(2,3),(3,9)}, f = (x => x*x), g = (x => 2*x) 
  // map(b,f,g) = {(1,10),(4,6),(9,18)}
  def map(b: Bag, f: Int => Int, g: Int => Int): Bag =

  def toString(b: Bag): String = {
    val xs = for (i  <-  0 to bound if contains(b, i)) yield (i,count(b,i))
    xs.mkString("{", ",", "}")
  }

  def printBag(b: Bag): Unit = {
    println(toString(b))
  }

}