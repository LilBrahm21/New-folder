let images = ["https://dirtwheelsmag.com/wp-content/uploads/2018/08/LITTLE_SAHARRA_SPRD-e1539123172352.jpg", "https://www.blm.gov/sites/default/files/styles/hero_lg_content/public/hero_backgrounds/little%20sahara.jpg?h=c74750f6&itok=iUS_Qup7","https://archive.sltrib.com/images/2015/0102/littlesahara_110314~0.jpg"]
let counter = 0

function change(){
    if (counter < images.length){
        document.getElementById("image").src = images[counter]
        counter += 1
    }else{
        counter = 0
        document.getElementById("image").src = images[counter]
    }

}

function myFunction() {
    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }