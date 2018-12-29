class Polygon {
    constructor (height, width) {
        this.height = height;
        this.width = width;
    }
}

var Polygon2 = class {
    constructor (height, width) {
        this.height = height;
        this.width = width;
    }
}

var Polygon3 = class Polygon {
    constructor (height, width) {
        this.height = height;
        this.width = width;
    }
}

class StaticMem {
    static disp() {
        console.log("Static func called");
    }
}
var someObject = new Polygon();
var someObject2 = new Polygon2();
var someObject3 = new Polygon3(); 

StaticMem.disp();

class Shape {
    constructor (a) {
        this.Area = a;
    }
}
class Circle extends Shape {
    disp () {
        console.log("Area of ths circle: " + this.Area);
    }
}

var obj = new Circle(223);
obj.disp();


