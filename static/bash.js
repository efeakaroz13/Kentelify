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

letterlist = []
document.addEventListener('keydown', (e) => {

    console.log(e.code)
    letter = e.code.split("Key")[1];
    
    digit = e.code.split("Digit")[1];

    
    if(letter == undefined){
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
        if (e.code =="Enter") {
            input = document.getElementById("query").innerHTML;
            document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p>Kentelify:~ admin <a style='color:rgb(52, 52, 254)'>$</a> "+input+"</p>"
            document.getElementById("query").innerHTML = ""
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
        
            else{
                document.getElementById("logs").innerHTML = document.getElementById("logs").innerHTML+"<p>Unknonw command '"+input+"', type --help for seeing commands</p>"
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