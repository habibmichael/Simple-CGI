#! /usr/bin/perl
use LWP::Simple;

#HEADER
print "Content-type: text/html\n";
print "Server-Software:",$ENV{'SERVER_NAME'},"\n";
print "Server-Port:",$ENV{'SERVER_PORT'},"\n";
print "Server-Protocol: ",$ENV{'SERVER_PROTOCOL'},"\n";
print "Content-Length:",$ENV{'CONTENT_LENGTH'},"\n";
print "Remote-Addr: ",$ENV{'REMOTE_ADDR'},"\n";
print "\n\n";

#Body - Few Links to Projects
print "<html><head>";
print "<link rel='stylesheet' href='simple.css'> <title>Simple CGI</title></head>";
print "<h1 id='main_title'> My Simple CGI </h1><body><div id='projects'>";
print "<h3 id='project_list_title'>Fun Projects</h3><ul>";
print "<li><a href = 'http://github.com/mh122354/VR-Frogger'>VR Frogger Game";
print "</a></li><li><a href = 'http://github.com/mh122354/Space-Shooter'>Space";
print "Shooter Game</a></li><li><a href='http://github.com/mh122354/7MinuteWorkout'>7 Minute Workout";
print "</a></li></ul></div>";


#Get Query String
$query =  $ENV{'QUERY_STRING'};
#Turn string into list
@values = split(/&/,$query);

print "<h3 id='query_string'>Query String List</h3><div id='q_list'><ol id='list'>";
foreach $i (@values){
	($field_name,$data)=split(/=/,$i);
	print "<li><b>Field</b>: $field_name";
	if($data){
		print", <b>Data</b>: $data</li>";
		}
	else{
		print"</li>";		
	}
	}
print "</div></ol></body></html>";
exit(0);
