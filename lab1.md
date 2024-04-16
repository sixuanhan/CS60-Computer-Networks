## Exercise 1
### a

```bash
(base) ➜  ~ traceroute packetbender.com
traceroute to packetbender.com (71.19.146.5), 64 hops max, 52 byte packets
 1  10.133.160.1 (10.133.160.1)  8.164 ms  5.010 ms  7.713 ms
 ```

The IP address of packetbender.com is 71.19.146.5.
Using Autonomous System Lookup, The Autonomous System Number is 47066, whose name is PRGMR.

### b

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
