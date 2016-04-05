
var margin = {top: 100, right: 100, bottom: 100, left: 100},
  legendPosition = {x: 25, y: 25},
  width = Math.min(700, window.innerWidth - 10) - margin.left - margin.right,
  height = Math.min(width, window.innerHeight - margin.top - margin.bottom - 20);

var color = d3.scale.ordinal()
  .range(["#EDC951","#CC333F","#00A0B0"]);
  
var radarChartOptions = {
  w: width,
  h: height,
  margin: margin,
  legendPosition: legendPosition,
  maxValue: 0.5,
  wrapWidth: 60,
  levels: 5,
  roundStrokes: true,
  color: color,
  axisName: "reason",
  areaName: "device",
  value: "value"
};

//Load the data and Call function to draw the Radar chart
d3.json("data_temp.json", function(error, data){
  RadarChart(".radarChart", data, radarChartOptions);
});
/*
setTimeout(function f() {
  d3.json("data2.json", function(error, data){
  RadarChart(".radarChart", data, radarChartOptions);
});
}  , 3000);
*/
var choosePlaylist = function(id) {
  alert("choose playlist " + id);
}