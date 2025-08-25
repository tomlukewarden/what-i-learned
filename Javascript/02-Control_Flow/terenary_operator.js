// TERNARY OPERATOR IN JAVASCRIPT
let age = 20;
let message = (age >= 18) ? "You can vote." : "You cannot vote.";
console.log(message);

// Nested ternary
let score = 85;
let grade = (score >= 90) ? "A" :
            (score >= 75) ? "B" :
            (score >= 50) ? "C" : "F";
console.log("Grade:", grade);
