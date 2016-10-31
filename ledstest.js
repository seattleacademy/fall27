var nodeimu = require('nodeimu');
var IMU = new nodeimu.IMU();

var PythonShell = require('python-shell');

PythonShell.run('helloworld.py', function (err, results) {
  if (err) throw err;
});

IMU.getValue(function(err, data) {
    if (err) throw err;
    console.log(data);
});

