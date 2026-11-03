// Authoring helper: lists each diagram's label groups (io/groups.json) so you can pick occlusion targets for anki/io_spec.py.
const { chromium } = require('playwright');
// Diagram ids to measure (MBB 322). Pass --all to measure every diagram in a new course.
const fs = require('fs'), path = require('path');
const C = require('./course');
const ALL = process.argv.includes('--all');
const WANT = ['gcycle','camp','plc','rod','na','syn','nmj','tools','rtk','ras','mapk','eph','hif','onc','src','ba','js','wnt','smad','met','mh','twohit','meth','dual','chr2','venn'];
(async () => {
  C.linkAssets(); const {server, url} = await C.serve(C.OUT);
  const b = await chromium.launch({args:['--disable-dev-shm-usage']});
  const p = await b.newPage({ viewport:{width:800,height:900}, colorScheme:'light', deviceScaleFactor:2, javaScriptEnabled:false });
  await C.blockExternal(p); await p.goto(url + '/index.html'); await p.waitForTimeout(300);
  const out = {};
  const wraps = await p.$$('figure.diagram .dg-wrap');
  for (const w of wraps) {
    const id = await w.$eval('svg', s => s.querySelector('defs marker').id.split('-')[0]);
    if ((!ALL && !WANT.includes(id)) || out[id]) continue;
    await w.scrollIntoViewIfNeeded(); await p.waitForTimeout(80);
    await w.screenshot({ path: path.join(C.BUILD, 'io_png', `${id}.png`) });
    const data = await w.evaluate((wrap) => {
      const wr = wrap.getBoundingClientRect();
      const svg = wrap.querySelector('svg');
      const title = svg.getAttribute('aria-label');
      const shapes = [...svg.querySelectorAll('rect, circle, ellipse')].filter(e => /\bf[TOAG]\b/.test(e.getAttribute('class')||'')).map(e => { const r=e.getBoundingClientRect(); return {el:e, x:r.left, y:r.top, w:r.width, h:r.height, area:r.width*r.height}; });
      const groups = new Map();
      [...svg.querySelectorAll('text')].forEach(t => {
        const txt = t.textContent.trim(); if (!txt) return;
        const fw = (t.getAttribute('style')||'').includes('font-weight:700');
        const r = t.getBoundingClientRect(); const cx=r.left+r.width/2, cy=r.top+r.height/2;
        let best=null; shapes.forEach(s=>{ if(cx>=s.x&&cx<=s.x+s.w&&cy>=s.y&&cy<=s.y+s.h&&(!best||s.area<best.area)) best=s; });
        const key = best ? best : t;
        if (!best && (fw || txt.length > 42)) return;
        if (!groups.has(key)) groups.set(key, {texts:[], boxes:[]});
        const g = groups.get(key); g.texts.push(txt); g.boxes.push([r.left-wr.left, r.top-wr.top, r.width, r.height]);
      });
      const res=[];
      groups.forEach(g=>{
        const label = g.texts.join(' ').replace(/\s+/g,' ').trim();
        if (label.replace(/[^A-Za-z0-9]/g,'').length < 3) return;
        if (['pump'].includes(label)) return;
        const x1=Math.min(...g.boxes.map(b=>b[0]))-3, y1=Math.min(...g.boxes.map(b=>b[1]))-2;
        const x2=Math.max(...g.boxes.map(b=>b[0]+b[2]))+3, y2=Math.max(...g.boxes.map(b=>b[1]+b[3]))+2;
        res.push({label, box:[x1,y1,x2,y2]});
      });
      return {title, groups:res};
    });
    out[id] = data;
  }
  fs.writeFileSync(path.join(C.COURSE, 'io', 'groups.json'), JSON.stringify(out, null, 1));
  console.log(Object.entries(out).map(([k,v])=>k+':'+v.groups.length).join(' '));
  await b.close(); server.close();
})();
