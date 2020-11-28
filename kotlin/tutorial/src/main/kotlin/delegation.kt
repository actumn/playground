import kotlin.properties.Delegates
import kotlin.reflect.KProperty

interface Base {
    fun printMe()
}

class BaseImpl(val x: Int) : Base {
    override fun printMe() {
        println(x)
    }
}
class Derived(b: Base) : Base by b

fun main(args: Array<String>) {
//    var b = BaseImpl(10)
//    Derived(b).printMe()

//    println(myVar + " my dear friend")

    val user = User()
    user.name = "first"
    user.name = "second"
}


// Lazy is a lambda function which takes a property as an input and
// in return gives an instance of Lazy<T>,
// where <T> is basically the type of the properties it is using.
// Let us take a look at the following to understand how it works.
val myVar: String by lazy {
    "Hello"
}

class User {
    var name: String by Delegates.observable("Welcome to Tutorialspoint.com") {
        prop, old, new ->
        println("$old -> $new")
    }
}

class Example {
    var p: String by Delegate()
}
class Delegate {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): String {
        return "$thisRef, thank you for delegating '${property.name}' to me!"
    }
    operator fun setValue(thisRef: Any?, property: KProperty<*>, value: String) {
        println("$value has been assigned to '${property.name} in $thisRef.'")
    }
}
