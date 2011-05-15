#!/usr/bin/env python
import sys
from time import sleep
import socket
import string
import ystockquote
import parser
HOST="irc.freenode.net"
PORT=6667
NICK="Stocktellerbot"
IDENT="Stockbot"
REALNAME="Stockbot"
OWNER="Pranav_rcmas"
CHANNELINIT="#noobchannel"
readbuffer=""
s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN :%s\r\n" % CHANNELINIT)


##s.send("PRIVMSG %s :%s\r\n" % (CHAN, "..."))

##sleep(10);

##s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Duh.."))


##stockprice=ystockquote.get_price('GOOG')


##s.send("PRIVMSG %s :%s\r\n" % (CHANNELINIT, stockprice))

while True:
   data = s.recv ( 500 )
   print data
   if data.find ( 'PING' ) != -1:
      s.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( 'Stocktellerbot quit' ) != -1:
      s.send ( "PRIVMSG %s :%s\r\n" % (CHANNELINIT, 'Fine, bye'))
      s.send ( 'QUIT\r\n' )
   if data.find ( 'hi Stocktellerbot' ) != -1:
      s.send ( 'PRIVMSG %s :%s\r\n' % (CHANNELINIT, 'Hiya' ))
   ##if data.find ( 'stock update pl0x' ) != -1:
     ## s.send("PRIVMSG %s :%s\r\n" % (CHANNELINIT, "Which stock?"))
   if data.find("PRIVMSG") != -1:
      parser.parsemsg(data)
      data=data.rstrip() #remove trailing 'rn'
      data=data.split()
      if data[3].find(":") != -1:
         data[3]=data[3].strip(':') 
         stockprice=ystockquote.get_price(data[3])
         print data[3]
         s.send("PRIVMSG %s :%s\r\n" % (CHANNELINIT, stockprice))
   

while 1:
	readbuffer=readbuffer+s.recv(1024)
 	temp=string.split(readbuffer, "\n")
 	readbuffer=temp.pop( )

for line in temp:
	line=string.rstrip(line)
	line=string.split(line)

if(line[0]=="PING"):
	s.send("PONG %s\r\n" % line[1])
