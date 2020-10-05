#!"C:\xampp\perl\bin\perl.exe"



use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

use Fcntl qw(:flock :seek);

my $i;
my $j;
my $temp;
@board=( [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0]) ;

for($i=1; $i<10; $i++){
   for($j=1; $j<10; $j++){
         $temp=param($i.$j);
         $board[$i-1][$j-1]=$temp;
   }
}
sub backtrack{
	
#      for($i=0;$i<9;$i++){
# 	for($j=0;$j<9;$j++){
# 	    print "$board[$i][$j] ";
# 	}
# 	    print "\n";
#     }
	
#     print "\n\n";
   my $e=1;
   my $row=-1;
   my $col=-1;
   my $i=0;
   my $j=0;
   my $c=0;
    B:{   for($i=0;$i<9;$i++){
        	    for($j=0;$j<9;$j++){
        	        if($board[$i][$j]==0){
        	            $row=$i;
        	            $col=$j;
        	            $e=0;
        	            last B;
        	        }
        	    }
            }
    }
    
    if($e){
        return 1;
    }
    
    	for($c=1;$c<=9;$c++){
		    if(isValid($row,$col,$c)==1){
			    $board[$i][$j]=$c;
			    if(backtrack()){
			        return 1;
			    }
			    else{
			         $board[$i][$j]=0;
			    }
		    }
		}
	return 0;

}


sub isValidConfig{
    my $i;
    my $j;
    for($i=0; $i<9; $i++){
        for($j=0; $j<9; $j++){
            if($board[$i][$j]!=0 && isValid($i,$j,$board[$i][$j])==0){

                return 0;
            }
        }
            
    }
    return 1;
}

sub isValid{
  my $i=$_[0];
  my $j=$_[1];
  my $c=$_[2];
  my $k=0;
  if($c==0){return 1;}
  for($k=0;$k<9;$k++){
      	if($board[$k][$j] != 0 && $i!=$k && $board[$k][$j]==$c)
	  {return 0; }
  }
  for($k=0;$k<9;$k++){
      	if($board[$i][$k] != 0 && $j!=$k && $board[$i][$k]==$c)
	  {return 0; }
  }
  
  
	 $bi=$i - $i%3;
	
	 $bj=$j - $j%3;
#   print "\n $bi $bj \n";
    for($k=0;$k<3;$k++){
         for($l=0;$l<3;$l++){
        	if($bi+$k!=$i && $bj+$l!=$j && $board[$bi+$k][$bj+$l]!=0 && $board[$bi+$k][$bj+$l]==$c)
            { return 0;}
         }
    }
    return 1;
}

my $result1=isValidConfig();
my $msg="For given sudoku formation solution is not possible.";
my $result;
if($result1==1){
    $result=backtrack();
}else{
    $result=0;
	$msg="Given sudoku is invalid, read the sudoku rules again then check the unsolved sudoku for violation of rule";
}
if($result==1){


   print header;
print start_html("Result");
 $temp=102002;
print <<END;
<head>
	<link href="https://fonts.googleapis.com/css2?family=Loved+by+the+King&family=Piedra&display=swap" rel="stylesheet">
<style>

.a1{
	height:30px;
	width:30px;
	text-align: center;
	padding: 2px;
	margin: 2px;
	border-radius: 18%;
	color: #132743;
	background-color: #f8efd4;
	font-family:  cursive;
}
.a1:hover{
	cursor: text;
	
}
.a2 tr td input{ 
	background-color: #edc988;
}
body{
  
	background-color: #132743;
}

h1,h2{
	color:  #f8efd4;
}
h1{
	font-size: 25px;
	
}
 .h12{
	font-family: 'Piedra', cursive;
	font-size: 50px;
	padding: 0;
   margin-top:0px;
	margin-bottom: -10px;
 }
.outer{
  
	background-color: #d7385e;
	
	border-radius: 5%;
	padding : 5px;
}


.container{
	display: flex;
	justify-content:space-evenly;

}
.Note{
	display: flex;
	flex-direction: column;
	justify-content: center;
	vertical-align: center;
	width: 31vw;
	text-align: justify;
	font-family: cursive;
	
}
.Note h1{
	font-size: 25px;
}
.note1{
	color: #d7385e;
	font-weight: 600;
	font-size: 25px;

}
.note2{
	color: #f8efd4;
	letter-spacing: .5px;
}

.button{
	margin: 10px;
	width: 80px;
	height: 30px;
	border-radius: 10px;
	margin-left: 410px;
	color: #132743;
	font-weight: 400;
	font-size: 16px;
	background-color:#f8efd4;
	font-family:'Piedra', cursive;
   text-decoration:none;
}

.button:hover{
	background-color: #132743;
	color:#f8efd4;
	cursor: pointer;
}

.copy{
	color :#f8efd4;
	font-size: 14px;
	
	font-family: 'Haettenschweiler', 'Arial Narrow Bold', sans-serif
}
</style>
</head>
<body>
<h1 align="center" class="h12">SUDOKU SOLVER</h1>
<hr><hr>
<br>
<div class="container">
	<div class="Note"><h1> !!! Congratulations Solution Found !!!</h1> <span class="note2"> Right side is the solved sudoku is shown.<br>
	press RESET to do it again ...... </span></div>
<div>
<form action="http://localhost/perl/solver.cgi" method="POST" style="margin-left:50px;">

<table class="outer" align="center">
	<tr>
<td>
<table class ="inner">
	<tr>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][0]"  name="11" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][1]"  name="12" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][2]" name="13" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][0]" name="21" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][1]" name="22" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][2]" name="23" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][0]"  name="31" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][1]" name="32" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][2]" name="33" disabled /></td>
	</tr>
