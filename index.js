const fs = require('fs');
const path = require('path');
const mergeFiles = require('merge-files');
let filesCollection = [];
const outputPath = __dirname + '/result.txt';
const directoriesToSkip = ['bower_components', 'node_modules', 'www'];

function readDirectorySynchronously(directory) {
    var currentDirectorypath = path.join(__dirname + directory);

    var currentDirectory = fs.readdirSync(currentDirectorypath, 'utf8');

    currentDirectory.forEach(file => {
        var fileShouldBeSkipped = directoriesToSkip.indexOf(file) > -1;
        var pathOfCurrentItem = path.join(__dirname + directory + '/' + file);
        if (!fileShouldBeSkipped && fs.statSync(pathOfCurrentItem).isFile()) {
            filesCollection.push(pathOfCurrentItem);
        }
        else if (!fileShouldBeSkipped) {
            var directorypath = path.join(directory + '/' + file);
            readDirectorySynchronously(directorypath);
        }
    });
}

async function start() {
    readDirectorySynchronously('/filters');
    console.log(filesCollection);
    const status = await mergeFiles(filesCollection, outputPath);
    console.log(status);
}

start();

