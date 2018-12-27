function getJSON() {
    return new Promise(function (resolve, reject) {
        var data = {'aa': 'bb'};
        resolve(data);
    });
};

function makeRequestPromise () {
    return getJSON().then(data => {
        console.log(data);
        return 'done';
    })
}

//makeRequestPromise().then(result => console.log(result));

const makeRequestAsync = async () => {
    console.log(await getJSON().then(() => 'getJson done'));
    return 'done';
}

makeRequestAsync().then(result => console.log(result))