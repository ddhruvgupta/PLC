object Driver extends App {
  import Bags._


    val b1 = add(add(add(add(add(emptyBag,1),3),5),3),5)
    val b2 = add(add(add(add(add(emptyBag,1),4),5),5),3)
    val b3 = add(add(emptyBag,1),5)
    val b4 = add(add(emptyBag,1),5)
    print("b1 = ")
    printBag(b1)
    print("b2 = ")
    printBag(b2)
    print("b3 = ")
    printBag(b3)
    print("b4 = ")
    printBag(b4)
    print("contains(b1,1) = ")
    println(contains(b1,1))
    print("contains(b1,9) = ")
    println(contains(b1,9))
    print("b1 union b2 = ")
    printBag(union(b1,b2))
    print("b1 intersect b2 = ")
    printBag(intersect(b1,b2))
    print("b1 difference b2 = ")
    printBag(difference(b1,b2))
    print("b1 sum b2 = ")
    printBag(sum(b1,b2))
    print("b3 equal b4 = ")
    println(equal(b3,b4))
  print("b1 equal b4 = ")
  println(equal(b1,b4))
    print("b3 subbag b1 = ")
    println(subbag(b3,b1))
    print("b1 subbag b2 = ")
    println(subbag(b1,b2))
    print("support(b2) = ")
    printBag(support(b2))
    print("map(b1,x=>x*x,x=>2*x) = ")
    printBag(map(b1,x=>x*x,x=>2*x))
    val b5 = add(add(add(add(add(add(add(add(emptyBag,1),5),1),4),1),4),4),5)
    print("b5 = ")
    printBag(b5)
    print("filter(b5,x=>x%2!=0,x=>x>2) = ")
    printBag(filter(b5,x=>x%2!=0,x=>x>2))
    print("forall(b5,x=>x<10,x=>x<3) = ")
    println(forall(b5,x=>x<10,x=>x<3))
    print("forall(b5,x=>x<10,x=>x<4) = ")
    println(forall(b5,x=>x<10,x=>x<4))
    print("exists(b5,x=>x>4,x=>x<3) = ")
    println(exists(b5,x=>x>4,x=>x<3))
    print("exists(b5,x=>x>4,x=>x>4) = ")
    println(exists(b5,x=>x>4,x=>x>4))


}