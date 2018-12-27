function getData() {
    return new Promise(function (resolve, reject) {
        var data = 100;
        resolve(data);
    });
};

function getDataError() {
    return new Promise(function (resolve, reject) {
        reject(new Error('Request is failed'));
    });
};

getData()
.then(data => console.log(data))
.then(getDataError)
.then(() => console.log('end.'))
.catch(error => {
    console.log('error')
});