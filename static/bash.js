function blinker(){
    blinkers = document.getElementsByClassName("blinker")
    for (let blink = 0; blink < blinkers.length; blink++) {
        const element = blinkers[blink];
        displaycheck = element.style.display;
        if (displaycheck == "none") {
            blinkers[blink].style.display="";
            
        }
        else{
            blinkers[blink].style.display="none";
        }
        
    }
}
setInterval(blinker,400)
oldcommands = []
letterlist = []
programcode = false
document.addEventListener('keydown', (e) => {

    console.log(e.code)
    letter = e.code.split("Key")[1];
    
    digit = e.code.split("Digit")[1];

    
    if(letter == undefined){
        if (e.code == "Period" || e.code == "Slash") {
            document.getElementById("query").innerHTML =document.getElementById("query").innerHTML+"."
        }
        if(e.code == "Equal"){
            if(letterlist[0] == "A2"){
                letterlist.length = 0;
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"_"
            }
            else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"-"
            }
        }

        if (e.code == "Tab") {
            queryrn = document.getElementById("query").innerHTML;
            if(queryrn.split("python3 ") [1] != undefined){
                if (queryrn.split("mu") [1] != undefined) {
                    document.getElementById("query").innerHTML = "python3 music_download_script.py"
                }
            }
        }
        if(e.code == "Minus"){
            document.getElementById("query").innerHTML =document.getElementById("query").innerHTML+"-"
        }
        if(e.code == "ShiftRight"){
            letterlist.length = 0;

            letterlist.push("A2")
        }
        if (e.code == "ShiftLeft"){
            letterlist.length = 0
            letterlist.push("A1")
        }
        if(e.code == "Space"){
            if(letterlist[0] == "A1"){
                letterlist.length = 0;
                navigator.clipboard.readText().then((clipText) => (document.getElementById("query").innerHTML = clipText));
            }
            else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+" "
            }
        }
        if (e.code == "Backspace") {
            const query = document.getElementById("query").innerHTML


            const queryarray = query.split('')

            queryarray.pop()


            const newquery = queryarray.join('')
            document.getElementById("query").innerHTML = newquery
        }
        counter = 1
        if(e.code == "ArrowUp"){
            document.getElementById("query").innerHTML = oldcommands[oldcommands.length-counter]
            counter -=1

        }
        if(e.code == "ArrowDown"){
            if (counter <1) {
                counter +=1
                document.getElementById("query").innerHTML = oldcommands[oldcommands.length-counter-1]
            }
            if (counter == 1) {
                document.getElementById("query").innerHTML = ""
            }
            
            
            
        }
        if (e.code =="Enter") {
            if (programcode == true) {
                
                input = document.getElementById("query").innerHTML;
                document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p><a style='color:white'>? | Enter a Spotify playlist URL</a> <a style='color:rgb(52, 52, 254)'>$</a> "+input+"</p>"
                document.getElementById("query").innerHTML = ""
                if (input.trim() == "q" || input.trim() == "exit"||input.trim() == "quit") {
                    document.getElementById("cmd").innerHTML="Kentelify:~ admin";
                    programcode = false
                }
                if (input.trim() == "clear" || input.trim() == "cls" ) {
                    document.getElementById("logs").innerHTML = ""
                    document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p><img src='/static/mp3fy.png' height='100'></p>"
                    document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p><a style='color:cyan'>Author</a>:   Efe Akaröz </p>"
                    document.getElementById("cmd").innerHTML="<a style='color:white'>? | Enter a Spotify playlist URL</a>"
                   

                }
                if (input.trim().split("https://open.spotify.com")[1] != undefined) {

                    $.getJSON("/playlister_api/"+input.trim().split("https://open.spotify.com/playlist/")[1],function (data) {
                        document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p>  "+data.out.length+" SONGS COUNTED</p>"
                        for (let song = 0; song < data.out.length; song++) {
                            const element = data.out[song];
                            document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p><a style='color:blue;'>DOWNLOADING</a> | <a style='color:white'>"+element+"</a></p>"
                        }

                    })
                }
            }else{

            input = document.getElementById("query").innerHTML;
            document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p>Kentelify:~ admin <a style='color:rgb(52, 52, 254)'>$</a> "+input+"</p>"
            document.getElementById("query").innerHTML = ""
            oldcommands.push(input.trim())
            if(input.trim() == "clear" || input.trim() == "cls" ){
                document.getElementById("logs").innerHTML = ""
            }
            else if(input.trim().split("alert(")[1] !=undefined){
                alert(input.trim().split("alert(")[1].replace(")",""))
            }else if(input.trim().split("--help")[1] !=undefined){
                document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p>Here is list of commands:<br>clear<br>alert(your_text)<br> --about</p>"
            }
            else if(input.trim().split("--about")[1] !=undefined){
                document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p>Kentelify bash emulator(JS) <br>Author:Efe Akaröz 4th Agust 2022</p>"
            }
            else if(input.trim()=="ls" ||input.trim()=="dir"){
                document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p>music_download_script.py</p>"
            }
            else if(input.trim()==""){
                null
            }
            else if(input.trim().split("python3 ")[1] !=undefined){
                if (input.trim().split("python3 ")[1] == "music_download_script.py") {
                    programcode = true
                    document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p><img src='/static/mp3fy.png' height='100'></p>"
                    document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p><a style='color:cyan'>Author</a>:   Efe Akaröz </p>"
                    document.getElementById("cmd").innerHTML="<a style='color:white'>? | Enter a Spotify playlist URL</a>"
                   
                }
                else{
                    document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p> No file named:"+input.trim().split("python3 ")[1]+"</p>"
                }
            }
            else{
                document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p>Unknonw command '"+input+"', type --help for seeing commands</p>"
            }
            }
        }

    }

    else{
        if(letterlist[0] == "A2"){
            letterlist.length=0
            document.getElementById("query").innerHTML = document.getElementById("query").innerHTML + letter;
        }else{
            document.getElementById("query").innerHTML = document.getElementById("query").innerHTML + letter.toLowerCase()
        }
        

    }
    if (digit != undefined) {
        if (digit == "8") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"("
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"8"
            }
        }
        if (digit == "7") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"/"
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"7"
            }
        }
        if (digit == "9") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+")"
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"9"
            }
        }
        if (digit == "1") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"!"
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"1"
            }
        }
        if (digit == "2") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"'"
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"2"
            }
        }
        if (digit == "3") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"#"
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"3"
            }
        }
        if (digit == "4") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"+"
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"4"
            }
        }
        if (digit == "5") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"%"
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"5"
            }
        }
        if (digit == "6") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"6"
            }
        }
        if (digit == "0") {
            if (letterlist[0] == "A2"){
                letterlist.length = 0
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"="
            }else{
                document.getElementById("query").innerHTML = document.getElementById("query").innerHTML+"0"
            }
        }
    }

    
});