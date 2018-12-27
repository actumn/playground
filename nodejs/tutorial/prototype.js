function Person() {}

Person.prototype.eyes = 2;
Person.prototype.noses = 1;

var kim = new Person();
var park = new Person();


console.log(kim.eyes);
console.log(kim.noses);

console.log(park.eyes);
console.log(park.noses);
