object ControlStrucutres {

def main(args: Array[String]) = {
 
 ifStrucutres()
 forStrucutre()
 matchStrucutre()
 whileStrucutre(1)
}

// this function reviews the if statement in scala3 
def ifStrucutres() = {
  var x = 20
  var y = 20
  if x < y then 
   println("x is less than y")
  else if x == y then 
     println("X is equal to y")
   else
    println("x is greater then y")
}

def forStrucutre() = {

val nums: List[Int] = List(1, 2, 3, 4, 5, 6, 7)
for numbers <- nums do
    println(numbers)

// using yield for list comprehension

val doublelist: List[Int] = for numbers <- nums yield numbers * 2

println(doublelist)


val fruits = List("apple", "banana", "lime", "orange")

val fruitLength: List[Int] =for fruit<- fruits if fruit.length > 4 yield fruit.length

println("Fruits with length greater than 4 are: " + fruitLength)

}


def matchStrucutre() = {

    val x = "apple"
    x match 
        case "apple" => println("apple")
        case "banana" => println("banana")
        case "orange" => println("orange")
        case _ => println("other")
    
    
    val fruit= x match 
        case "apple" => "apple"
        case "banana" => "banana"
        case "orange" => "orange"
        case _ => "other"
    
    println(fruit)


}

def whileStrucutre(x: Int) = {

var h = x
while 
h < 10
do
  println(h)
  h = h + 1
}






}