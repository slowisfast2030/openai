const fs = require('fs');

// const stream = fs.createReadStream('file.txt');

// stream.on('data', function(chunk) {
//     const lines = chunk.toString().split('\n');
//     for(let i = 0; i < lines.length; i++){
//        console.log(i+1, lines[i]);
// }
// })


fs.readFile('file.txt', 'utf-8', (err, data) => {
    if (err) throw err;
  
    const lines = data.trim().split('\n');
  
    lines.forEach((line, index) => {
      console.log(`Line ${index + 1}: ${line}`);
    });

  });