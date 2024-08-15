// validation harusnya seperti ini
function formSubmit() {
    console.log("TEST")
    let angka = document.getElementById("angka")
    angka = Number(angka)
    if (angka){
        return true
    }
    return false
}

function myFunction(){
    let form = document.getElementById("form")
    console.log(form)
    console.log("CLICKED")
}