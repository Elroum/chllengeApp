function near_shops() {
if (document.getElementById("near_shops").style.display== "none"){

  document.getElementById("near_shops").style.display="block";
  document.getElementById("pref_shops").style.display="none";
}


}

function prefred_shops() {
if (document.getElementById("pref_shops").style.display== "none"){

  document.getElementById("pref_shops").style.display="block";
  document.getElementById("near_shops").style.display="none";
}

}