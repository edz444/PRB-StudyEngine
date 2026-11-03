// Screenshot each diagram for image occlusion (build/io_png/<id>.png) and record every text label's box (io/lines.json).
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const C = require('./course');
(async () => {
  C.linkAssets(); const {server, url} = await C.serve(C.OUT);
  const png = path.join(C.BUILD, 'io_png'); fs.mkdirSync(png, {recursive: true}); fs.mkdirSync(path.join(C.COURSE, 'io'), {recursive: true});
  const b = await chromium.launch({args:['--disable-dev-shm-usage']});
  const p = await b.newPage({ viewport: {width: 800, height: 900}, colorScheme: 'light', deviceScaleFactor: 2, javaScriptEnabled: false });
  await C.blockExternal(p); await p.goto(url + '/index.html'); await p.waitForTimeout(300);
  const out = {};
  for (const w of await p.$$('figure.diagram .dg-wrap')) {
    const id = await w.$eval('svg', s => s.querySelector('defs marker').id.split('-')[0]);
    if (out[id]) continue;
    await w.scrollIntoViewIfNeeded(); await w.screenshot({ path: path.join(png, `${id}.png`) });
    out[id] = await w.evaluate(wrap => { const wr = wrap.getBoundingClientRect(); const svg = wrap.querySelector('svg');
      return {title: svg.getAttribute('aria-label'), lines: [...svg.querySelectorAll('text')].map(t => { const r = t.getBoundingClientRect(); return [t.textContent.trim(), r.left - wr.left, r.top - wr.top, r.width, r.height]; }).filter(l => l[0])}; });
  }
  fs.writeFileSync(path.join(C.COURSE, 'io', 'lines.json'), JSON.stringify(out));
  console.log(Object.keys(out).length, 'diagrams measured');
  await b.close(); server.close();
})();
