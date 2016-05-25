var options = {
  valueNames: [ 'name', 'number', 'professor' ]
};

var userList = new List('users', options);

$(document).ready(function(){
  $("#hideme").click(function(){
    $(".novisit").toggle();
  });
  
  $("#prof").click(function(){
    $("#prof_list").toggle();
    $("#down_arrow_prof").toggle();
    $("#side_arrow_prof").toggle();
  });
  
  $("#dept").click(function(){
    $("#dept_list").toggle();
    $("#down_arrow_dept").toggle();
    $("#side_arrow_dept").toggle();
  });
  
  $("#class_size").click(function(){
    $("#class_size_list").toggle();
    $("#down_arrow_class_size").toggle();
    $("#side_arrow_class_size").toggle();
  }); 
});
