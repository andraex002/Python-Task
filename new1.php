<?php
$servername = "localhost:3306";
$username = "root";
$password = "Denisalore100";
$dbname = "task_python";


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO department (name, user)
VALUES ('Engineering', 'andex');";
$sql .= "INSERT INTO department (name, user)
VALUES ('Manager', 'mariaex');";
$sql .= "INSERT INTO department (name, user)
VALUES ('Engineering', 'akrityex');";
$sql .= "INSERT INTO departments (name, user)
VALUES ('Engineering', 'johnex');";
$sql .= "INSERT INTO department (name, user)
VALUES ('Sales', 'christineengex');";
$sql .= "INSERT INTO department (name, user)
VALUES ('IT_Manager', 'stefanex');";
$sql .= "INSERT INTO department (name, user)
VALUES ('Developer', 'orsolyaex');";


if ($conn->multi_query($sql) === TRUE) {
  echo "New records created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>