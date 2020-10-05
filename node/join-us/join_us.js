const csv = require("csvtojson");
const fs = require("fs");
const file = "./join_us.csv";

const output = [];

const getJSON = async () => {
  await csv()
    .fromFile(file)
    .then((jsonObj)=>{
			jsonObj.map((item, index)=>{
				console.log("​getJSON -> id", index)
        const { responsibilities,requirements, mark, jobName, id, ...others } = item;
          output.push({
          id: index+1,
          jobName: `${jobName} ${mark}`,
          responsibilities: responsibilities.split("\n").filter(i => !!i),
          requirements: requirements.split("\n").filter(i => !!i),
          ...others,
        });
      })
    });
    const json = JSON.stringify(output);
    fs.writeFileSync("./rst.json", json, "utf8");
};

getJSON();
