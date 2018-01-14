const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('./Recycling.db');

db.serialize(function () {


db.run("INSERT INTO recycle VALUES(NULL, ?, ?)", ['CUP', '0']);
		
db.each("SELECT * FROM recycle", function (err, row) {
    console.log(row);
  });
});