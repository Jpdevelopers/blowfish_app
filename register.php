<?php
 $servername = "localhost";
   $username = "root";
  $password = "paras123";
  
$name=$_POST['name'];
$uname=$_POST['uname'];
$pass=$_POST['pass'];
$keyval=$_POST['keyval'];

  $conn = mysqli_connect($servername, $username, $password,"minor");

// Check connection
 if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
  } 
  $sql="insert into users(name,username,password,keyval,keypath) values('$name','$uname','$pass','$keyval','')";

 
if (mysqli_query($conn, $sql)) {
    $last_id = mysqli_insert_id($conn);
    $path=$last_id.".png";
    $sql1 = "UPDATE users SET keypath='$path' WHERE id=$last_id";
    $res=mysqli_query($conn, $sql1);
    $tmp = exec('python script.py '.$keyval.' '.$last_id);
    $download_path=$last_id."_A.png";
    echo $tmp;

    if (headers_sent()) {
    echo 'HTTP header already sent';
} else {
    if (!is_file($download_path)) {
        header($_SERVER['SERVER_PROTOCOL'].' 404 Not Found');
        echo 'File not found';
    } else if (!is_readable($download_path)) {
        header($_SERVER['SERVER_PROTOCOL'].' 403 Forbidden');
        echo 'File not readable';
    } else {
        header($_SERVER['SERVER_PROTOCOL'].' 200 OK');
        header("Content-Type: image/png");
        header("Content-Transfer-Encoding: Binary");
        header("Content-Length: ".filesize($download_path));
        header("Content-Disposition: attachment; filename=\"".basename($download_path)."\"");
        ob_clean();
        readfile($download_path);
        @unlink($download_path);
        echo "success";
    }
}
} else {
    echo mysqli_error($conn);
}



     mysqli_close($conn);
?>