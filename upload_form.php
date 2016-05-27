<!DOCTYPE HTML>  
<html>
<head>
<style>
	body {
		background-color:#666666;
		}
	.error {color: #FF0000;}
	.legends {color: linen; font-size:18px}
	
	.inputs {
		float:right;
		}
		
	form {
		float:right;
		width:500px;
		}
		
	body{
		float:left;
		}
</style>
</head>
<body>  

<?php
// define variables and set to empty values
$firstNameErr = $lastNameErr = $genderErr = $deptErr = $classnumErr =$yearErr=$emailErr= "";
$firstName = $lastName = $gender = $comment = $dept = $classnum = $visitable =$year=$email= "";
$thankyou = "";
$errors = 0;

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  	// Test First Name
	if (empty($_POST["firstName"])) {
		$firstNameErr = "First Name is required";
		$errors++;
	} else {
		$firstName = test_input($_POST["firstName"]);
	}
	
	// Test Last Name
	if (empty($_POST["lastName"])) {
		$lastNameErr = "Last Name is required";
	$errors++;
	} else {
		$lastName = test_input($_POST["lastName"]);
	}
	
	// Test Department
	if (empty($_POST["dept"])) {
		$deptErr = "Department is required";
	} else {
		$dept = test_input($_POST["dept"]);
	}
	
	// Test Class number
	if (empty($_POST["classnum"])) {
		$classnumErr = "Class Number is required";
	} else {
		$classnum = test_input($_POST["classnum"]);
	}
	
	// handle comment
	if (empty($_POST["comment"])) {
		$comment = "";
	} else {
		$comment = test_input($_POST["comment"]);
	}
	
	// Test Year
	if (empty($_POST["year"])) {
		$yearErr = "Year is required";
		$errors++;
	}
	else {
		$year = test_input($_POST["year"]);
	}
	

	//Need to add a test for email
	/*
	if (empty ($_POST["email"])){
		$emailErr = "Email is required"
	}
	
	$email = test_input($_POST["email"]);
	else if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
  		$emailErr = "Invalid email format";
  		$errors++;
	}*/
	
	// Thank you note
	if ($errors === 0){
		$thankyou = "Thank you for your submission!";
	}
	
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>



<h2 style="text-align:center;color:white;">Syllabus Upload</h2>
<p><span class="error">* required field.</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>"> 
	
	<fieldset>
		<br>
		<legend class="legends">Personal Information</legend>
		
	First Name: <input class="inputs" type="text" name="firstName">
	<span class="error">* <?php echo $firstNameErr;?></span>
	<br><br>
	Last Name:  <input class="inputs" type="text" name="lastName">
	<span class="error">* <?php echo $lastNameErr;?></span>
	<br><br>
	Email:  <input class="inputs" type="email" name="email">
	<span class="error">* <?php echo $emailErr;?></span>
	<br><br>
	</fieldset>	
	<br/><br/>
	
	
	<fieldset>
		<legend class="legends">Class Information</legend><br>
		Department: <input class="inputs" type="text" name="dept" placeholder="Ex: MAT">
		<span class="error">* <?php echo $deptErr;?></span>
		<br><br>
		Class Number: <input class="inputs" type="number" name="classnum" placeholder="Ex: 110">
		<span class="error">* <?php echo $classnumErr;?></span>
		<br><br>
		Year: <input class="inputs" type="number" name="year" value=<?php echo date("Y");?>>
		<span class="error">* <?php echo $yearErr;?></span>
		<br/><br/>
		Select Semester: <input type="radio" name="semester" value="fall" checked> Fall
			             <input type="radio" name="semester" value="spring"> Spring
	</fieldset>	
	<br/><br/>
	
	<fieldset>
		<legend class="legends">Privacy Settings</legend>
		Share this syllabus width<br/>
		<input type="radio" name="privacy" value="all" checked>Anyone<br/>
		<input type="radio" name="privacy" value="davidson"> Just Davidson Students<br/>
		<input type="radio" name="privacy" value="admin"> Only Select Administrators<br/>
		<br/>
		<input type="checkbox" name="visitable" checked> Prospective students may visit your class.
	</fieldset>
	
	<br/><br/>
	Further Comments on this syllabus: 
	<br><textarea name="comment" rows="5" cols="61" placeholder="Optional"></textarea>
	<br/><br/>	
	<input type="submit" name="submit" value="Submit">  
</form>
<br/><br/>
<h2><?php echo $thankyou;?><h2>

</body>
</html>