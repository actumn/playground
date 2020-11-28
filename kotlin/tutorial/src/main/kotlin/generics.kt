fun main(args: Array<String>) {
    var obj = GenericsExample("JAVA")
    var obj1 = GenericsExample(10)

    println(obj)
    println(obj1)
}

class GenericsExample<T>(input:T) {
    init {
        println("I am getting called with the value $input")
    }
}
