import { chromium } from 'playwright'; import fs from 'fs';
const [,, w, h, layout, theme, fit, dir, fps='30', only=''] = process.argv;
fs.mkdirSync(dir,{recursive:true});
const b = await chromium.launch(); const p = await b.newPage({viewport:{width:+w,height:+h}});
await p.goto(`file://${process.cwd()}/anim.html?w=${w}&h=${h}&layout=${layout}&theme=${theme}&fit=${fit}`);
const times = only ? only.split(',').map(Number) : null;
const N = Math.round(6*fps);
for (let i=0;i<(times?times.length:N);i++){
  const t = times ? times[i] : i/fps;
  await p.evaluate(t=>A.render(t), t);
  await p.screenshot({path:`${dir}/f${String(i).padStart(4,'0')}.png`});
}
await b.close();
