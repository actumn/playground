class Allen {
    var skills : String = "null"

    fun printMySkills() {
        print(skills)
    }
}

// Function Extension
fun Allen.addMySkills(a:Allen):String {
    var a4 = Allen()
    a4.skills = this.skills + " " + a.skills
    return a4.skills
}

// Object Extension
class A {
    companion object {
        fun show(): String {
            return("You are learning Kotlin from TutorialsPoint.com")
        }
    }
}
