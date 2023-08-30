<?php  
//Create the variable

$connexion_time = date("Y-m-d H:i:s");
$protocol = $_SERVER['SERVER_PROTOCOL'];
$ip = $_SERVER['REMOTE_ADDR'];
$ip2 = $_SERVER['HTTP_X_FORWARDED_FOR'];
$port = $_SERVER['REMOTE_PORT'];
$agent = $_SERVER['HTTP_USER_AGENT'];
$ref = $_SERVER['HTTP_REFERER'];
$hostname = gethostbyaddr($_SERVER['REMOTE_ADDR']);
 
//Display the text and the variable

echo "If you are seeing this page that mean that everything work !" . "<br><br>";
echo "Time: " . $connexion_time . "<br>";
echo "Protocol: " . $protocol . "<br>";
echo "Ip local: " . $ip . "<br>";
echo "Public Ip: " . $ip2 . "<br>";
echo "Port: " . $port . "<br>";
echo "User agent: " . $agent . "<br>";
echo "HTTP_REFERER: " . $ref . "<br>";
echo "hostname: " . $hostname . "<br>";

?>