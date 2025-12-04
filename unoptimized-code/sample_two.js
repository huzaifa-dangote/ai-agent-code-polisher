function loadProd(){
    fetch("https://example.com/api/products")
    .then(res => {
        return res.json()
    }).then(d => {
        let arr = []
        for(let i=0;i<d.length;i++){
            if(d[i].price < 50){
                arr.push(d[i])
            }
        }

        let el = document.getElementById("list");
        el.innerHTML = "";
        for(let j=0; j<arr.length; j++){
            el.innerHTML += "<div class='p'>" + arr[j].name + " - " + arr[j].price + "</div>"
        }
    })
    .catch(e => {
        console.log("err", e)
    })
}

loadProd()
