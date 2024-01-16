Basic benchmark load test with server being run on 2 core cpu and 2 gb ram
Result 1 for 1 lakh request on / endpoint with logger enabled with 100 concurrent request
```bash
ab -n 100000 -c 100 http://localhost:8080/
```

Benchmarking localhost (be patient)

Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        Python/3.9
Server Hostname:        localhost
Server Port:            8080

Document Path:          /
Document Length:        13 bytes

Concurrency Level:      100
Time taken for tests:   177.757 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      19300000 bytes
HTML transferred:       1300000 bytes
Requests per second:    562.56 [#/sec] (mean)
Time per request:       177.757 [ms] (mean)
Time per request:       1.778 [ms] (mean, across all concurrent requests)
Transfer rate:          106.03 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   3.3      0     175
Processing:     3  177  68.9    164     763
Waiting:        3  148  59.7    136     626
Total:          3  178  69.2    164     763

Percentage of the requests served within a certain time (ms)
  50%    164
  66%    188
  75%    208
  80%    222
  90%    267
  95%    311
  98%    355
  99%    416
 100%    763 (longest request)

 During the test cpu was getting hitting 96% to 98%

Result 2 for 1 lakh request on /goodbye endpoint with logger enabled with 10 concurrent request
```bash
ab -n 100000 -c 10 http://localhost:8080/goodbye
```
 
 Benchmarking localhost (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        Python/3.9
Server Hostname:        localhost
Server Port:            8080

Document Path:          /goodbye
Document Length:        15 bytes

Concurrency Level:      10
Time taken for tests:   188.122 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      19700000 bytes
HTML transferred:       1500000 bytes
Requests per second:    531.57 [#/sec] (mean)
Time per request:       18.812 [ms] (mean)
Time per request:       1.881 [ms] (mean, across all concurrent requests)
Transfer rate:          102.26 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0      20
Processing:     1   19  11.6     16     273
Waiting:        1   16  10.8     13     269
Total:          1   19  11.6     16     273

Percentage of the requests served within a certain time (ms)
  50%     16
  66%     19
  75%     21
  80%     23
  90%     28
  95%     38
  98%     55
  99%     68
 100%    273 (longest request)