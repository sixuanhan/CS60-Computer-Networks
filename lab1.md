## Exercise 1

**Collaboration Statement**: I discussed with Hugo Fang and Yuanhao Chen.

### a
The IP address of packetbender.com is 71.19.146.5.

Using Autonomous System Lookup, The Autonomous System Number is 47066, whose name is PRGMR.

Connectivity: upstream Hurricane Electric LLC, Tier 1 AS: AS701 Verizon, AS3356 Lumen, etc.

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
(base) ➜  ~ sudo hping3 -c 1 -1 -C 13 192.168.64.3
```
Gives Type 14 Code 0.

The above is captured in [capture1.pcap](/capture1.pcap).

```bash
(base) ➜  ~ traceroute -m 2 8.8.8.8
```
Gives Type 11 Code 0.

```bash
(base) ➜  ~ ping -c 1 8.8.8.8
```
Gives Type 0 Code 0.

```bash
(base) ➜  ~ traceroute dartmouth.edu
```
Gives Type 3 Code 3.

```bash
ubuntu@inventive-curassow:~$ sudo hping3 -c 1 -1 -C 8 -K 1 172.26.83.109
```
Gives Type 0 Code 1.

The above are captured in [capture2.pcap](/capture2.pcap).


## Exercise 3
```bash
[sixuan@thepond ~]$ netstat -lantu
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:106             0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:603             0.0.0.0:*               LISTEN
tcp        0    224 129.170.212.8:106       10.135.21.96:55863      ESTABLISHED
tcp        0      0 129.170.212.8:106       10.135.171.197:50479    ESTABLISHED
tcp        0      0 129.170.212.8:106       10.134.88.184:52910     ESTABLISHED
tcp        0      0 129.170.212.8:106       10.134.85.11:64485      ESTABLISHED
tcp        0      0 129.170.212.8:60492     129.170.212.8:603       CLOSE_WAIT
tcp        0      0 129.170.212.8:106       10.135.171.197:50344    ESTABLISHED
tcp6       0      0 :::106                  :::*                    LISTEN
udp        0      0 0.0.0.0:603             0.0.0.0:*
```
The bot listens at port 603.

```bash
[sixuan@thepond ~]$ nc localhost 603
12
Error: Message is not 10 bytes
000000000
Error: Message does not start with magic byte
```

Using `find_message.py`, looping over the first byte, the second byte, and the third byte, we get that the message should start with 9, 0, 255, and then include the netID.

```python
message = bytes([9, 0, 255, ord('f'), ord('0'), ord('0'), ord('4'), ord('n'), ord('7'), ord('k')])
```

### UDP
Using `find_port.py`, we loop over all ports from 2000 to 2999 and get:

Found valid source port: 2699

Response: Hello sixuan, your token is: 42f4d9e0

### TCP
Found valid source port: 2106

Response: Hello sixuan, your token is: 6b8f2831
