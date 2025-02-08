import * as promptSync from 'prompt-sync';
const prompt = promptSync();
const x = parseFloat(prompt('Enter a number: '));
const y = parseFloat(prompt('Enter another number: '));
console.log('Choose an operation:');
console.log('1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Modulus');
const choice = prompt('Enter your choice (1/2/3/4/5): ');
let result: number;
switch (choice) {
    case '1':
        result = x + y;
        console.log(`Addition of ${x} and ${y} is ${result}`);
        break;
    case '2':
        result = x - y;
        console.log(`Subtraction of ${x} and ${y} is ${result}`);
        break;
    case '3':
        result = x * y;
        console.log(`Multiplication of ${x} and ${y} is ${result}`);
        break;
    case '4':
        if (y !== 0) {
            result = x / y;
            console.log(`Division of ${x} and ${y} is ${result}`);
        } else {
            console.log('Error: Division by zero is not allowed.');
        }
        break;
    case '5':
        result = x % y;
        console.log(`Modulus of ${x} and ${y} is ${result}`);
        break;
    default:
        console.log('Invalid choice. Please select a valid operation.');
        break;
}
