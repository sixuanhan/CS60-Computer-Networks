## Exercise 1
### a
The IP address of packetbender.com is 71.19.146.5.
Using Autonomous System Lookup, The Autonomous System Number is 47066, whose name is PRGMR.

### b
```bash
(base) ➜  ~ traceroute -P icmp packetbender.com
traceroute to packetbender.com (71.19.146.5), 64 hops max, 72 byte packets
 1  10.134.80.1 (10.134.80.1)  8.563 ms  6.121 ms  6.755 ms
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * * *
 8  * * *
 9  * * *
10  * * *
11  * * *
12  * * *
13  * * *
14  * * *
15  packetbender.vm.tornadovps.net (71.19.146.5)  225.671 ms  245.405 ms  256.288 ms
 ```
**15** Hops separate my machine from the host packetbender.com.

### c
```bash
(base) ➜  ~ echo f004n7k | md5 | cut -c1-8
53da9c84

(base) ➜  ~ echo -n "ID=53da9c84" | xxd -p
49443d3533646139633834

(base) ➜  ~ ping -c 1 71.19.146.5 -p 49443d3533646139633834 -m 45
```

After testing for ttl, I find that there is a token when ttl = 45. 

Data: 49443d353364613963383449443d353364613963383449443d353364613963383449443d353364613963383449443d35

TOKEN=G4mJxm0d


## Exercise 2
```bash
(base) ➜  ~ traceroute -m 2 8.8.8.8
```
Gives Type 11 Code 0.

```bash
(base) ➜  ~ ping -c 1 8.8.8.8
```
Gives Type 0 Code 0.


## Exercise 3
```python
message = bytes([9, 0, 255, ord('f'), ord('0'), ord('0'), ord('4'), ord('n'), ord('7'), ord('k')])
```

### UDP
Found valid source port: 2699

Response: Hello sixuan, your token is: 42f4d9e0

### TCP
Found valid source port: 2106

Response: Hello sixuan, your token is: 6b8f2831
