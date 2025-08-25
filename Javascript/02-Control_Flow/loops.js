// LOOPS IN JAVASCRIPT

// for loop
for (let i = 0; i < 5; i++) {
    console.log("For Loop:", i);
}

// while loop
let count = 0;
while (count < 3) {
    console.log("While Loop:", count);
    count++;
}

// do-while loop
let num = 0;
do {
    console.log("Do-While Loop:", num);
    num++;
} while (num < 2);

// for...of loop (arrays)
const fruits = ["apple", "banana", "cherry"];
for (let fruit of fruits) {
    console.log("Fruit:", fruit);
}

// for...in loop (objects)
const person = { name: "Alice", age: 25 };
for (let key in person) {
    console.log(key, ":", person[key]);
}
