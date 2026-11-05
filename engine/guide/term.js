(function(){
  const G = window.GLOSS || []; if(!G.length) return;
  const main = document.querySelector('main'); if(!main) return;
  const byMatch = new Map(); G.forEach((g,i)=>g.m.forEach(s=>byMatch.set(s,i)));
  const keys=[...byMatch.keys()].sort((a,b)=>b.length-a.length).map(s=>s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'));
  const W='A-Za-z0-9Ͱ-Ͽ';
  const re = new RegExp(`(?<![${W}-])(${keys.join('|')})(?![${W}])`,'g');
  const SKIP='svg,figure,h1,h2,h3,h4,a,button,.co-lab,.fig-tag,code,#glossary-body,.term,.m3d,.labcta,summary';
  let seen=new Set(), inGloss=false;
  [...main.children].forEach(el=>{
    if(el.tagName==='H2'){ seen=new Set(); inGloss = el.id==='glossary'; return; }
    if(inGloss || el.matches(SKIP)) return;
    seen=new Set();
    const tw=document.createTreeWalker(el,NodeFilter.SHOW_TEXT,{acceptNode:n=>(n.parentElement.closest(SKIP)?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT)});
    const nodes=[]; while(tw.nextNode()) nodes.push(tw.currentNode);
    nodes.forEach(n=>{
      const txt=n.nodeValue; re.lastIndex=0; let m, last=0, frag=null;
      while((m=re.exec(txt))){
        const gi=byMatch.get(m[1]); if(seen.has(gi)) continue; seen.add(gi);
        frag=frag||document.createDocumentFragment();
        frag.appendChild(document.createTextNode(txt.slice(last,m.index)));
        const b=document.createElement('button'); b.type='button'; b.className='term'; b.dataset.g=gi; b.textContent=m[1]; frag.appendChild(b);
        last=m.index+m[1].length;
      }
      if(frag){ frag.appendChild(document.createTextNode(txt.slice(last))); n.parentNode.replaceChild(frag,n); }
    });
  });
  const pop=document.createElement('div'); pop.className='gpop'; pop.hidden=true; pop.setAttribute('role','dialog'); document.body.appendChild(pop);
  let cur=null;
  const close=()=>{ pop.hidden=true; if(cur) cur.setAttribute('aria-expanded','false'); cur=null; };
  main.addEventListener('click',e=>{
    const b=e.target.closest('.term'); if(!b) return;
    e.stopPropagation();
    if(cur===b){ close(); return; }
    const g=G[+b.dataset.g];
    pop.innerHTML=`<p class="gpop-t">${g.t}</p><p class="gpop-d">${g.d}</p><p class="gpop-w">${g.w==='background'?'Background (Chapter 0)':'Comes up in: '+g.w}</p>`;
    pop.hidden=false; cur=b; b.setAttribute('aria-expanded','true');
    const r=b.getBoundingClientRect(), pw=Math.min(340, document.documentElement.clientWidth-24);
    pop.style.width=pw+'px';
    let left=r.left+window.scrollX; left=Math.max(12+window.scrollX, Math.min(left, window.scrollX+document.documentElement.clientWidth-pw-12));
    pop.style.left=left+'px'; pop.style.top=(r.bottom+window.scrollY+6)+'px';
  });
  document.addEventListener('click',e=>{ if(!pop.hidden && !pop.contains(e.target)) close(); });
  document.addEventListener('keydown',e=>{ if(e.key==='Escape') close(); });
})();
