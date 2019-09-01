// https://javascript.info/promise-chaining
// promise-chain
/*
new Promise((resolve, reject) => {
    setTimeout(() => resolve(1), 1000);
}).then((result) => {
    console.log(result);
    return result * 2;
}).then((result) => {
    console.log(result);
    return result * 2;
}).then((result) => {
    console.log(result);
    return result * 2;
});
*/

// error here.
/*
let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve(1), 1000);
});

promise.then((result) => {
    console.log(result);
    return result * 2;
});
promise.then((result) => {
    console.log(result);
    return result * 2;
});
promise.then((result) => {
    console.log(result);
    return result * 2;
});
*/

// handler return a promise
new Promise((resolve, reject) => {
    setTimeout(() => resolve(1), 1000);
}).then((result) => {
    console.log(result);
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve(result * 2), 1000);
    });
}).then((result) => {
    console.log(result);
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve(result * 2), 1000);
    });
}).then((result) => {
    console.log(result);
});



