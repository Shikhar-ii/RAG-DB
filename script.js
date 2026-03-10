const API = "http://127.0.0.1:8000"


async function upload(){

let file=document.getElementById("file").files[0]

let form=new FormData()

form.append("file",file)

await fetch(API+"/upload",{

method:"POST",

body:form

})

alert("uploaded")

}


async function ask(){

let q=document.getElementById("query").value

let form=new FormData()

form.append("query",q)

let res=await fetch(API+"/ask",{

method:"POST",

body:form

})

let data=await res.json()

document.getElementById("answer").innerText=data.answer

}
