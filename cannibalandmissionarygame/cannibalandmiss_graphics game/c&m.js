 var bank=function(side,h,g)
   {this.s=side;
    this.h=h;
    this.g=g;
  }
  var b=new Array(2);
  b[0]=new bank(0,3,3);
  b[1]=new bank(0,0,0);

var boat=function(side,h,g)
{
  this.s=side;
  this.h=h;
  this.g=g;
}
var bo=new boat(0,0,0);

function start(){
 
 $(".center").click(function(){
     $(".center").fadeOut(600,function(){
         $(".formal").fadeIn(1000);
        clean();
        write();
          });
   });

}
function write(){

for(var i = 0 ;i< b[0].h;  i++)
  {
    $(".humanl").prepend("miss<br/>");
}
for(var i = 0 ;i< b[1].h;  i++)
  {
    $(".humanr").prepend("miss<br/>");
}
for(var i = 0 ;i< b[0].g;  i++)
  {
    $(".ghostl").prepend("cann<br/>");
}
for(var i = 0 ;i< b[1].g;  i++)
  {
    $(".ghostr").prepend("cann<br/>");
  }
for(var i = 0;i<bo.h;i++)
{
  $(".humanb").prepend("miss<br/>");
}
for(var i = 0;i<bo.g;i++)
{
  $(".ghostb").prepend("cann<br/>");
 }

if(status())
   $(".boati").html("<b>Move!!</b>").css("cursor","pointer");
  else $(".boati").html("Boat").css("cursor","default");

}

function clean(){
  $(".humanl").empty();
  $(".humanr").empty();
  $(".humanb").empty();
  $(".ghostl").empty();
  $(".ghostr").empty();
  $(".ghostb").empty();
  
}

function status(){
if(bo.h+bo.g==2)
  return 2;
else if(bo.h+bo.g==1)
  return 1
;else return 0;
}
//left//
function clickhl(){
  $(".humanl").click(function(){
    if(bo.s==0&&status()!=2&&b[0].h)
      { 
    b[0].h--;
    bo.h++;
    clean();
    write();
    }
  });
}
function clickgl(){
  $(".ghostl").click(function(){
    if(bo.s==0&&status()!=2&&b[0].g)
      { 
    b[0].g--;
    bo.g++;
    clean();
    write();
    }
  });
}
//right//

function clickhr(){
  $(".humanr").click(function(){
    if(bo.s==1&&status()!=2&&b[1].h)
      { 
    b[1].h--;
    bo.h++;
    clean();
    write();
    }
  });
}
function clickgr(){
  $(".ghostr").click(function(){
    if(bo.s==1&&status()!=2&&b[1].g)
      { 
    b[1].g--;
    bo.g++;
    clean();
    write();

    }
  });
}
//boat//
function clickhb(callback){
  $(".humanb").click(function(){
    if(bo.h){
    b[bo.s].h++;
    bo.h--;
    clean();
    write();
    callback();
    }
  });
}
function clickgb(callback){
  $(".ghostb").click(function(){
   if(bo.g){
    b[bo.s].g++;
    bo.g--;
    clean();
    write();
callback();
    }
  });
}





function iswin()
{
  if (b[1].h==3&&b[1].g==3)
    {$(".formal").fadeTo(1500,0.4,function(){
  $(".gameover").fadeIn(1000,function(){
   $ (".gameover").html("<p style='font-size:100px'>You win!<br/><br/><br/>Click to Try again!</p><p></p>");
  })

})
 
}

}






function isover()
{
  $(".formal").fadeTo(1500,0.4,function(){
  $(".gameover").fadeIn(1000,function(){
   $ (".gameover").html("<p style='font-size:100px'><br/>Click to Try again!</p>");
  })

})
 
}




function clickb(){
  $(".boati").click(function(){
    if(status()){
      
     if(bo.s==0){
       $(".boati").animate({left:'+=30%'},
        function(){ 
            if(b[bo.s].h<b[bo.s].g&&b[bo.s].h)
                    {$(".humanl").css("color","red"); isover(); }
            bo.s=1;
            if(b[bo.s].h+bo.h<b[bo.s].g+bo.g&&b[bo.s].h+bo.h)
            {$(".humanl").css("color","red");
            isover(); }
      });
      $(".humanb").animate({left:'+=30%'});
      $(".ghostb").animate({left:'+=30%'});
     
     
    }
      else{
      $(".boati").animate({left:'-=30%'},
       function(){ 
        if(b[bo.s].h<b[bo.s].g&&b[bo.s].h)
                    {$(".humanr").css("color","red");
                  isover();}
           bo.s=0;
          if(b[bo.s].h+bo.h<b[bo.s].g+bo.g&&b[bo.s].h+bo.h)
          {$(".humanr").css("color","red"); isover();}
      });
      $(".humanb").animate({left:'-=30%'});
      $(".ghostb").animate({left:'-=30%'});
     
      }
    }
  });
}

function Tryagain(){
 $(".gameover").click(function(){
    location.reload();
  });
}

$(document).ready(function(){

 start();

 clickhl();
 clickgl();
 clickhr();
 clickgr();
 clickhb(iswin);
 clickgb(iswin);
 clickb();
 Tryagain();

});
