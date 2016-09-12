#! /usr/bin/perl

print "Content-type: text/html\n";
print "Server-Software:",$ENV{'SERVER_NAME'},"\n";
print "Server-Port:",$ENV{'SERVER_PORT'},"\n";
print "Server-Protocol: ",$ENV{'SERVER_PROTOCOL'},"\n";
print "Content-Length:",$ENV{'CONTENT_LENGTH'},"\n";
print "Remote-Addr: ",$ENV{'REMOTE_ADDR'},"\n";
print "\n\n";
