// VARIABLES IN JAVASCRIPT

// var - function-scoped, can be re-declared and updated
var nameVar = "Alice";
var nameVar = "Bob"; // allowed
console.log("var example:", nameVar);

// let - block-scoped, can be updated but NOT re-declared in same scope
let nameLet = "Charlie";
// let nameLet = "Dave"; // ❌ Error: Identifier 'nameLet' has already been declared
nameLet = "Dave"; // ✅ allowed
console.log("let example:", nameLet);

// const - block-scoped, cannot be reassigned
const nameConst = "Eve";
// nameConst = "Frank"; // ❌ Error: Assignment to constant variable
console.log("const example:", nameConst);

// Block scope demo
{
    var a = 1;
    let b = 2;
    const c = 3;
}
console.log(a); // ✅ Works
// console.log(b); // ❌ ReferenceError
// console.log(c); // ❌ ReferenceError
