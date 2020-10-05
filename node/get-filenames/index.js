const path = require("path");
const fs = require("fs")

const genFileNameArray = (pathname) => {
  const nameArray = [];
  fs.readdir(pathname, {}, (_, files) => {
    for (var i = 0; i < files.length; i++) {
      nameArray.push(files[i].replace('.svg', ''))
    }
    console.log(nameArray)
  })
}

genFileNameArray('/Users/jose/Downloads/first')