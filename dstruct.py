#!/usr/bin/python3

##      _     _                   _
##   __| |___| |_ _ __ _   _  ___| |_
##  / _` / __| __| '__| | | |/ __| __|
## | (_| \__ \ |_| |  | |_| | (__| |_
##  \__,_|___/\__|_|   \__,_|\___|\__|
##  _ _|_ _ ._    _  _  
## (_\/|_(_)|_)\/(_|(/_ 
##   /      |  /  _|    
##
## dstruct
## monitor and wipe usb devices 
## written in python 
## (c) 2017 by cytopyge
##

import pyudev
from subprocess import call


context = pyudev.Context()

path = pyudev.Devices.from_sys_path


#TODO def enumerate(device.device_node)


# enumerate at startup
for device in context.list_devices(subsystem='block'):
  if 'ID_FS_TYPE' in device:
    if device.device_node[5:7] == 'sd':
    # set dd parameters; input file, output file, block size, status
        dd_if = '/dev/urandom'
        dd_of = device.device_node
        dd_bs = '1M'
        dd_status = 'progress'


  print(device.sys_name)
  call(['dd', 'if=' + dd_if, 'of=' + dd_of, 'bs=' + dd_bs, 'status=' + dd_status])
  print('completed')
  exit


monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('block')


# enumerate at device connection
for device in iter(monitor.poll, None):
  if 'ID_FS_TYPE' in device:
    if device.action == 'add':
        if device.device_node[5:7] == 'sd':
        # set dd parameters; input file, output file, block size, status
            dd_if = '/dev/urandom'
            dd_of = device.device_node
            dd_bs = '1M'
            dd_status = 'progress'


  print(device.sys_name)
  call(['dd', 'if=' + dd_if, 'of=' + dd_of, 'bs=' + dd_bs, 'status=' + dd_status])
  print('completed')
  exit


#TODO led status light control
#TODO connect multiple devices
#TODO error: 'dd: failed to open '/dev/sda': Read-only file system'
