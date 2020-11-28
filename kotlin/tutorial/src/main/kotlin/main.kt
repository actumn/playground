
fun main(args: Array<String>) {
    var a: Int = 100000
    val d: Double = 100.00
    val f: Float = 100.00f
    val l: Long = 10000000004
    val s: Short = 10
    val b: Byte = 1


    println("Your Int Value is "+a);
    println("Your Double  Value is "+d);
    println("Your Float Value is "+f);
    println("Your Long Value is "+l);
    println("Your Short Value is "+s);
    println("Your Byte Value is "+b);

    val letter: Char = 'A'
    println("$letter")

    val letter2: Boolean = true
    println("Your character value is $letter2")

    var rawString: String = "I am Raw String!"
    val escapedString: String = "I am escaped String!\n"

    println("Hello! $escapedString")
    println("Hey!! $rawString")

    val numbers: IntArray = intArrayOf(1, 2, 3, 4, 5)
    println("Hey!! I am array Example"+numbers[2])


    val numbersMutable: MutableList<Int> = mutableListOf(1, 2, 3)
    val readOnlyView: List<Int> = numbersMutable
    println("My mutable list-"+numbersMutable)
    numbersMutable.add(4)
    println("My mutable list after addition -"+numbersMutable)
    println(readOnlyView)

    val items = listOf(1, 2, 3, 4)
    println("First Element of our list--"+items.first())
    println("Last Element of our list--"+items.last())
    println("Even Numbers of our List--"+items.filter { it % 2 == 0 })

    val readWriteMap = hashMapOf("foo" to 1, "bar" to 2)
    println(readWriteMap["foo"])

    val strings = hashSetOf("a", "b", "c", "c")
    println("My Set Values are"+strings)

    val i:Int = 2
    for (j in 1..4)
        print(j)

    if (i in 1..10) {
        println("We found your number - "+i)
    }

    val aInt:Int = 5
    val bInt:Int = 2
    val max = if (aInt > bInt) aInt else bInt
    println("Maximum of a or b is "+max)

    val x:Int = 5
    when (x) {
        1 -> println("x==1")
        2 -> println("x==2")
        else -> {
            println("x is neither 1 nor 2")
        }
    }

    val items2 = listOf(1, 2, 3, 4)
    for (i in items2)
        println("values of the array"+i)

    val items3 = listOf(1, 22, 83, 4)
    for ((index, value) in items3.withIndex()) {
        println("the element at $index is $value")
    }


    var x2:Int = 0
    println("Example of While Loop-")
    while(x2<=10) {
        println(x2)
        x2++
    }
    println("The value is--"+doubleMe(10))

    myLabel@ for (x in 1..10) {
        if(x == 5) {
            println("I am inside if block with value"+x+"\n-- hence it will close the operation")
            break@myLabel
        } else {
            println("I am inside else block with value"+x)
            continue@myLabel
        }
    }

    val obj = myClass()
    obj.printMe()

    val demo = Outer.Nested().foo()
    println(demo)

    val demo2 = Outer().InnerNested().foo()
    println(demo2)

    var programmer: Human = object:Human {
        override fun think() {
            println("I am an example of Annonymous Inner Class")
        }
    }
    programmer.think()

    val person1 = Person("TutorialsPoint.com", 15)
    println("First Name = ${person1.firstName}")
    println("Age = ${person1.age}")

    val internalExample = InternalExample()
    internalExample.doSomething()
}

fun doubleMe(x:Int): Int {
    return 2 * x;
}

class myClass {
    private var name: String = "Tutorials.point"

    fun printMe() {
        println("You are at the best Learning website named-"+name)
    }
}

class Outer {
    class Nested {
        fun foo() = "Welcome to The TutorialsPoint.com"
    }

    private val welcomeMessage: String = "Welcome to the TutorialsPoint.com"
    inner class InnerNested {
        fun foo() = welcomeMessage
    }
}

interface Human {
    fun think()
}


class Person(val firstName: String, var age: Int) {
}

class HUman(val firstName: String, var age: Int) {
    var message:String = "Hey!!!"
    constructor(name: String, age: Int, message: String):this(name, age) {

    }
}

open class ABC {
    open fun think() {
        println("Hey!! I am thinking.")
    }
}
class BCD: ABC() {
    override fun think() {
        println("I Am from Child")
    }
}

interface ExampleInterface {
    var myVar: Int
    fun absMethod(): String
    fun hello() {
        println("Hello ther,e Welcometo TutorialsPoint.Com!")
    }
}
class InterfaceImp: ExampleInterface {
    override var myVar: Int = 25
    override fun absMethod() = "Happy Learning"
}

class InternalExample {
    internal val i = 1
    internal fun doSomething() {
    }
}

class PublicExample {
    val i = 1
    fun doSomething() {

    }
}
