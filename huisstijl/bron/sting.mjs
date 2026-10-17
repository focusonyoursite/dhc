import { chromium } from 'playwright'; import fs from 'fs';
const [,, w, h, fit, dir] = process.argv; fs.mkdirSync(dir,{recursive:true});
const b = await chromium.launch(); const p = await b.newPage({viewport:{width:+w,height:+h}});
await p.goto(`file://${process.cwd()}/anim.html?w=${w}&h=${h}&layout=staand&theme=papier&fit=${fit}`);
const N = 81; // 2,7 s bij 30 fps; animatie op dubbele snelheid
for (let i=0;i<N;i++){ await p.evaluate(t=>A.render(t), Math.min(6, i/30*2)); await p.screenshot({path:`${dir}/f${String(i).padStart(4,'0')}.png`}); }
await b.close();
