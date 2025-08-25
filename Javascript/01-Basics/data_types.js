// DATA TYPES IN JAVASCRIPT

// Primitive types
let str = "Hello";      // String
let num = 42;           // Number
let bool = true;        // Boolean
let undef;              // Undefined
let nul = null;         // Null
let sym = Symbol("id"); // Symbol
let bigIntNum = 123456789012345678901234567890n; // BigInt

console.log(typeof str); // "string"
console.log(typeof num); // "number"
console.log(typeof bool); // "boolean"
console.log(typeof undef); // "undefined"
console.log(typeof nul); // "object" (quirk in JS)
console.log(typeof sym); // "symbol"
console.log(typeof bigIntNum); // "bigint"

// Reference types
let obj = { name: "Alice", age: 25 };
let arr = [1, 2, 3];
let func = function() { return "Hello World"; };

console.log(typeof obj); // "object"
console.log(typeof arr); // "object" (arrays are objects)
console.log(typeof func); // "function"
