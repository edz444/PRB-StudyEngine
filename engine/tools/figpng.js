// Render every SVG diagram in the built guide to build/figpng/<id>.png (used on Anki card backs).
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const C = require('./course');
(async () => {
  C.linkAssets(); const {server, url} = await C.serve(C.OUT);
  const dir = path.join(C.BUILD, 'figpng'); fs.mkdirSync(dir, {recursive: true});
  const b = await chromium.launch({args:['--disable-dev-shm-usage']});
  const p = await b.newPage({ viewport: { width: 800, height: 900 }, colorScheme: 'light', deviceScaleFactor: 2, javaScriptEnabled: false });
  await C.blockExternal(p); await p.goto(url + '/index.html'); await p.waitForTimeout(300);
  const ids = await p.$$eval('figure.diagram svg', ss => ss.map(s => s.querySelector('defs marker').id.split('-')[0]));
  const wraps = await p.$$('figure.diagram .dg-wrap');
  for (let i = 0; i < wraps.length; i++) await wraps[i].screenshot({ path: path.join(dir, `${ids[i]}.png`) });
  console.log(wraps.length, 'diagram PNGs ->', dir);
  await b.close(); server.close();
})();
