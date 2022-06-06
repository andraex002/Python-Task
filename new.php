<?php
$servername = "localhost:3306";
$username = "root";
$password = "Denisalore100";
$dbname = "task_python";


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "CREATE TABLE Department (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30) NOT NULL,
user VARCHAR(30) NOT NULL
)";

if ($conn->query($sql) === TRUE) {
  echo "Table Employer created successfully";
} else {
  echo "Error creating table: " . $conn->error;
}

$conn->close();
?>