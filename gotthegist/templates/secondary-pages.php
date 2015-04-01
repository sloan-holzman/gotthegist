<!DOCTYPE html>
<html lang="en">
<head>
<title>Got the Gist: Sports</title>
<?php
    include("../templates/stylesheet_links.inc");
?>

</head>

<body>

<!--basic template taken from: "http://www.tutorialrepublic.com/twitter-bootstrap-tutorial/bootstrap-responsive-layout.php"-->
<style type="text/css">
    body{
    	padding-top: 70px;
    }
</style>
</head>
<body>
<?php
    include("../templates/nav-bar.inc");
?>
<b>






<div id="masthead" class="">
    <div class="container">
        <div class="row">
            <div class="col-md-8">
                 <h1 class="">New York Knicks
            <p class="lead">A sad team</p>
          </h1>

            </div>
            <div class="col-md-4">
                <div class="well well-lg">
                    <div class="row">
                        <div class="col-sm-6">
                            <img src="//placehold.it/160x90" class="img-responsive">
                        </div>
                        <div class="col-sm-6">  <strong class="">Important</strong>

                            <p class="">Blah blah blah blah bla!</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- /cont -->
</div>
<div class="container" id="mycontentcon">
<script>
$('body').scrollspy({ target: '#sidebar', offset:80 });

<!--I am not sure what to do with the script!!!!-->

var clicked = false;
$('#mynav li a').click(
function(){
    $('#mycontent > div > h2').css('padding-top',0);
    $($( this ).attr('href') + ' > h2').css('padding-top','50px');
    clicked = true;
    }
);  

$('body').on('activate.bs.scrollspy', function () {
  console.log('scrolling...');
  if(!clicked)$('#mycontent > div > h2').css('padding-top',0);
  clicked = false;
})
</script>

    <div class="row">
        <div class="col-md-3">
            <div class="list-group navbar" id="sidebar">
                <ul class="nav" id="mynav" data-spy="affix" data-offset-top="280">
                    <li><a href="#c1" class="list-group-item" contenteditable="false">Overview
                        </a>
                    </li>
                    <li> <a href="#c2" class="list-group-item" contenteditable="false">Team Colors
                        </a>
                    </li>
                    <li> <a href="#c3" class="list-group-item" contenteditable="false">Fan Mood
                        </a>
                    </li>
                    <li> <a href="#c4" class="list-group-item" contenteditable="false">Players
                        </a>
                    </li>
                    <li> <a href="#c5" class="list-group-item" contenteditable="false">Coach
                        </a>
                    </li>
                    <li> <a href="#c6" class="list-group-item" contenteditable="false">Style
                        </a>
                    </li>
                    <li> <a href="#c7" class="list-group-item" contenteditable="false">Schedule
                        </a>
                    </li>
                        <li> <a href="#c8" class="list-group-item" contenteditable="false">Celebrity Connections
                        </a>
                    </li>
                        <li> <a href="#c9" class="list-group-item" contenteditable="false">History
                        </a>
                    </li>
                    <li> <a href="#c10" class="list-group-item" contenteditable="false">Fun Facts
                        </a>
                    </li>
                    <li> <a href="#c11" class="list-group-item" contenteditable="false">How To Sound Smart
                        </a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="col-md-9" id="mycontent">
            <div id="c1">
                <h2 class="">Overview</h2>
                    At Bootply we attempt to build simple Bootstrap templates that utilize
                    the code Bootstap CSS without a lot of customization. Tia cor magni dolores
                    eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui
                    dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia
                    non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam
                    quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem
                    ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur?
                <hr class="col-md-12">
            </div>
            <div id="c2">
                <h2>Team Colors</h2>
                    Rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto
                    beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas
                    sit aspernatur aut odit aut fugit, sed quia cor magni dolores eos qui ratione
                    voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum
                    quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam
                    eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.
                    Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit
                    laboriosam, nisi ut
                <hr class="col-md-12">
            </div> 
            <div id="c3">   
                <h2 class="">Fan Mood</h2>
                    Rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto
                    beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas
                    sit aspernatur aut odit aut fugit, sed quia cor magni dolores eos qui ratione
                    voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum
                    quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam
                    eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.
                    Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit
                    laboriosam, nisi ut
                <hr class="col-md-12">
            </div>
            <div id="c4">
                    <h2 class="">Players</h2>
                    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
                    doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
                    veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
                    ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
                    cor magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro
                    quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
                    velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore
                    magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum
                    exercitationem ullam corporis suscipit laboriosam, nisi ut
                <hr class="col-md-12">
            </div>
            <div id="c5">
                <h2 class="">Coach</h2>
                    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
                    doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
                    veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
                    ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
                    cor magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro
                    quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
                    velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore
                    magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum
                    exercitationem ullam corporis suscipit laboriosam, nisi ut
                <hr class="col-md-12">
            </div>
            <div id="c6">
                <h2 class="">Style</h2>
                    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
                    doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
                    veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
                    ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
                    cor magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro
                    quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
                    velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore
                    magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum
                    exercitationem ullam corporis suscipit laboriosam, nisi ut
                <hr class="col-md-12">
            </div>
            <div id="c7">
                <h2 class="">Schedule</h2>
                    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
                    doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
                    veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
                    ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
                    cor magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro
                    quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
                    velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore
                    magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum
                    exercitationem ullam corporis suscipit laboriosam, nisi ut
                <hr class="col-md-12">
            </div>
            <div id="c8">
                <h2 class="">Celebrity Connections</h2>
                    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
                    doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
                    veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
                    ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
                    cor magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro
                    quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
                    velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore
                    magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum
                    exercitationem ullam corporis suscipit laboriosam, nisi ut
                <hr class="col-md-12">
            </div>
            <div id="c9">
                <h2 class="">History</h2>
                    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
                    doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
                    veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
                    ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
                    cor magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro
                    quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
                    velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore
                    magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum
                    exercitationem ullam corporis suscipit laboriosam, nisi ut
                    <br>
                    <br>
                    <a href="#">Learn More About the Team's History >></a>
                <hr class="col-md-12">
            </div>
            <div id="c10">
                <h2 class="">Fun Facts</h2>
                    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
                    doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
                    veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
                    ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
                    cor magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro
                    quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
                    velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore
                    magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum
                    exercitationem ullam corporis suscipit laboriosam, nisi ut
                <hr class="col-md-12">
            </div>
            <div id="c11">
                <h2 class="">How to Sound Smart</h2>
                    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
                    doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
                    veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim
                    ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia
                    cor magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro
                    quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci
                    velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore
                    magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum
                    exercitationem ullam corporis suscipit laboriosam, nisi ut
                <hr class="col-md-12">
            </div>
        </div>
    </div>
</div>
</body>
</html>                                		