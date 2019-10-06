# Computer Networking Problem P31

# Suppose that the five measured SampleRTT values (see Section 3.5.3 ) are 106 ms, 120 ms, 140 ms, 90 ms, and 115 ms. 
# Compute the EstimatedRTT after each of these SampleRTT values is obtained, using a value of alpha=0.125
# and assuming that the value of EstimatedRTT was 100 ms just before the first of these five samples were obtained. 
# Compute also the DevRTT after each sample is obtained, assuming a value of beta=0.25 
# and assuming the value of DevRTT was 5 ms just before the first of these five samples was obtained. 
# Last, compute the TCP TimeoutInterval after each of these samples is obtained.


alpha = 0.125
beta = 0.25

SampleRTT_list = [106,120,140,90,115]
EstimatedRTT =100
DevRTT = 5
for SampleRTT in SampleRTT_list:
    EstimatedRTT = (1-alpha)*EstimatedRTT + alpha * SampleRTT
    DevRTT = (1-beta) *DevRTT + beta * abs(SampleRTT-EstimatedRTT)
    TimeoutInterval  = EstimatedRTT+ 4* DevRTT
    print("When obtaining "+str(SampleRTT)+", \n\t EstimatedRTT = "+str(EstimatedRTT)+", DevRTT = "+str(DevRTT)+ ", TimeoutInterval = "+str(TimeoutInterval))
