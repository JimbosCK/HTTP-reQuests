const http = require('http')

const options = {
    hostname: 'localhost',
    port: 3000,
    path: '/',
    method: 'GET',
    headers:{
        'name': 'Jimbos'
    },
};

const callBack = function(response){
    let body = '';
    response.on('data', function(data){
        body += data;
    });

    response.on('end', function(){
        console.log(body);
    })
}

const req = http.request(options, callBack);


req.end();

