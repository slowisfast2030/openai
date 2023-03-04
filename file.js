const fs = require('fs');

// const stream = fs.createReadStream('file.txt');

// stream.on('data', function(chunk) {
//     const lines = chunk.toString().split('\n');
//     for(let i = 0; i < lines.length; i++){
//        console.log(i+1, lines[i]);
// }
// })


// fs.readFile('file.txt', 'utf-8', (err, data) => {
//     if (err) throw err;
  
//     const lines = data.trim().split('\n');
  
//     lines.forEach((line, index) => {
//       console.log(`Line ${index + 1}  ${line}`);
//     });

//   });

// 您可以使用模板字符串来对齐输出。
// 在模板字符串中，您可以使用占位符${}来插入变量的值。
// 将${index + 1}放在固定宽度的字段中，
// 例如${index + 1}，可以使每行的行号对齐。
  fs.readFile('file.txt', 'utf-8', (err, data) => {
    if (err) throw err;
  
    const lines = data.trim().split('\n');
  
    lines.forEach((line, index) => {
      console.log(`Line ${String(index + 1).padStart(3)}: ${line}`);
    });
  
  }); // 这段代码的输出格式已对齐