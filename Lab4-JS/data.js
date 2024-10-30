const fs = require('fs');

function getData(filePath) {
    try {
        const data = fs.readFileSync(filePath, 'utf-8');
        const linesArray = data.split('\n');
        
        let array = [];

        for (let i = 0; i < linesArray.length; i++) {
            let line = linesArray[i].replace(/,/g, ".").split('\t');

            let x_i = Number(line[0]);
            let y_i = Number(line[1]);
            array.push([x_i, y_i]);
        }
        return array;

    } catch (error) {
        console.error('Ошибка при чтении файла:', error);
        return [];
    }
}

// // Пример использования
const filePath = 'cords.txt';
const lines = getData(filePath);
console.log(lines);
