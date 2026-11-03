// Shared helper for the browser scripts: finds the course folder and serves its out/ folder over a tiny local server.
const fs = require('fs'), path = require('path'), http = require('http');
const ROOT = path.resolve(__dirname, '..', '..');
function courseDir(){
  if (process.env.COURSE) return path.resolve(ROOT, process.env.COURSE);
  const cs = fs.readdirSync(path.join(ROOT, 'courses')).filter(n => !n.startsWith('_') && fs.statSync(path.join(ROOT, 'courses', n)).isDirectory()).sort();
  return path.join(ROOT, 'courses', cs[0]);
}
const COURSE = courseDir(), OUT = path.join(COURSE, 'out'), BUILD = path.join(COURSE, 'build');
const TYPES = {'.html':'text/html; charset=utf-8','.js':'application/javascript','.css':'text/css','.jpg':'image/jpeg','.png':'image/png','.json':'application/json'};
function serve(dir){
  return new Promise(res => {
    const s = http.createServer((q, r) => {
      const f = path.join(dir, decodeURIComponent(q.url.split('?')[0]).replace(/^\/+/, '') || 'index.html');
      if (!f.startsWith(dir) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { r.writeHead(404); return r.end(); }
      r.writeHead(200, {'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream'}); fs.createReadStream(f).pipe(r);
    }).listen(0, '127.0.0.1', () => res({server: s, url: `http://127.0.0.1:${s.address().port}`}));
  });
}
// Index.html links slides/ and m3d/ relative to itself; expose them inside out/ via the course folder.
function linkAssets(){
  for (const d of ['slides', 'm3d']) {
    const src = path.join(COURSE, d), dst = path.join(OUT, d);
    if (fs.existsSync(src) && !fs.existsSync(dst)) fs.symlinkSync(src, dst, 'dir');
  }
}
// Block web fonts and CDN scripts: pages must render without them, and the sandbox may not reach them.
async function blockExternal(page){ await page.route(/^https?:\/\/(?!127\.0\.0\.1)/, r => r.abort()); }
module.exports = { ROOT, COURSE, OUT, BUILD, serve, linkAssets, blockExternal };
