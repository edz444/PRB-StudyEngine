/* Inline 3D models: one shared WebGL renderer, mounted into whichever figure the reader opens. */
(function(){
const figs=[...document.querySelectorAll('figure.m3d')];
if(!figs.length) return;
let ROOT=null;
const $=id=>ROOT?ROOT.querySelector('.a-'+id):null;
const css=v=>getComputedStyle(document.documentElement).getPropertyValue(v).trim();
const C={teal:0x0e7490,soft:0x9fd3df,orange:0xc2410c,amber:0xe0a33a,mem:0xe6c98a,slate:0xb9b4ab,red:0xd94a3a,purple:0x7b5cc7,yellow:0xf2c230,green:0x2f9e62,white:0xf1ece2,pink:0xe7a0a0,blue:0x3b82f6,dark:0x5a4a7a,blood:0xd04848};
const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
let R=null, S=null, G=null, A=[], step=0, playing=null, tog={}, T=0;
function mat(c,o=1,e=0){ return new THREE.MeshStandardMaterial({color:c,transparent:o<1,opacity:o,depthWrite:o>=1,roughness:.5,metalness:.05,emissive:c,emissiveIntensity:e,side:o<1?THREE.DoubleSide:THREE.FrontSide}); }
function M(geo,m,x=0,y=0,z=0){ const o=new THREE.Mesh(geo,m); o.position.set(x,y,z); return o; }
const Cyl=(r,h,s=20)=>new THREE.CylinderGeometry(r,r,h,s), Sph=(r,s=20)=>new THREE.SphereGeometry(r,s,Math.max(8,s*0.6)), Box=(a,b,c)=>new THREE.BoxGeometry(a,b,c);
function an(o){ o.userData.tp=o.position.clone(); o.userData.ts=o.scale.clone(); o.userData.tr=o.rotation.clone(); A.push(o); return o; }
function to(o,x,y,z){ o.userData.tp.set(x,y,z); }
function sc(o,s){ if(typeof s==='number') o.userData.ts.setScalar(s); else o.userData.ts.set(...s); }
function rot(o,x,y,z){ o.userData.tr.set(x,y,z); }
function snap(o){ o.position.copy(o.userData.tp); o.scale.copy(o.userData.ts); o.rotation.copy(o.userData.tr); }
function label(text,{size=1,bg=true}={}){
  const c=document.createElement('canvas'); const sp=new THREE.Sprite(new THREE.SpriteMaterial({depthTest:false,transparent:true}));
  sp.renderOrder=20;
  sp.set=t=>{ const g=c.getContext('2d'), f=30, pad=14, ls=String(t).split('\n');
    g.font=`700 ${f}px Atkinson Hyperlegible, Segoe UI, sans-serif`;
    const w=Math.ceil(Math.max(...ls.map(l=>g.measureText(l).width)))+pad*2, h=ls.length*(f+6)+pad*1.3;
    c.width=w; c.height=h; g.font=`700 ${f}px Atkinson Hyperlegible, Segoe UI, sans-serif`;
    if(bg){ g.fillStyle=css('--surface')||'#fff'; g.strokeStyle=css('--line')||'#ccc'; g.lineWidth=3; g.beginPath(); g.roundRect?g.roundRect(2,2,w-4,h-4,14):g.rect(2,2,w-4,h-4); g.fill(); g.stroke(); }
    g.fillStyle=css('--ink')||'#222'; g.textAlign='center'; g.textBaseline='middle';
    ls.forEach((l,i)=>g.fillText(l,w/2,pad*0.65+(f+6)*(i+0.5)));
    if(sp.material.map) sp.material.map.dispose();
    sp.material.map=new THREE.CanvasTexture(c); sp.material.needsUpdate=true;
    sp.scale.set(w/95*size,h/95*size,1); };
  sp.set(text); return sp;
}
function L(G,text,x,y,z,o){ const s=label(text,o); s.position.set(x,y,z); G.add(s); return s; }
function rnd(a,b){ return a+Math.random()*(b-a); }
