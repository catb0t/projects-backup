#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# This software is used to gather basic environmennt data
# with the Rapsberry Pi Model B. This software was sepecifically
# designed for one single system

import os
import sys
import re
#import Adafruit_DHT
#import Adafruit_BMP.BMP085 as BMP085
#import MySQLdb
import time

# make sure script is run as root
euid = os.geteuid()
if euid != 0:
    print('Script not started as root. Running sudo...')
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    os.execlpe('sudo', *args)

# create timestamp
timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

print('Gathering data...')
# grab humidity data from DHT22 sensor
sensor = 22
pin = 4
#humidity, temperature_DHT22 = Adafruit_DHT.read_retry(sensor, pin)

# grab barometric data
#sensor = BMP085.BMP085()
#temperature_bmp9985 = sensor.read_temperature()
#pressure_bmp9985  = (sensor.read_pressure()/100)

# grab outside temperature from ds18b20
f = open("/home/cat/zeros.img", "r")#'/sys/bus/w1/devices/28-00043c9677ff/w1_slave', 'r')
lines = f.read()
f.close()
#match = re.search('t=(-?[0-9]+)', lines)
#temperature_18b20 = (float(match.group(1))/1000)

# grab cpu temperature
cpuTempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
cpu_temp = float(cpuTempFile.read())/1000
cpuTempFile.close()

# calculate aproximate dew point
#DewPoint = ((humidity / 100) ** 0.125) * (112 + 0.9 * temperature_18b20) + (0.1 * temperature_18b20) - 112

print('Opening database connection')
# connecting to MySQL database and creating cursor
# all queries are executed by the cursor
#db = MySQLdb.connect(host="HOST", user="USER", passwd="PASSWORD", db="DATABASE")
#cur = db.cursor()

print('Preparing SQL statement')
#sql = (('INSERT INTO `weather_data` (`t_out`, `t_out_wall`, `t_case`, `t_cpu`, `humidity`, `pressure`, `dewpoint`) VALUES ({:.2f}, {:.1f}, {:.2f}, {:.2f}, {:.2f}, {:.0f}, #{:.2f});').format(temperature_18b20, temperature_DHT22, temperature_bmp9985, cpu_temp, humidity, pressure_bmp9985, DewPoint))

#print('Executing SQL statement')
##cur.execute(sql)
##print('Commiting SQL statement')
##db.commit()
##print('Closing database connection')
##cur.close()
#db.close()

#print('Acquired data:')
#print(timestamp)
#print('temperature_18b20   =     {:0.2f} °C').format(temperature_18b20)
#print('temperature_dht22   =     {:0.1f} °C').format(temperature_DHT22)
#print('temperature_bmp9985 =     {:0.2f} °C').format(temperature_bmp9985)
#print('temperature_cpu     =     {:0.2f} °C').format(cpu_temp)
#print('humidity_dht22      =     {:0.1f}%').format(humidity)
#print('pressure_bmp9985    =     {:0.0f} hPa').format(pressure_bmp9985)
#print('dew_point           =     {:.2f} °C').format(DewPoint)