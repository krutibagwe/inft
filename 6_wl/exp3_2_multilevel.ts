class Arithmetic{
    num1: number;
    num2: number;
    constructor(num1: number, num2: number){
        this.num1 = num1;
        this.num2 = num2;
    }
    add(): number{
        return this.num1 + this.num2;
    }
}
class Power extends Arithmetic{
    num3: number;
    constructor(num1: number, num2: number, num3: number){
        super(num1, num2);
        this.num3 = num3;
    }
    power(): number{
        return Math.pow(this.num1, this.num3);
    }
}
class Square extends Power{
    square(): number{
        return Math.pow(this.num1, 2);
    }
}
let obj1 = new Square(2, 3, 5);
console.log("Addition: " + obj1.num1 + " + " + obj1.num2 + " = " + obj1.add());
console.log("Power: " + obj1.num1 + " raised to the power of " + obj1.num3 + ": " + obj1.power());
console.log("Square: Square of " + obj1.num1 + " is " + obj1.square());
