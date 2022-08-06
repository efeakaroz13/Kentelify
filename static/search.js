var alldatas = []
function init(){
    $.getJSON("/songlister",function(data){

        for (let i = 0; i < data.out.length; i++) {
            var element = data.out[i]
            alldatas.push(data.out[i]["songname"])
        }
    })

}

function searchit(){

    document.getElementById("results").innerHTML = ""
    searchval = document.getElementById("search").value;
    if(searchval == ""){
        document.getElementById("results").innerHTML = ""
    }else{
    results = []
     for (let a=0 ; a<alldatas.length; a++){
            var searchforloop = alldatas[a]
            if(alldatas[a].toLowerCase().split(searchval.toLowerCase())[1] != undefined){
                results.push(alldatas[a])
                document.getElementById("results").innerHTML =document.getElementById("results").innerHTML +"<li class='list-group-item'>"+alldatas[a]+"</li>"

            }
    }
    console.log(results)
    }
}
init()