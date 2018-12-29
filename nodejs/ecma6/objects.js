var identifier = {
    Key1: 'value',
    Key2 () {
        console.log('some function')
    },
    Key3: ['content1', 'content2']
}

var baz = { identifier }
var baz2 = { ...identifier }
console.log(baz.identifier)
console.log(baz2.Key1)

var myCar = new Object();
myCar.make = "Ford";
myCar.model = "Mustang";
myCar.year = 1987;

console.log(myCar["make"])
console.log(myCar["model"])
console.log(myCar["year"])


function someFunction () {
    this.proprty = "value";
}
var someObject = new someFunction();
console.log(someObject.proprty)

var roles = {
    type: 'admin',
    displayType () {
        console.log(this.type)
    }
}

roles.displayType();
var superRole = Object.create(roles);
superRole.displayType();

var guestRole = Object.create(roles);
guestRole.type ='Guest';
guestRole.displayType();
superRole.displayType();


var emp = { name: 'John', Id: 3 }
let { name, Id } = emp
console.log(name)
console.log(Id)