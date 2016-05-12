var $container=$('#masonry-grid');
$container.masonry({
  itemSelector:'.grid-item',
  percentPosition:true,
  columnWidth:'.grid-sizer',
  animate:true
});
$container.on('click','.grid-item',function(){
    var $target = $(this);
    var w = $target.width();
    $target.toggleClass('.grid-item--width2');
    if(w>500){
      w="300px";
    }else{
      w="600px";
    }
    $(this).children().animate({width:w});
    $(this).animate({width:w},doMasonry);
  });

  $container.imagesLoaded().progress(function(){
  $container.masonry();
});


getAllImgs();
function getAllImgs(){
  $.get("{%url'get-all-images'%}",function(data){
    for(vari=0;i<data.imageDict.length;i++){
      var domElement='<div class="grid-item"><img width="'+300+'"src="'+data.imageDict[i]+'"/></div>';
      var $wrap=$(domElement);
      $container.append($wrap).masonry('appended',$wrap).masonry();
    }
  });
}

function doMasonry(){
  $container.masonry();
}