const fs = require('fs');

const stream = fs.createReadStream('file.txt');

stream.on('data', function(chunk) {
    const lines = chunk.toString().split('\n');
    for(let i = 0; i < lines.length; i++){
       console.log(i+1, lines[i]);
}
})