</table>
</td>

<td>
	<table class ="inner a2">
		<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][3]" name="14" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][4]" name="15" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][5]" name="16" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][3]" name="24" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][4]" name="25" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][5]" name="26" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][3]" name="34" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][4]" name="35" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][5]" name="36" disabled /></td>
		</tr>
	</table>
	</td>

	<td>
		<table class ="inner">
			<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][6]" name="17" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][7]" name="18" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][8]" name="19" disabled /></td>
			</tr>
			<tr>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][6]" name="27" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][7]" name="28" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][8]" name="29" disabled /></td>
			</tr>
			<tr>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][6]" name="37" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][7]" name="38" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][8]" name="39" disabled /></td>
			</tr>
		</table>
		</td>
</tr>

<tr>
	<td>
<table class ="inner a2">
	<tr>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][0]"  name="41" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][1]"  name="42" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"  value="$board[3][2]" name="43" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"  value="$board[4][0]" name="51" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][1]"  name="52" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][2]"  name="53" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][0]"  name="61" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][1]"  name="62" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][2]" name="63" disabled /></td>
	</tr>
</table>
</td>

<td>
	<table class ="inner">
		<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"  value="$board[3][3]" name="44" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"  value="$board[3][4]" name="45" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][5]"  name="46" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][3]" name="54" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][4]" name="55" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][5]" name="56" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][3]" name="64" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][4]" name="65" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][5]" name="66" disabled /></td>
		</tr>
	</table>
</td>

<td>
		<table class ="inner a2">
			<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][6]" name="47" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][7]" name="48" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][8]" name="49" disabled /></td>
			</tr>
			<tr>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][6]" name="57" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][7]" name="58" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][8]" name="59" disabled /></td>
			</tr>
			<tr>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][6]" name="67" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][7]" name="68" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][8]"  name="69" disabled /></td>
			</tr>
		</table>
		</td>
</tr>

<tr>
	<td>
<table class ="inner">
	<tr>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][0]" name="71" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][1]" name="72" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][2]" name="73" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][0]" name="81" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][1]" name="82" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"value="$board[7][2]"  name="83" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][0]" name="91" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][1]" name="92" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][2]" name="93" disabled /></td>
	</tr>
</table>
</td>

<td>
	<table class ="inner a2">
		<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][3]" name="74" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][4]" name="75" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][5]" name="76" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][3]" name="84" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][4]" name="85" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][5]" name="86" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][3]" name="94" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][4]"  name="95" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][5]"  name="96" disabled /></td>
		</tr>
	</table>
	</td>

	<td>
		<table class ="inner">
			<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][6]" name="77" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][7]" name="78" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][8]" name="79" disabled /></td>
			</tr>
			<tr>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][6]" name="87" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][7]" name="88" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"value="$board[7][8]"  name="89" disabled /></td>
			</tr>
			<tr>
				<td> <input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][6]" name="97" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][7]" name="98" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][8]" name="99" disabled /></td>
			</tr>
		</table>
		</td>
</tr>
</table>


</form>
<form action="sudokuSolver.html">
<input type="submit"  value="RESET" class="button">
</form>
</div>
</div>
<br>
<div class="copy" align="center">\@copyRight 17BIT008 & 17BIT013</div>
</body>
END

