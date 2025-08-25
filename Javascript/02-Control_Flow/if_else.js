// IF-ELSE STATEMENTS IN JAVASCRIPT

let age = 18;

if (age > 18) {
    console.log("You are an adult.");
} else if (age === 18) {
    console.log("You just became an adult!");
} else {
    console.log("You are a minor.");
}

// Truthy & Falsy demo
let value = 0; // falsy value
if (value) {
    console.log("Truthy");
} else {
    console.log("Falsy"); // this will run
}
