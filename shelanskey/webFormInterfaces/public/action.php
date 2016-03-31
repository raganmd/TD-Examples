<?php 
$myfile = fopen("var.txt", w);
$txt = $_POST['json'];
fwrite($myfile,$txt);
fclose($myfile);
header('Location: working.html')
?>