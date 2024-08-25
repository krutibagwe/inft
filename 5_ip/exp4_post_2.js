function Animal(name, age) {
    this.name = name;
    this.age = age;
  }
  
  Animal.prototype.describe = function() {
    return `${this.name} is a ${this.species} and is ${this.age} years old.`;
  };
  
  function Dog(name, age, breed) {
    Animal.call(this, name, age);
    this.breed = breed;
  }
  
  Dog.prototype = Object.create(Animal.prototype);
  Dog.prototype.constructor = Dog;
  Dog.prototype.species = 'Dog';
  
  Dog.prototype.describe = function() {
    return `${this.name} is a ${this.species}, breed is ${this.breed}, and is ${this.age} years old.`;
  };
  
  Dog.prototype.bark = function() {
    return `${this.name} says woof!`;
  };
  
  function Cat(name, age, color) {
    Animal.call(this, name, age);
    this.color = color;
  }
  
  Cat.prototype = Object.create(Animal.prototype);
  Cat.prototype.constructor = Cat;
  Cat.prototype.species = 'Cat';
  
  Cat.prototype.describe = function() {
    return `${this.name} is a ${this.species} with ${this.color} fur and is ${this.age} years old.`;
  };
  
  Cat.prototype.meow = function() {
    return `${this.name} says meow!`;
  };
  
  const myDog = new Dog('Tommy', 5, 'Labrador');
  const myCat = new Cat('Cairo', 3, 'Black');
  
  console.log(myDog.describe());
  console.log(myDog.bark());
  
  console.log(myCat.describe());
  console.log(myCat.meow());
