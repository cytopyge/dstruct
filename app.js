const udev = require("udev");
const monitor = udev.monitor();
const exec = require('child_process').exec;
console.clear();

function wipe(sdb, id) {
  console.log(`whipe ${sdb}`);
  // const CMD = `dd command`;
  const CMD = `echo "dd commando wiping ${sdb}"`;
  let dd = exec(CMD);
  // DD output
  dd.stdout.on('data', function(data) {
    // TODO: LEDS
    console.log(`--> ${data}`);
  });
}

monitor.on('add', function(device) {
  console.log("add monitor");
  // New device
  if (device.DEVNAME.indexOf("/dev/sd") == 0 && device.DEVTYPE.indexOf("disk") == 0) {
    // console.log(device);
    wipe(device.DEVNAME, device.ID_SERIAL_SHORT)
  }
});

monitor.on('remove', function(device) {
  console.log('removed ' + device);
});
