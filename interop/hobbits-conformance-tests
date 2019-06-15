# Conformance testing procedure

![hct](hct.png)

### Test 1: Ping/Pong
  1) conformance app sends a ping with a random payload of bytes
  2) sample app receives the ping and returns the payload in the pong
  3) conformance app tests the payload sent vs the payload received.  
    match -> success  
    mismatch -> fail 

### Test 2: Port Test
  1) conformance app dials the sample app's tcp port
      open -> success
      closed -> fail

### Test 3:  Send/Rcv Msg 
  1) conformance app sends a message to sample app
  2) sample app receives message and returns payload in a reply message
  3) conformance app tests the payload sent vs the payload received.  
    match -> success  
    mismatch -> fail 
