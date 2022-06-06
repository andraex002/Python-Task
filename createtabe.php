<?php
$servername = "localhost:3306";
$username = "root";
$password = "Denisalore100";
$dbname = "task_python";


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "CREATE TABLE Employer (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
firstname VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
age INT(50),
job VARCHAR(30) NOT NULL,
salary INT(200),
bonus INT(50),
totalsalary INT(250)
)";

if ($conn->query($sql) === TRUE) {
  echo "Table Employer created successfully";
} else {
  echo "Error creating table: " . $conn->error;
}

$conn->close();
?>