## Networked Technology ##

**Transport Control Protocol (TCP)** -- built on top of **Internet Protocol (IP)** to provide a pipeline

TCP Connections also called **Sockets** and have **Port Connections** e.g. Port 80 = HTTP

Only need 3 lines of python:
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )

Application protocols include mail and web

**Hypertext Transfer Protocol (HTTP)** -- invented for the web to retrieve HTML form of standards

Getting data from the server uses a GET command

American Standard Code for Information Exchange -- **ASCII**, use the ord() function to find the numeric value (ordinal)

**Unicode** universal way for different countries to exchange data.  UTF-8 is the most common option (1-4 bytes per character)

In Python3, everything is unicode, so no need to convert between string and unicode (as in Python 2).  However, Python 3 has a **byte string** type: x = b'abc'

Using sockets:  before sending, need to **encode()**, when receiving need to **decode()**

**urlib** is a library that does all of the socket work for us and makes web pages look like a file

**Web Scraping** uses Python as a web browser, can use it to gather data -- be careful of copyrighted information, biggest problem is parsing of HTML

Best library is **Beautiful Soup** -- free software