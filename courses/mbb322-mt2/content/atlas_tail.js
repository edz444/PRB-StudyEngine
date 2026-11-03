
const BY={}; SCENES.forEach(s=>BY[s.id]=s);
function engine(){
  if(R) return R;
  if(!window.THREE||!THREE.OrbitControls) return null;
  try{
    const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true}); renderer.setPixelRatio(Math.min(devicePixelRatio||1,2));
    const scene=new THREE.Scene(), cam=new THREE.PerspectiveCamera(42,1.4,.1,300);
    const ctl=new THREE.OrbitControls(cam,renderer.domElement); ctl.enableDamping=true; ctl.minDistance=4; ctl.maxDistance=45;
    scene.add(new THREE.HemisphereLight(0xffffff,0x8a8a8a,.85)); const dl=new THREE.DirectionalLight(0xffffff,.55); dl.position.set(6,12,10); scene.add(dl);
    R={renderer,scene,cam,ctl,host:null};
    const rs=()=>{ if(!R.host) return; const w=R.host.clientWidth||700, h=Math.round(Math.max(340,Math.min(560,w*.68))); renderer.setSize(w,h); cam.aspect=w/h; cam.updateProjectionMatrix(); };
    R.resize=rs; new ResizeObserver(rs).observe(document.body);
    const clock=new THREE.Clock();
    (function loop(){ requestAnimationFrame(loop); const dt=Math.min(clock.getDelta(),.05); if(!R.host) return; T+=dt;
      const k=1-Math.exp(-dt*(still?40:4.5));
      A.forEach(o=>{ o.position.lerp(o.userData.tp,k); o.scale.lerp(o.userData.ts,k);
        o.rotation.x+=(o.userData.tr.x-o.rotation.x)*k; o.rotation.y+=(o.userData.tr.y-o.rotation.y)*k; o.rotation.z+=(o.userData.tr.z-o.rotation.z)*k; });
      if(S&&S.live&&S.live.tick) S.live.tick(still?dt*.3:dt,T);
      ctl.update(); renderer.render(scene,cam); })();
    return R;
  }catch(e){ return null; }
}
function stopPlay(){ if(playing){ clearInterval(playing); playing=null; const b=$('play'); if(b) b.textContent='Play all steps'; } }
function caption(){ const c=$('cap'); c.classList.remove('alert'); c.textContent=S.steps[step][1]; if(S.live&&S.live.go) S.live.go(step); }
function go(k,instant){ step=k; ROOT.querySelectorAll('.a-steps button').forEach((b,j)=>b.setAttribute('aria-pressed',j===k)); caption(); if(instant) A.forEach(snap); }
function close(fig){
  stopPlay(); if(R && R.host===fig.querySelector('.m3d-stage')){ R.renderer.domElement.remove(); R.host=null; } fig.classList.remove('live'); fig.querySelector('.m3d-ui').hidden=true; fig.querySelector('.m3d-cover').hidden=false;
  fig.querySelector('.m3d-close').hidden=true;
}
function openFig(fig){
  const r=engine(); if(!r){ fig.querySelector('.m3d-open').textContent='3D needs WebGL, which is not available here'; return; }
  if(ROOT && ROOT!==fig) close(ROOT);
  ROOT=fig; S=BY[fig.dataset.scene]; tog={};
  const stage=fig.querySelector('.m3d-stage'); fig.querySelector('.m3d-cover').hidden=true; fig.querySelector('.m3d-close').hidden=false;
  stage.prepend(r.renderer.domElement); r.host=stage; r.resize(); fig.classList.add('live');
  const ui=fig.querySelector('.m3d-ui'); ui.hidden=false;
  ui.innerHTML=`<p class="a-notice m3d-notice">${S.notice}</p>
   <div class="a-steps m3d-steps">${S.steps.map((s,k)=>`<button type="button" aria-pressed="false" data-k="${k}"><span class="n">${k+1}</span>${s[0]}</button>`).join('')}</div>
   <div class="m3d-row"><button type="button" class="m3d-btn a-play">Play all steps</button>${(S.toggles||[]).map(t=>`<button type="button" class="m3d-btn" data-t="${t.id}" aria-pressed="false">${t.label}</button>`).join('')}<button type="button" class="m3d-btn a-reset">Reset view</button></div>
   <p class="a-cap m3d-cap" aria-live="polite"></p><div class="m3d-trap"><b>Exam trap:</b> ${S.trap}</div>`;
  ui.querySelectorAll('.a-steps button').forEach(b=>b.onclick=()=>{ stopPlay(); go(+b.dataset.k); });
  ui.querySelectorAll('[data-t]').forEach(b=>b.onclick=()=>{ const t=S.toggles.find(x=>x.id===b.dataset.t); if(!t.act){ tog[t.id]=!tog[t.id]; b.setAttribute('aria-pressed',tog[t.id]); } if(S.live.toggle) S.live.toggle(t.id); if(!t.act) caption(); });
  const resetCam=()=>{ r.cam.position.set(...S.cam); r.ctl.target.set(...S.tgt); r.ctl.update(); };
  ui.querySelector('.a-reset').onclick=resetCam;
  ui.querySelector('.a-play').onclick=()=>{ if(playing){ stopPlay(); return; } go(0); $('play').textContent='Pause'; playing=setInterval(()=>{ if(step>=S.steps.length-1){ stopPlay(); return; } go(step+1); },4200); };
  if(G) r.scene.remove(G); A=[]; G=new THREE.Group(); r.scene.add(G); S.live=S.build(G);
  resetCam(); go(0,true);
}
figs.forEach(f=>{ f.querySelector('.m3d-open').onclick=()=>openFig(f); f.querySelector('.m3d-close').onclick=()=>close(f); });
})();
