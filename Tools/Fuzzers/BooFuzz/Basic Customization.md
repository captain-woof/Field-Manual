# Basic Customization

## [Target](https://boofuzz.readthedocs.io/en/stable/source/Target.html)
From [boofuzz.readthedocs.io](https://boofuzz.readthedocs.io/en/stable/source/Target.html#boofuzz.Target), Target() takes the following important parameters in its constructors:

- A 'connection' object (parameter name is 'connection')
- A repeater object (parameter name is 'repeater')

You can see all parameters in this declaration:
`class boofuzz.Target(connection, monitors=None, monitor_alive=None, max_recv_bytes=10000, repeater=None, **kwargs)`

#### Repeaters:

- **[TimeRepeater](https://boofuzz.readthedocs.io/en/stable/source/Target.html#boofuzz.repeater.TimeRepeater)**
Time-based repeater class. Starts a timer, and repeats until duration seconds have passed.

`class boofuzz.repeater.TimeRepeater(duration, sleep_time=0)`


*duration (float)* – The duration of the repitition.

*sleep_time (float)* – Time to sleep between repetitions.

- **[CountRepeater](https://boofuzz.readthedocs.io/en/stable/source/Target.html#countrepeater)**
Count-Based repeater class. Repeats a fixed number of times.

`class boofuzz.repeater.CountRepeater(count, sleep_time=0)`


*count (int)* – Total amount of packets to be sent. Important: Do not confuse this parameter with the amount of repetitions. Specifying 1 would send exactly one packet.

*sleep_time (float)* – Time to sleep between repetitions.

## [Connections](https://boofuzz.readthedocs.io/en/stable/user/connections.html)
Available:

- TCPSocketConnection
- UDPSocketConnection
- SSLSocketConnection
- RawL2SocketConnection
- RawL3SocketConnection
- SocketConnection (depreciated)
- SerialConnection

#### [TCPSocketConnection](https://boofuzz.readthedocs.io/en/stable/user/connections.html#tcpsocketconnection)
`class boofuzz.connections.TCPSocketConnection(host, port, send_timeout=5.0, recv_timeout=5.0, server=False)`

- *host (str)* – Hostname or IP adress of target system.

- *port (int)* – Port of target service.

- *send_timeout (float)* – Seconds to wait for send before timing out. Default 5.0.

- *recv_timeout (float)* – Seconds to wait for recv before timing out. Default 5.0.

- *server (bool)* – Set to True to enable server side fuzzing.

#### [UDPSocketConnection](https://boofuzz.readthedocs.io/en/stable/user/connections.html#udpsocketconnection)
`class boofuzz.connections.UDPSocketConnection(host, port, send_timeout=5.0, recv_timeout=5.0, server=False, bind=None, broadcast=False)`

- *host (str)* – Hostname or IP adress of target system.

- *port (int)* – Port of target service.

- *send_timeout (float)* – Seconds to wait for send before timing out. Default 5.0.

- *recv_timeout (float)* – Seconds to wait for recv before timing out. Default 5.0.

- *server (bool)* – Set to True to enable server side fuzzing.

- *bind (tuple (host, port))* – Socket bind address and port. Required if using recv().

- *broadcast (bool)* – Set to True to enable UDP broadcast. Must supply appropriate broadcast address for send() to work, and ‘’ for bind host for recv() to work.


