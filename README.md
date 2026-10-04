## Optimizing Ignition Using JMX and VisualVM

You can use these resouces to help convert visual vm traces into a flame graph.

#### Instructions:

Add in the following lines into your Ignition gateway conf:


wrapper.java.additional.2=-Dcom.sun.management.jmxremote=true 
wrapper.java.additional.3=-Dcom.sun.management.jmxremote.port=1234 
wrapper.java.additional.4=-Dcom.sun.management.jmxremote.rmi.port=1234 
wrapper.java.additional.5=-Dcom.sun.management.jmxremote.local.port=1235 
wrapper.java.additional.6=-Dcom.sun.management.jmxremote.authenticate=false 
wrapper.java.additional.7=-Dcom.sun.management.jmxremote.ssl=false 


Notice that there is a number after each additional parameter.  These numbers must be unique in the gateway conf.

It is also important that these parameters are put into the ignition.conf AFTER the existing wrapper.java.additional parameters.

Different gateways may have different parameters depending on when they were installed and what versions were updated.


Once you take a sample, take a "snapshot".

In the snapshot screen, export nps file for backup.  Then export forward calls.


Once exported, you then process the data to make it into a flame graph.

Two steps need to happen.

1. Run the file through the parse_stack_optimized.py and save the results to a file.

IE: python3 parse_stack_optimized.py exampleForwardCalls.csv > myParsedFile

2. Run the saved file through the perl script 

IE: ./flamegraph.pl myParsedFile > flame.svg


Open the flame.svg file in any svg viewer.  Chrome works great.



Thank you to IA for creating a great product and thank you to Brendan Gregg for creating a great viewer for processing stack traces. https://github.com/brendangregg/FlameGraph
