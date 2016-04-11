
var margin = {top: 100, right: 100, bottom: 100, left: 100},
  legendPosition = {x: 25, y: 25},
  width = Math.min(700, window.innerWidth - 10) - margin.left - margin.right,
  height = Math.min(width, window.innerHeight - margin.top - margin.bottom - 20);

var color = d3.scale.ordinal()
  .range(["#D9B435","#F76D0C","#CC3241","#7C15B0","#4249A1"]);
  
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
d3.json("playlist0.json", function(error, data){
  RadarChart(".radarChart", data, radarChartOptions);
});


//ASSUME names are playlist1.json, playlist2.json, ...
var choosePlaylist = function(id) {
  $("div").removeClass()
  d3.json("playlist" + id + ".json", function(error, data){
    RadarChart(".radarChart", data, radarChartOptions);
  });
}