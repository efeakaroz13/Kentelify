var alldatas = []
function init(){
    $.getJSON("/songlister",function(data){

        for (let i = 0; i < data.out.length; i++) {
            var element = data.out[i]
            alldatas.push(data.out[i])
        }
    })

}

function searchit(playlistid){

    document.getElementById("results").innerHTML = ""
    searchval = document.getElementById("search").value;
    if(searchval == ""){
        document.getElementById("results").innerHTML = ""
    }else{
    results = []
     for (let a=0 ; a<alldatas.length; a++){
            var searchforloop = alldatas[a]
            if(alldatas[a]["songname"].toLowerCase().split(searchval.toLowerCase())[1] != undefined){
                results.push(alldatas[a]["songname"])
                document.getElementById("results").innerHTML =document.getElementById("results").innerHTML +"<li class='list-group-item'>"+alldatas[a]["songname"]+"<button onclick="+'"'+"window.location.assign('/add_song/"+playlistid+"?file="+alldatas[a]["filename"]+"&music="+alldatas[a]["songname"]+"')"+'"'+" style='color:#9400de;background:none;margin-left:95%;margin-bottom:20px;border:0px'><i style='background' class='fa-solid fa-plus' ></i></button></li>"

            }
    }
    console.log(results)
    }
}
init()