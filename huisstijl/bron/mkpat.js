const fs = require('fs'); const P = JSON.parse(fs.readFileSync('parts.json','utf8')).parts;
const DP = require('./patterns.js'); fs.mkdirSync('out/patronen',{recursive:true});
const combos = {zwart:{bg:'#2B2828',fg:'#3A3838'}, geel:{bg:'#F2B705',fg:'#2B2828'}, groen:{bg:'#2D6A52',fg:'#FFFFFF',acc:'#F2B705'}, papier:{bg:'#EEE8DF',fg:'#2B2828',acc:'#F2B705'}};
for (const k of ['staven','schakels','raster']) for (const [n,c] of Object.entries(combos)) {
  const s = DP.svg(k, c, ({staven:.28,schakels:.2,raster:.18})[k], 2000, 2000, P);
  fs.writeFileSync(`out/patronen/dhc-patroon-${k}-${n}.svg`, s);
}
console.log('ok');
