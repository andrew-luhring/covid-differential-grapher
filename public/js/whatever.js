

function createMasterObj(data){
  console.log(data)


    // mo[fips.state][key] = fips
  
  //
  // for(let [statename, state] of Object.entries(mo)){
  //   for(let [fipsName, fips] of Object.entries(state)){
  //
  //
  //   }
  // }
}


(function makeRequest(){
  let httpRequest = new XMLHttpRequest();
  let jsondata;
  httpRequest.onreadystatechange = function(data){
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
      if (httpRequest.status === 200) {
        jsondata = JSON.parse(httpRequest.responseText)

        createMasterObj(jsondata)
      }
    }
  }
  httpRequest.open('GET', './js/data.json');
  httpRequest.send();
}())

var ctx = document.getElementById('myChart').getContext('2d');
