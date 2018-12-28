# lgtraceroute
lgtraceroute module that performs route-server or looking glass traceroute for provided IP address

Module can be imported by other scripts to validate hops in traceroute paths.
```
Example:

$ python3 lgtraceroute.py 8.8.8.8
Try: traceroute ttl 16 no-resolve 8.8.8.8
>traceroute 8.8.8.8 is running in background -- Please wait


--- JUNOS 17.1R1-S1 built 2017-04-07 08:21:13 UTC
traceroute ttl 16 no-resolve 8.8.8.8
exit
rviews@route-server.ip.att.net> traceroute ttl 16 no-resolve 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 16 hops max, 48 byte packets
 1  12.0.1.203  0.870 ms  0.783 ms  1.042 ms
 2  12.122.131.202  6.285 ms  3.799 ms  4.041 ms
     MPLS Label=31209 CoS=1 TTL=0 S=1
 3  12.122.131.202  3.839 ms  3.735 ms  8.515 ms
     MPLS Label=31209 CoS=1 TTL=1 S=1
 4  12.122.105.105  3.656 ms  3.841 ms  3.621 ms
 5  12.255.10.192  3.770 ms  3.623 ms 12.255.10.194  4.303 ms
 6  * * *
 7  209.85.240.227  4.578 ms 209.85.241.23  4.315 ms 209.85.245.191  4.344 ms
 8  8.8.8.8  3.856 ms  4.208 ms  4.308 ms

rviews@route-server.ip.att.net> exit


$ python3 lgtraceroute.py 8.8.8.8 --ttl 10
Try: traceroute ttl 10 no-resolve 8.8.8.8
>traceroute 8.8.8.8 is running in background -- Please wait


--- JUNOS 17.1R1-S1 built 2017-04-07 08:21:13 UTC
traceroute ttl 10 no-resolve 8.8.8.8
exit
rviews@route-server.ip.att.net> traceroute ttl 10 no-resolve 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 10 hops max, 48 byte packets
 1  12.0.1.203  41.529 ms  0.760 ms  10.351 ms
 2  12.122.131.202  6.656 ms  3.810 ms  3.825 ms
     MPLS Label=31209 CoS=1 TTL=0 S=1
 3  12.122.131.202  3.850 ms  3.895 ms  3.990 ms
     MPLS Label=31209 CoS=1 TTL=1 S=1
 4  12.122.105.105  3.611 ms  3.723 ms  3.652 ms
 5  12.255.10.194  4.908 ms  3.870 ms 12.255.10.192  4.615 ms
 6  108.170.248.1  5.308 ms 108.170.248.65  4.460 ms 108.170.248.97  4.017 ms
 7  108.170.237.206  4.458 ms 72.14.234.64  6.147 ms 216.239.62.168  6.329 ms
 8  108.170.238.195  4.416 ms 72.14.239.67  5.478 ms 209.85.243.193  4.086 ms
 9  8.8.8.8  4.232 ms  6.261 ms  4.389 ms

rviews@route-server.ip.att.net> exit
```

```
# Importing lgtraceroute as a module
In [1]: from lgtraceroute import lgtraceroute

In [2]: result = lgtraceroute('8.8.8.8')
Try: traceroute ttl 16 no-resolve 8.8.8.8
>traceroute 8.8.8.8 is running in background -- Please wait

In [3]: print(result)


--- JUNOS 17.1R1-S1 built 2017-04-07 08:21:13 UTC
traceroute ttl 16 no-resolve 8.8.8.8
exit
rviews@route-server.ip.att.net> traceroute ttl 16 no-resolve 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 16 hops max, 48 byte packets
 1  12.0.1.203  1.045 ms  0.736 ms  0.613 ms
 2  12.122.131.202  7.075 ms  3.816 ms  3.999 ms
     MPLS Label=31209 CoS=1 TTL=0 S=1
 3  12.122.131.202  3.779 ms  3.945 ms  3.894 ms
     MPLS Label=31209 CoS=1 TTL=1 S=1
 4  12.122.105.105  3.829 ms  3.726 ms  3.711 ms
 5  12.255.10.192  3.903 ms 12.255.10.194  4.121 ms  4.054 ms
 6  * * *
 7  209.85.243.193  4.914 ms 209.85.246.195  5.099 ms 108.170.228.135  4.889 ms
 8  8.8.8.8  4.069 ms  4.366 ms  4.401 ms

rviews@route-server.ip.att.net> exit
```
