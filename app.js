const udev = require("udev");
const monitor = udev.monitor();
console.clear();
// console.log(udev.list()); // this is a long list :)

monitor.on('add', function(device) {
  if (device.DEVNAME.indexOf("/dev/sd") == 0 && device.DEVTYPE.indexOf("disk") == 0) {
    console.log(device.DEVNAME);
    console.log(device.ID_SERIAL_SHORT);
    console.log(device);
  }
});

monitor.on('remove', function(device) {
  console.log('removed ' + device);
});
