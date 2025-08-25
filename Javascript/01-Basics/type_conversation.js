// TYPE CONVERSION IN JAVASCRIPT

// String to Number
let strNum = "123";
let num = Number(strNum);
console.log(typeof num, num); // number 123

// Number to String
let n = 456;
let str = String(n);
console.log(typeof str, str); // string "456"

// Boolean Conversion
console.log(Boolean(1)); // true
console.log(Boolean(0)); // false
console.log(Boolean("")); // false
console.log(Boolean("hello")); // true

// Implicit Conversion (Type Coercion)
console.log("5" + 1); // "51" (string concatenation)
console.log("5" - 1); // 4 (number subtraction)
console.log("5" * "2"); // 10
