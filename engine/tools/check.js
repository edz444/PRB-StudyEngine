// Smoke test for the built guide and Lesson Path app at desktop (1280) and phone (390) widths, light and dark.
// Plays one lesson end to end, one boss level, and flips through a board view. Exits 1 on any failure.
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const C = require('./course');
const fails = []; const ok = (cond, msg) => { if (!cond) fails.push(msg); };

(async () => {
  C.linkAssets();
  const appFile = fs.readdirSync(path.join(C.OUT, 'lessons')).find(f => f.endsWith('-lesson-path.html'));
  const g = await C.serve(C.OUT), a = await C.serve(path.join(C.OUT, 'lessons'));
  const b = await chromium.launch({ args: ['--disable-dev-shm-usage'] });
  for (const [w, h, dark] of [[1280, 860, false], [390, 844, true]]) {
    const tag = `${w}px ${dark ? 'dark' : 'light'}`;
    // guide
    let p = await b.newPage({ viewport: { width: w, height: h }, colorScheme: dark ? 'dark' : 'light' });
    let errs = []; p.on('pageerror', e => errs.push(e.message));
    await C.blockExternal(p); await p.goto(g.url + '/index.html'); await p.waitForTimeout(500);
    ok((await p.evaluate(() => document.documentElement.scrollWidth)) <= w, `guide scrolls sideways at ${tag}`);
    ok(errs.length === 0, `guide errors at ${tag}: ${errs.join('; ')}`);
    await p.close();
    // app
    p = await b.newPage({ viewport: { width: w, height: h }, colorScheme: dark ? 'dark' : 'light' });
    errs = []; p.on('pageerror', e => errs.push(e.message));
    await C.blockExternal(p); await p.goto(a.url + '/' + appFile); await p.waitForTimeout(400);
    ok((await p.evaluate(() => document.documentElement.scrollWidth)) <= w, `app home scrolls sideways at ${tag}`);
    const first = await p.$('.node:not(.boss)'); await first.click(); await p.waitForTimeout(150);
    let finished = false;
    for (let k = 0; k < 80; k++) {
      for (const x of await p.$$('#pin .blank:not(.shown)')) await x.click();
      if (await p.$('.gm:not([hidden]) .got')) { await p.click('.gm .got'); await p.waitForTimeout(450); continue; }
      const over = await p.evaluate(() => { const s = document.querySelector('#pbody'); return s.scrollWidth - s.clientWidth; });
      ok(over <= 1, `lesson screen ${k} overflows at ${tag}`);
      const t = await p.$eval('#pnext', e => e.textContent);
      if (t.includes('Finish')) { await p.$$eval('.chk input[data-j]', xs => xs.forEach(x => x.click())); await p.click('#pnext'); await p.waitForTimeout(500); finished = true; break; }
      await p.click('#pnext'); await p.waitForTimeout(80);
    }
    ok(finished, `could not finish a lesson at ${tag}`);
    ok((await p.$eval('#pin', e => e.innerText)).includes('XP'), `no reward screen at ${tag}`);
    // board view
    await p.click('#pclose'); await p.click('.node:not(.boss) >> nth=1'); await p.click('#pboard'); await p.waitForTimeout(200);
    const pages = (await p.$$('.bd-dot')).length / 2 || 1;
    for (let k = 0; k < pages; k++) {
      const over = await p.evaluate(() => { const s = document.querySelector('#pbody'); return s.scrollWidth - s.clientWidth; });
      ok(over <= 1, `board page ${k + 1} overflows at ${tag}`);
      if (k < pages - 1) { await p.click('#pnext'); await p.waitForTimeout(100); }
    }
    // boss level
    await p.click('#pclose'); await p.click('.node.boss'); await p.waitForTimeout(150);
    let badge = false;
    for (let k = 0; k < 60; k++) {
      for (const x of await p.$$('#pin .blank:not(.shown)')) await x.click();
      if (await p.$('.gm:not([hidden]) .miss')) { await p.click('.gm .miss'); await p.waitForTimeout(450); continue; }
      const o = await p.$('.opt:not([disabled])'); if (o) await o.click();
      const t = await p.$eval('#pnext', e => e.textContent);
      if (t.includes('Claim')) { await p.click('#pnext'); await p.waitForTimeout(600); badge = true; break; }
      await p.click('#pnext'); await p.waitForTimeout(80);
    }
    ok(badge, `could not finish a boss level at ${tag}`);
    ok(errs.length === 0, `app errors at ${tag}: ${errs.join('; ')}`);
    console.log(`checked ${tag}: lesson, board (${pages} pages), boss`);
    await p.close();
  }
  await b.close(); g.server.close(); a.server.close();
  if (fails.length) { console.log('FAILED:\n- ' + fails.join('\n- ')); process.exit(1); }
  console.log('all checks passed');
})();
