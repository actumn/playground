// code from here: https://typescript-kr.github.io/pages/tutorials/TypeScript%20in%205%20minutes.html
interface Person {
  firstName: string;
  lastName: string;
}

class Student {
  fullName: string;
  constructor(public firstName: string, public middleInitial: string, public lastName: string) {
    this.fullName = firstName + " " + middleInitial + " " + lastName;
  }
}

function greeter(person: Person) {
  return `Hello, ${person.firstName} ${person.lastName}`
}

// let user = { firstName: "Jane", lastName: "User" };
let user = new Student("Jane", "M.", "User");

console.log(greeter(user));
