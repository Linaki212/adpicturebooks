var i = 0;
var txt = 'Lorem ipsum typing effect!'; /* The text */
var speed = 50; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("demo").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}



// var spans = '<span>' + str.split('').join('</span><span>') + '</span>';
// $(spans).hide().appendTo('.css-typing').each(function (i) {
//     $(this).delay(100 * i).css({
//         display: 'inline',
//         opacity: 0
//     }).animate({
//         opacity: 1
//     }, 100);
// });

// $(document).ready(function(){
// 	$("h1").css("color", "red");
// });

// $( "#clickme" ).click(function() {
//   $( "#old_hands3" ).fadeOut( "slow", function() {
//     // Animation complete.
//   });
// });