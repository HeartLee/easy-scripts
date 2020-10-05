const csv = require("csvtojson");
const _ = require("lodash");
const fs = require("fs");
const file = "./table1.csv";

const dates = [];
const allData = [];
const lastResult = [];

const getJSON = async () => {
  await csv()
    .fromFile(file)
    .then(jsonObj => {
      jsonObj.map((item, index) => {
        const { name, code, ...others } = item;
        let rowData = {};
        _.values(others).map(moneyData => {
          if (moneyData !== "") {
            const curDate = moneyData.replace(
              /(\d+\.*\d+)(\()(\d+)(\))/,
              (match, p1, p2, p3) => {
                rowData[p3] = { [code]: p1 };
                // console.log(p1, p3);
              }
            );
            // if (index === 0) {
            //   console.log("TCL: getJSON -> curDate", curDate);
            // }
          }
        });
        allData.push(rowData);
        // console.log(others);
      });
      // console.log(allData);
      allData.map(zhaiquanInfo => {
        dates.push(_.keys(zhaiquanInfo));
      });
      const formatAllDates = [...new Set(_.flatten(dates))];
      formatAllDates.map(date => {
        let curObj = { date };
        allData.map(item => {
          if (item[date]) {
            curObj = { ...curObj, ...item[date] };
          }
        });
        lastResult.push(curObj);
      });
      console.log(lastResult);
    });

  // const json = JSON.stringify(output);
  // fs.writeFileSync("./rst.json", json, "utf8");
};

getJSON();
