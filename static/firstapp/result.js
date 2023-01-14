
var i =0;
$( "form" ).hide( 0 );

$( '#showbutton' ).click(function() {
if(i==0){
  $( "form" ).show( "slow" );
  i=1;}
  else if(i==1){
  $( "form" ).hide( "slow" );
  i=0;}
});


//$('#abcd').css('color','blue')
//$('h2').css('color','blue')
$( "#finalresult" ).hide( 0 );
$( "#finalresult" ).show( "slow" );