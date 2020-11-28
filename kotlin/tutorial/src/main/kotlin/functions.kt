fun main(args:Array<String>) {
    val mylambda:(String)->Unit = {s:String->print(s)}
    val v:String = "TutorialsPoint.com"
    mylambda(v)
    myFun(v, mylambda)
}

fun myFun(a:String, action:(String)->Unit) {
    print("Heyyy!!!")
    action(a)
}
