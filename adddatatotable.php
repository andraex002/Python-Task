<?php
$servername = "localhost:3306";
$username = "root";
$password = "Denisalore100";
$dbname = "task_python";


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO Employer (firstname, lastname, age, job, salary, bonus, totalsalary)
VALUES ('Andra', 'Finta', '23', 'Engineer', '100', '50', '150');";
$sql .= "INSERT INTO Employer (firstname, lastname, age, job, salary, bonus, totalsalary)
VALUES ('John', 'Pop', '25', 'Engineer', '100', '50', '150');";
$sql .= "INSERT INTO Employer (firstname, lastname, age, job, salary, bonus, totalsalary)
VALUES ('Akriti', 'Abdugal', '30', 'Engineer', '200', '20', '220');";
$sql .= "INSERT INTO Employer (firstname, lastname, age, job, salary, bonus, totalsalary)
VALUES ('Maria', 'Glass', '27', 'Manager', '200', '50', '250');";;
$sql .= "INSERT INTO Employer (firstname, lastname, age, job, salary, bonus, totalsalary)
VALUES ('Stefan', 'Milcher', '35', 'IT_Manager', '200', '50', '250');";
$sql .= "INSERT INTO Employer (firstname, lastname, age, job, salary, bonus, totalsalary)
VALUES ('Cristine', 'England', '45', 'Sales', '100', '50', '150');";
$sql .= "INSERT INTO Employer (firstname, lastname, age, job, salary, bonus, totalsalary)
VALUES ('Orsolya', 'Bor', '40', 'Developer', '200', '50', '250');";


if ($conn->multi_query($sql) === TRUE) {
  echo "New records created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>