const http = require('http');

const server = http.createServer((req, res) =>{
    let name = req.headers['name'];
    res.end("Hello " + name)
});

server.listen(3000, () => {
    console.log("Server listening on http://localhost:3000");
});