print end_html;

}
else{
 print header;
print start_html("Result");

print <<END;
<head>
	<link href="https://fonts.googleapis.com/css2?family=Loved+by+the+King&family=Piedra&display=swap" rel="stylesheet">
<style>

.a1{
	height:30px;
	width:30px;
	text-align: center;
	padding: 2px;
	margin: 2px;
	border-radius: 18%;
	color: #132743;
	background-color: #f8efd4;
	font-family:  cursive;
}
.a1:hover{
	cursor: text;
	
}
.a2 tr td input{ 
	background-color: #edc988;
}
body{
  
	background-color: #132743;
}

h1,h2{
	color:  #f8efd4;
}
h1{
	font-size: 25px;
	
}
 .h12{
	font-family: 'Piedra', cursive;
	font-size: 50px;
	padding: 0;
   margin-top:0px;
	margin-bottom: -10px;
 }
.outer{
  
	background-color: #d7385e;
	
	border-radius: 5%;
	padding : 5px;
}


.container{
	display: flex;
	justify-content:space-evenly;

}
.Note{
	display: flex;
	flex-direction: column;
	justify-content: center;
	vertical-align: center;
	width: 31vw;
	text-align: justify;
	font-family: cursive;
	
}
.Note h1{
	font-size: 25px;
}
.note1{
	color: #d7385e;
	font-weight: 600;
	font-size: 25px;

}
.note2{
	color: #f8efd4;
	letter-spacing: .5px;
}

.button{
	margin: 10px;
	width: 80px;
	height: 30px;
	border-radius: 10px;
	margin-left: 410px;
	color: #132743;
	font-weight: 400;
	font-size: 16px;
	background-color:#f8efd4;
	font-family:'Piedra', cursive;
   text-decoration:none;
}

.button:hover{
	background-color: #132743;
	color:#f8efd4;
	cursor: pointer;
}

.copy{
	color :#f8efd4;
	font-size: 14px;
	
	font-family: 'Haettenschweiler', 'Arial Narrow Bold', sans-serif
}
</style>
</head>
<body>
<h1 align="center" class="h12">SUDOKU SOLVER</h1>
<hr><hr>
<br>
<div class="container">
	<div class="Note"><h1 class="note1"> !!! Error Solution doesn't exist !!!</h1> <span class="note2"> $msg<br>
	Check the given sudoku for any error and press RESET to do it again ...... </span></div>
<div>
<form action="http://localhost/perl/solver.cgi" method="POST" style="margin-left:50px;">

<table class="outer" align="center">
	<tr>
<td>
<table class ="inner">
	<tr>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][0]"  name="11" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][1]"  name="12" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][2]" name="13" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][0]" name="21" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][1]" name="22" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][2]" name="23" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][0]"  name="31" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][1]" name="32" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][2]" name="33" disabled /></td>
	</tr>
</table>
</td>

<td>
	<table class ="inner a2">
		<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][3]" name="14" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][4]" name="15" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][5]" name="16" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][3]" name="24" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][4]" name="25" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][5]" name="26" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][3]" name="34" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][4]" name="35" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][5]" name="36" disabled /></td>
		</tr>
	</table>
	</td>

	<td>
		<table class ="inner">
			<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][6]" name="17" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][7]" name="18" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[0][8]" name="19" disabled /></td>
			</tr>
			<tr>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][6]" name="27" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][7]" name="28" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[1][8]" name="29" disabled /></td>
			</tr>
			<tr>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][6]" name="37" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][7]" name="38" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[2][8]" name="39" disabled /></td>
			</tr>
		</table>
		</td>
</tr>

<tr>
	<td>
<table class ="inner a2">
	<tr>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][0]"  name="41" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][1]"  name="42" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"  value="$board[3][2]" name="43" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"  value="$board[4][0]" name="51" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][1]"  name="52" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][2]"  name="53" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][0]"  name="61" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][1]"  name="62" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][2]" name="63" disabled /></td>
	</tr>
</table>
</td>

<td>
	<table class ="inner">
		<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"  value="$board[3][3]" name="44" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"  value="$board[3][4]" name="45" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][5]"  name="46" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][3]" name="54" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][4]" name="55" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][5]" name="56" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][3]" name="64" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][4]" name="65" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][5]" name="66" disabled /></td>
		</tr>
	</table>
</td>

<td>
		<table class ="inner a2">
			<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][6]" name="47" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][7]" name="48" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[3][8]" name="49" disabled /></td>
			</tr>
			<tr>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][6]" name="57" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][7]" name="58" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[4][8]" name="59" disabled /></td>
			</tr>
			<tr>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][6]" name="67" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][7]" name="68" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[5][8]"  name="69" disabled /></td>
			</tr>
		</table>
		</td>
</tr>

<tr>
	<td>
<table class ="inner">
	<tr>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][0]" name="71" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][1]" name="72" disabled /></td>
	<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][2]" name="73" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][0]" name="81" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][1]" name="82" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"value="$board[7][2]"  name="83" disabled /></td>
	</tr>
	<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][0]" name="91" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][1]" name="92" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][2]" name="93" disabled /></td>
	</tr>
</table>
</td>

<td>
	<table class ="inner a2">
		<tr>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][3]" name="74" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][4]" name="75" disabled /></td>
		<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][5]" name="76" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][3]" name="84" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][4]" name="85" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][5]" name="86" disabled /></td>
		</tr>
		<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][3]" name="94" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][4]"  name="95" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][5]"  name="96" disabled /></td>
		</tr>
	</table>
	</td>

	<td>
		<table class ="inner">
			<tr>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][6]" name="77" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][7]" name="78" disabled /></td>
			<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[6][8]" name="79" disabled /></td>
			</tr>
			<tr>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][6]" name="87" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[7][7]" name="88" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1"value="$board[7][8]"  name="89" disabled /></td>
			</tr>
			<tr>
				<td> <input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][6]" name="97" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][7]" name="98" disabled /></td>
				<td><input type="text" pattern="\\d" title="single digit allow between 0-9" class="a1" value="$board[8][8]" name="99" disabled /></td>
			</tr>
		</table>
		</td>
</tr>
</table>


</form>
<form action="sudokuSolver.html">
<input type="submit"  value="RESET" class="button">
</form>
</div>
</div>
<br>
<div class="copy" align="center">\@copyRight 17BIT008 & 17BIT013</div>
</body>
END

print end_html;
}
