# subnet-calculator
simple script to generate lists of smaller subnets from larger for Class B subnets
class B subnet broken down
- first two octets are for the network
- last two octets are for the hosts
```
192.0.0.0/19
192.0 = network
0.0 = host
```


## How to run
- -s /26 flag is the smaller subnets to make
- -l 192.168.64.0/19 is the larger subnet to break down into smaller /26
```
RESML-1721798:subnet-calculator bvandy00$ python3.10 calculator.py -s /26 -l 192.168.64.0/19
192.168.64.0-26
192.168.64.64-26
192.168.64.128-26
192.168.64.192-26
192.168.65.0-26
192.168.65.64-26
192.168.65.128-26
192.168.65.192-26
etc...
etc...
```
