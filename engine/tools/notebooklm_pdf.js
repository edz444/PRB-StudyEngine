// One PDF per lecture for NotebookLM (out/notebooklm/<slug>_<name>.pdf), cut from the built guide.
// Sections come from NOTEBOOKLM in course.py. Usage: node engine/tools/notebooklm_pdf.js [section-id]
const {chromium}=require('playwright'); const fs=require('fs'), path=require('path');
const C=require('./course');
const ONLY=process.argv[2];
const S0=JSON.parse(fs.readFileSync(path.join(C.OUT,'notebooklm.json'),'utf8'));
const S=ONLY?S0.filter(x=>x[0]===ONLY):S0;
const SLUG=(fs.readFileSync(path.join(C.COURSE,'course.py'),'utf8').match(/SLUG\s*=\s*'([^']+)'/)||[,'course'])[1].toUpperCase();
const DEST=path.join(C.OUT,'notebooklm'); fs.mkdirSync(DEST,{recursive:true});
const t0=Date.now();const L=(m)=>{ if(process.env.VERBOSE) console.log(((Date.now()-t0)/1000).toFixed(1),m); };
(async()=>{ C.linkAssets(); const {server,url}=await C.serve(C.OUT); const b=await chromium.launch({args:['--disable-dev-shm-usage','--disable-gpu']});
for(const [id,fn,title] of S){
 const p=await b.newPage({javaScriptEnabled:false,viewport:{width:900,height:1200},colorScheme:'light'});
 await C.blockExternal(p);
 await p.goto(url+'/index.html',{waitUntil:'load'});
 await p.evaluate(([id,title])=>{
  document.documentElement.setAttribute('data-theme','light');
  const main=document.querySelector('main'); const h=document.getElementById(id);
  const keep=[]; let n=h; while(n){ keep.push(n); n=n.nextElementSibling; if(n && n.tagName==='H2') break; }
  const EB=(document.querySelector('.hero .eyebrow')||{textContent:''}).textContent; main.innerHTML='';
  const hd=document.createElement('p'); hd.className='eyebrow'; hd.textContent=EB+'. '+title; main.appendChild(hd);
  keep.forEach(k=>main.appendChild(k));
  document.querySelectorAll('.topnav,.vprog,.lightbox,.labbox,.gpop,.rail').forEach(e=>e.remove());
  document.querySelectorAll('[class*="m3d"]').forEach(e=>{ if(e.closest('main')) e.remove(); });
  document.querySelectorAll('button.term').forEach(bt=>{const s=document.createElement('span'); s.textContent=bt.textContent; bt.replaceWith(s);});
  document.querySelectorAll('details').forEach(d=>d.open=true);
  const st=document.createElement('style'); st.textContent='@page{margin:16mm 14mm} body{background:#fff!important;font-size:14px} .wrap{max-width:none;padding:0} aside,figure,.tbl,table,img,svg{break-inside:avoid} h2,h3,h4{break-after:avoid} .slide img{max-height:120mm;width:auto;max-width:100%}';
  document.head.appendChild(st); window.scrollTo(0,0);
 },[id,title]);
 L('built'); L('built'); await p.waitForTimeout(300);
 await p.evaluate(async()=>{ await Promise.race([Promise.all([...document.images].map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r;}))), new Promise(r=>setTimeout(r,15000))]); });
 L('imgs waited'); await p.pdf({path:path.join(DEST,`${SLUG}_${fn}.pdf`),format:'Letter',printBackground:true});
 L('pdf done'); const imgs=await p.$$eval('main img',x=>x.filter(i=>i.naturalWidth>0).length); const svgs=await p.$$eval('main svg',x=>x.length);
 const words=await p.evaluate(()=>document.querySelector('main').innerText.split(/\s+/).length);
 console.log(fn,'imgs',imgs,'svgs',svgs,'words',words); await p.close();}
await b.close(); server.close();})();
