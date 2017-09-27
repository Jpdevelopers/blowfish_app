<?php
 $servername = "localhost";
   $username = "root";
  $password = "paras123";
  
$pass=$_POST['pass'];
$uname=$_POST['uname'];


  $conn = mysqli_connect($servername, $username, $password,"minor");
session_start();
// Check connection
 if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
  } 
 $sql="select * from users where username='$uname' and password='$pass'"; 
$result = mysqli_query($conn, $sql);
 
if (mysqli_num_rows($result) > 0) {
    $row=mysqli_fetch_assoc($result);
    $_SESSION["user_id"] = $row["id"];
    header('Location: upload.php');
} else {
    echo mysqli_error($conn);
}



     mysqli_close($conn);
?>


