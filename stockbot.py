#!/usr/bin/env python
import sys
from time import sleep
import socket
import string
import ystockquote
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
   data = s.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      s.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( 'Stocktellerbot quit' ) != -1:
      s.send ( "PRIVMSG %s :%s\r\n" % (CHANNELINIT, 'Fine, bye'))
      s.send ( 'QUIT\r\n' )
   if data.find ( 'hi Stocktellerbot' ) != -1:
      s.send ( 'PRIVMSG %s :%s\r\n' % (CHANNELINIT, 'Hiya' ))
   ##if data.find ( 'hello botty' ) != -1:
      ##s.send ( 'PRIVMSG #paul :I already said hi...\r\n' )
   ##if data.find ( 'KICK' ) != -1:
      ##s.send ( 'JOIN #paul\r\n' )
   ##if data.find ( 'cheese' ) != -1:
     ## s.send ( 'PRIVMSG #paul :WHERE!!!!!!\r\n' )
   ##if data.find ( 'slaps botty' ) != -1:
      ##s.send ( 'PRIVMSG #paul :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
   if data.find ( 'Stock update pl0x' ) != -1:
      stockprice=ystockquote.get_price('GOOG')
      s.send("PRIVMSG %s :%s\r\n" % (CHANNELINIT, stockprice))

   print data

while 1:
	readbuffer=readbuffer+s.recv(1024)
 	temp=string.split(readbuffer, "\n")
 	readbuffer=temp.pop( )

for line in temp:
	line=string.rstrip(line)
	line=string.split(line)

if(line[0]=="PING"):
	s.send("PONG %s\r\n" % line[1])
