object VariableDemo
{
    def main(args: Array[String]) = {
    

    //we try and use the various ways to declare variables in scala
    //var keyword is used for mutable variables
    // this is explicitly defining variable type
    var ten: String = "Ten";
    
    // val keyword is used for immutable variables
    val _ten = 10;
    //val (var1, var2)= Pair(23,"Twenty Three");

    println("The first variable defined: " + ten);
    println("The second variable defined: " + _ten);
    //print("The third variable defined", var1);
    //print("The fourth variable defined", var2);

    val nums: List[Int] = List(1,2,3,4,5);
    val words: List[String] = List("one", "two", "three", "four", "five");
    val numsAndWords: List[Any] = nums ::: words;
    println("The list of numbers and words: " + numsAndWords);
    println(s"The first element of the list is: ${numsAndWords.head}");

    }
}
