<?php



// Display Errors in PHP and SQL for debugging
ini_set('display_errors', '1'); // php
ini_set('display_startup_errors', '1'); // php
error_reporting(E_ALL); // php
echo mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT); // for mySql



function SQLConnect()
{
  $servername = "database-2.cfdkhifsqoch.us-east-1.rds.amazonaws.com";
  $username = "admin";
  $password = "password";

  // Create connection
  $conn = new mysqli($servername, $username, $password);

  // Check connection
  if ($conn->connect_error)
  {
  die("Connection failed: " . $conn->connect_error);
  }
  echo "Connected successfully</br>";

  return $conn;

}

function SQLEndConnect($conn)
{
  $conn->close();
}


if ($_SERVER['REQUEST_METHOD'] === 'POST')
{

    $name = $_POST["name"];
    $favicecream = $_POST["favicecream"];

    $conn = SQLConnect();

    // create the database and table - "IF NOT EXSISTS" will prevent issues if it already is present
    $conn->query("CREATE DATABASE IF NOT EXISTS testdb");
    $conn->query("USE testdb");
    $conn->query("CREATE TABLE  IF NOT EXISTS testtable (name VARCHAR(30), favicecream VARCHAR(30))");

    $result = $conn->query("INSERT INTO testtable (name, favicecream) VALUES ('" . $name . "', '" . $favicecream . "')");

    if($result === TRUE)
    {
    echo 'Successfully Created Entry</br>';
    }
    else
    {
    echo "Failed to Create Entry</br>";
    }
    ?>

    <!DOCTYPE html>
    <html>
      <head>
        <title>Week 1 - Day 4-5 Database Test</title>
      </head>
      <body>
        <p style="color:purple;">Thank you for submitting an icecream flavor.</p>
      </body>
      </html>
    <?php
}
else  // request method is GET
{

?>
<!DOCTYPE html>
<html>
  <head>
    <title>Week 1 - Day 4-5 Database Test</title>
  </head>
  <body>

    <div style="border:solid blue 1px;margin:10px;">
      <?php
        $conn = SQLConnect();


        $result = $conn->query("SELECT * FROM testdb.testtable");

        if ($result->num_rows > 0)
        {
           // output data of each row
           while($row = $result->fetch_assoc())
           {
            echo "Name: " . $row["name"]. " - Favorite Icecream: " . $row["favicecream"] . "<br>";
           }
        }
        else
        {
        echo "Failed to read Db entries </br>";

        }
      ?>
    </div>

    <form method="post" action="./index.php">
      Enter your name: <input type="text" name="name" value=""></br>
      Enter your favorite icecream: <input type="text" name="favicecream" value=""></br>
      <input type="submit" name="submit" value="Submit">
    </form>
  </body>
</html>
<?php
}

?>
