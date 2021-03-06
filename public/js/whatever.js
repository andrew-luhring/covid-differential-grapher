function findHighest(data){
  let highest = 0;

  for(let [statename, state] of Object.entries(data)){
    let len = state.death_differentials.length;
    if(len > highest){
      highest = len;
    }
  }
  return highest;
}


function drawStuff(_jsondata){
  const jsondata = JSON.parse(JSON.stringify(_jsondata))
  let data = [];
  let highest = findHighest(jsondata.states);

  for(let [statename, state] of Object.entries(jsondata.states)){
    let dds = state.death_differentials;
    if(state.death_differentials.length < highest){
      let zeroes = new Array(highest - state.death_differentials.length);
      zeroes.fill(0)
      dds.unshift(zeroes)
      dds = dds.flat()
    }
    let color = `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, 1)`
    let obj = {label: statename, data: dds, borderColor: color, backgroundColor: 'rgb(255,255,255,0.0)', hidden: true}
    data.push(obj)
  }

  data.push({label: 'national death rates', data: jsondata.death_differentials, borderColor: 'rgb(0,0,0,1)', backgroundColor: 'rgb(255,255,255,0.0)', hidden: false})
  data.push({label: 'national deaths', data: jsondata.deaths, borderColor: 'rgb(20,20,20,1)', backgroundColor: 'rgb(255,255,255,0.0)', hidden: false})

  var ctx = document.getElementById('myChart').getContext('2d');
  var labelarr = jsondata.cases.map((i, idx)=> `day ${idx}`)

  var chart = new Chart(ctx, {
      type: 'line',
      data: {
          labels:labelarr,
          datasets: data
      },
      options: {
        legend: {
          display: true,
        },
        scales: {
            yAxes: [{
                stacked: false
            }],
            xAxes: [{
                stacked: true
            }]
        }

      }
  });

  function toggleAll(){
    chart.data.datasets.forEach(item=> item.hidden = !item.hidden)
  }
  document.toggleAll = toggleAll;
}


(function makeRequest(){
  let httpRequest = new XMLHttpRequest();
  let jsondata;
  httpRequest.onreadystatechange = function(data){
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
      if (httpRequest.status === 200) {
        jsondata = JSON.parse(httpRequest.responseText)
        const ordered = {}
        let keys = Object.keys(jsondata.states).sort();
        keys.forEach((key)=>{
          ordered[key] = jsondata.states[key];
        });
        jsondata.states = ordered;
        drawStuff(jsondata)
      }
    }
  }
  httpRequest.open('GET', './js/data.json');
  httpRequest.send();
}())
