//document.body.style.backgroundColor = 'green';

if (sessionStorage.getItem("bg_color_main") == null){
	whitebg();
}else{
	document.body.style.backgroundColor = sessionStorage.getItem("bg_color_main");
}

//Background functions

function whitebg(){
    document.body.style.backgroundColor = 'white';
    sessionStorage.setItem("bg_color_main", 'white');
}

function coralbg(){
    document.body.style.backgroundColor = 'lightcoral';
    sessionStorage.setItem("bg_color_main", 'lightcoral');
}

function cyanbg(){
    document.body.style.backgroundColor = 'lightcyan';
    sessionStorage.setItem("bg_color_main", 'lightcyan');
}

function yellowbg(){
    document.body.style.backgroundColor = 'lightgoldenrodyellow';
    sessionStorage.setItem("bg_color_main", 'lightgoldenrodyellow');
}

function pinkbg(){
    document.body.style.backgroundColor = 'lightpink';
    sessionStorage.setItem("bg_color_main", 'lightpink');
}

//font size functions

//document.getElementById("about").style.fontSize = "40px";
function px25(){
    document.getElementById("main").style.fontSize = "25px";
    sessionStorage.setItem("bg_font_size", "25px");
}

function px30(){
    document.getElementById("main").style.fontSize = "30px";
    sessionStorage.setItem("bg_font_size", "30px");
}

function px35(){
    document.getElementById("main").style.fontSize = "35px";
    sessionStorage.setItem("bg_font_size", "35px");
}

function add_func(){   
    input_news = document.getElementById("news_input").value;
    if (input_news==""){
        alert("Please enter valid update.")
    }else{
        cur_news_index = localStorage.getItem("news_count");
        if (cur_news_index == null){
            localStorage.setItem("news_count", 0);
        }
        cur_news_index = parseInt(localStorage.getItem("news_count"));
	    localStorage.setItem(cur_news_index+"date", Date());
        localStorage.setItem(cur_news_index, input_news);
        localStorage.setItem("news_count", cur_news_index+1)

        //alert("Update "+ (cur_news_index+1) + " '" + input_news+"' Added.");

        var row = document.createElement('tr');
        var data = document.createElement('td');
        data.innerHTML = localStorage.getItem(cur_news_index+'date')+":" + localStorage.getItem(cur_news_index);
        row.appendChild(data);
        table_obj.appendChild(row);
    }
    window.location.href = "index.html#news";
}

function del_func(){
    localStorage.clear();
    // window.location='index.html#news';
    document.location.reload();
    window.location.href = "index.html#news";
}
