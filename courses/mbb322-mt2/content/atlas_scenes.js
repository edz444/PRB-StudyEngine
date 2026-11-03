/* ---------- scenes ---------- */
const SCENES=[
{ id:'na', name:'Na+ channel: three states', lec:'Lecture 6', cam:[6,4,13], tgt:[0,0,0],
  notice:'Watch the red voltage sensors and the orange plug. Closed and inactivated both stop Na+, but only closed can open again.',
  trap:'Closed is not inactivated. A closed channel opens when the membrane depolarizes; an inactivated one is plugged from the cytosol side and cannot open until the membrane repolarizes. That plug is why the action potential only moves forward.',
  steps:[['Closed (at rest)','At rest (about -70 mV) the pore is shut but ready: a small depolarization will open it.'],
   ['Open','Depolarization pushes the positively charged S4 voltage sensors outward. The pore opens in under 0.1 ms and Na+ rushes in, pushed by both its concentration gradient and the negative inside.'],
   ['Inactivated','Within about 1 ms the inactivation segment swings up from the cytosol and plugs the pore. The membrane is still depolarized, but no Na+ passes and the channel cannot reopen: the refractory period.'],
   ['Back to closed','Repolarization (delayed K+ channels letting K+ out) moves the sensors back down and the plug swings out. The channel is closed and ready again.']],
  build(G){
    G.add(M(Box(12,1.6,7),mat(C.mem,.32)));
    L(G,'OUTSIDE (Na+ high)',-4.2,3.2,0,{size:.8}); L(G,'CYTOSOL',-4.6,-2.6,0,{size:.8}); L(G,'membrane',5.2,.2,2.6,{size:.7});
    const doms=[], s4=[];
    for(let k=0;k<4;k++){ const a=k*Math.PI/2+Math.PI/4;
      doms.push([an(M(Cyl(.5,2.4),mat(C.teal),Math.cos(a)*.75,0,Math.sin(a)*.75)),a]);
      s4.push([an(M(Cyl(.14,1),mat(C.red,1,.25),Math.cos(a)*1.4,-.35,Math.sin(a)*1.4)),a]); }
    doms.forEach(d=>G.add(d[0])); s4.forEach(d=>G.add(d[0]));
    L(G,'S4 voltage sensors (+)',2.9,1.6,1.2,{size:.75});
    const plug=an(M(Sph(.42),mat(C.orange),2,-2.1,0)); G.add(plug); const pl=L(G,'inactivation plug',3.3,-2.4,0,{size:.75});
    const chainGeo=new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(1.1,-1.2,0),new THREE.Vector3(2,-2.1,0)]);
    const chain=new THREE.Line(chainGeo,new THREE.LineBasicMaterial({color:C.orange})); G.add(chain);
    const mv=L(G,'Membrane: -70 mV',-3.8,1.6,2.6,{size:.85});
    const ions=[]; for(let i=0;i<18;i++){ const o=M(Sph(.17,12),mat(C.purple,1,.15),rnd(-5,5),rnd(1.3,3.2),rnd(-3,3)); o.userData.ph='out'; ions.push(o); G.add(o); }
    const lab=L(G,'Na+',-1.6,2.7,-2.2,{size:.7});
    return {
      go(i){ const r=(i===1||i===2)?1.0:.72; doms.forEach(([d,a])=>to(d,Math.cos(a)*r,0,Math.sin(a)*r));
        s4.forEach(([d,a])=>to(d,Math.cos(a)*(r+.65),(i===1||i===2)?.55:-.35,Math.sin(a)*(r+.65)));
        if(i===2) to(plug,0,-1.15,0); else to(plug,2,-2.1,0);
        mv.set(['Membrane: -70 mV','Membrane: rising to +40 mV','Membrane: still depolarized','Membrane: back to -70 mV'][i]); },
      tick(dt,t){ const p=chain.geometry.attributes.position; p.setXYZ(1,plug.position.x,plug.position.y,plug.position.z); p.needsUpdate=true; pl.position.set(plug.position.x+1.3,plug.position.y-.35,0);
        ions.forEach((o,j)=>{ const u=o.userData;
          if(u.ph==='out'){ if(step===1){ const tg=new THREE.Vector3(0,1.4,0); o.position.lerp(tg,dt*(.6+j%5*.15)); if(o.position.distanceTo(tg)<.35) u.ph='down'; } else o.position.y+=Math.sin(t*2+j)*.003; }
          else { o.position.y-=dt*3; o.position.x*=.9; o.position.z*=.9; if(o.position.y<-3){ o.position.set(rnd(-5,5),rnd(2.2,3.2),rnd(-3,3)); u.ph='out'; } } }); }
    }; }},

{ id:'axon', name:'Action potential and myelin', lec:'Lecture 6', cam:[0,6,21], tgt:[0,0,0],
  notice:'The teal ring is the action potential. Teal bands mark nodes of Ranvier, where the Na+ channels are. The orange zone behind the spike is inactivated channels.',
  trap:'Myelin makes conduction faster (saltatory: node to node). It is NOT why the spike goes one way. One-way travel comes from the inactivated Na+ channels left behind it. MS damages CNS myelin; Guillain-Barré damages PNS myelin.',
  steps:[['Myelinated axon','Myelin insulates the axon, so the spike only has to regenerate at the nodes of Ranvier. It jumps node to node: saltatory conduction. Watch the timer.'],
   ['Unmyelinated axon','No insulation: every patch of membrane has to fire in turn, so the spike crawls. Compare the timer with step 1.'],
   ['Why only forward? (slow motion)','Behind the spike the Na+ channels are inactivated (orange). They cannot fire, so the spike can only move into fresh membrane ahead of it.']],
  toggles:[{id:'fire',label:'Fire again',act:true}],
  build(G){
    const ax=M(Cyl(.45,18,28),mat(C.soft)); ax.rotation.z=Math.PI/2; G.add(ax);
    const nodes=[-9,-6,-3,0,3,6,9]; const sheaths=[];
    nodes.slice(0,-1).forEach(x=>{ const s=an(M(Cyl(.85,2.4,28),mat(C.white,.92))); s.rotation.z=Math.PI/2; s.userData.tr.z=Math.PI/2; s.position.x=x+1.5; s.userData.tp.x=x+1.5; G.add(s); sheaths.push(s); });
    nodes.forEach(x=>{ const r=M(new THREE.TorusGeometry(.5,.08,10,30),mat(C.teal,1,.2),x,0,0); r.rotation.y=Math.PI/2; G.add(r); });
    L(G,'nodes of Ranvier (Na+ channels)',-6,1.9,0,{size:1.2}); const ml=L(G,'myelin sheath',1.5,1.9,0,{size:1.2});
    const wave=M(new THREE.TorusGeometry(.95,.16,12,36),mat(C.teal,1,.8)); wave.rotation.y=Math.PI/2; G.add(wave);
    const trail=M(Cyl(.62,1.8),mat(C.orange,.55,.3)); trail.rotation.z=Math.PI/2; G.add(trail);
    const tl=L(G,'Inactivated: cannot fire',0,-1.8,0,{size:1.2});
    const timer=L(G,'time: 0.0',0,3.4,0,{size:1.4});
    let x=-9, run=true, acc=0, el=0, ni=0; const res={};
    const restart=()=>{ x=-9; ni=0; acc=0; el=0; run=true; };
    return {
      go(i){ sheaths.forEach(s=>sc(s,i===1||i===2?0.001:1)); ml.visible=!(i===1||i===2); restart(); },
      toggle(){ restart(); },
      tick(dt){ if(!run) return; el+=dt;
        if(step===0){ acc+=dt; if(acc>.28){ acc=0; ni=Math.min(ni+1,nodes.length-1); } x=nodes[ni]; }
        else x+= (step===1?2.2:.8)*dt;
        if(x>=9){ x=9; run=false; res[step]=el; }
        wave.position.x=x; trail.position.x=x-(step===0?1.5:1.1); trail.visible=x>-8.2; tl.position.x=trail.position.x; tl.visible=step===2&&trail.visible;
        timer.set(`time: ${el.toFixed(1)} s${!run?'  (done)':''}${res[0]&&res[1]?`   myelinated ${res[0].toFixed(1)} vs unmyelinated ${res[1].toFixed(1)}`:''}`); }
    }; }},

{ id:'syn', name:'Synapse: calcium is the send button', lec:'Lecture 6', cam:[6,2.5,11], tgt:[0,.5,0],
  notice:'Yellow = Ca2+. Teal dots = neurotransmitter. Nothing is released until Ca2+ comes in.',
  trap:'The Ca2+ channel at the terminal is voltage-gated (opened by the action potential), not ligand-gated. Botulinum toxin cuts SNAREs (no release, paralysis); sarin blocks acetylcholinesterase (transmitter never cleared); curare blocks the receptor.',
  steps:[['Loaded and docked','Vesicles were filled by an H+ antiporter and wait at the membrane, held by SNARE proteins. Synaptotagmin (the Ca2+ sensor) keeps them from fusing.'],
   ['Action potential arrives','The spike opens voltage-gated Ca2+ channels and Ca2+ rushes into the terminal.'],
   ['Vesicles fuse','Ca2+ binds synaptotagmin, docked vesicles fuse with the membrane, and transmitter spills into the cleft.'],
   ['Receptors open','Transmitter binds receptors on the postsynaptic cell (ligand-gated channels or GPCRs). Here, channels open.'],
   ['Clean-up','Reuptake transporters and enzymes clear the cleft, and vesicle membrane is recycled by endocytosis, ready to refill.']],
  toggles:[{id:'botox',label:'Add botulinum toxin'}],
  build(G){
    const dome=M(new THREE.SphereGeometry(3,40,20,0,Math.PI*2,0,Math.PI/2),mat(C.mem,.3),0,1,0); G.add(dome);
    G.add(M(Cyl(3,.14,40),mat(C.mem,.7),0,1,0));
    G.add(M(Box(9,1,6),mat(C.pink,.55),0,-1.4,0));
    L(G,'presynaptic terminal',-3.6,3.6,0,{size:.8}); L(G,'synaptic cleft',4.2,.1,0,{size:.75}); L(G,'postsynaptic cell',-3.4,-2.4,0,{size:.8});
    const cach=[-2.4,2.4].map(x=>{ const o=M(Cyl(.28,.7),mat(C.amber),x,1,0); G.add(o); return o; }); L(G,'voltage-gated\nCa2+ channel',-2.4,2.2,1.6,{size:.65});
    const recs=[-1.5,-.5,.5,1.5].map(x=>{ const o=M(Cyl(.25,.55),mat(C.slate),x,-.72,0); G.add(o); return o; }); L(G,'receptors',1.9,-.3,1.6,{size:.7});
    const ves=[]; [[-1,1.55,0],[0,1.55,.6],[1,1.55,-.4],[-.6,2.6,-.8],[.8,2.6,.7],[0,3.4,0]].forEach((p,i)=>{
      const g=new THREE.Group(); g.add(M(Sph(.42),mat(C.white,.6))); for(let k=0;k<5;k++) g.add(M(Sph(.07,8),mat(C.teal,1,.4),rnd(-.2,.2),rnd(-.2,.2),rnd(-.2,.2)));
      g.position.set(...p); G.add(g); an(g); g.userData.home=p; g.userData.dock=i<3; ves.push(g); });
    const tx=[]; for(let i=0;i<24;i++){ const o=M(Sph(.09,8),mat(C.teal,1,.4)); o.visible=false; G.add(o); tx.push(o); }
    const ca=[]; for(let i=0;i<12;i++){ const o=M(Sph(.12,8),mat(C.yellow,1,.3)); o.visible=false; G.add(o); ca.push(o); }
    const ions=[]; for(let i=0;i<10;i++){ const o=M(Sph(.1,8),mat(C.purple,1,.2)); o.visible=false; G.add(o); ions.push(o); }
    let st=0;
    return {
      go(i){ st=0; const bx=tog.botox;
        ves.forEach(v=>{ const h=v.userData.home; if(v.userData.dock && i>=2 && i<4 && !bx){ to(v,h[0],1.05,h[2]); sc(v,.001); } else { to(v,...h); sc(v,1); } });
        recs.forEach(r=>r.material.color.setHex(i===3&&!bx?C.teal:C.slate));
        tx.forEach((o,k)=>{ const d=ves[k%3].userData.home; o.position.set(d[0]+rnd(-.3,.3),.9,d[2]+rnd(-.3,.3)); o.userData.tg=new THREE.Vector3([-1.5,-.5,.5,1.5][k%4]+rnd(-.15,.15),-.4,rnd(-.2,.2)); o.visible=(i===2||i===3||i===4)&&!bx; });
        ca.forEach((o,k)=>{ const x=k%2?2.4:-2.4; o.position.set(x+rnd(-.2,.2),rnd(-.6,0),rnd(-.4,.4)); o.visible=i>=1&&i<=2; });
        ions.forEach((o,k)=>{ o.position.set([-1.5,-.5,.5,1.5][k%4],rnd(-.3,.4),0); o.visible=i===3&&!bx; });
        $('cap').classList.toggle('alert', bx&&i>=2);
        if(bx&&i>=2) $('cap').textContent='Botulinum toxin has cut the SNARE proteins: vesicles cannot fuse, so no transmitter is released no matter how much Ca2+ comes in. Result: paralysis.'; },
      toggle(id){ this.go(step); },
      tick(dt,t){ ca.forEach(o=>{ if(!o.visible) return; o.position.y+=dt*1.6; if(o.position.y>2.3) o.position.y=rnd(-.6,0); });
        tx.forEach(o=>{ if(!o.visible) return; if(step===4){ o.position.lerp(new THREE.Vector3(Math.sign(o.position.x||1)*3.2,.4,0),dt*1.2); if(Math.abs(o.position.x)>3) o.visible=false; } else o.position.lerp(o.userData.tg,dt*1.5); });
        ions.forEach(o=>{ if(!o.visible) return; o.position.y-=dt*1.4; if(o.position.y<-1.9) o.position.y=.4; }); }
    }; }},

{ id:'sarc', name:'Sarcomere: Ca2+, troponin, tropomyosin', lec:'Lecture 6', cam:[2,5,12], tgt:[0,0,0],
  notice:'Pink beads = actin, dark rods = tropomyosin with yellow troponin, purple core = myosin. Red dots appear when myosin-binding sites are uncovered.',
  trap:'Ca2+ binds troponin (not tropomyosin, not myosin). Troponin then shifts tropomyosin off the binding sites. And in contraction the filaments slide: actin and myosin stay the same length, the Z disks move closer.',
  steps:[['Relaxed','Tropomyosin lies along actin and covers the myosin-binding sites. Myosin cannot grab.'],
   ['Ca2+ binds troponin','Ca2+ from the SR binds troponin. Troponin changes shape and drags tropomyosin aside, exposing the binding sites (red).'],
   ['Myosin pulls','Myosin heads grab actin and pull (using ATP). Actin slides toward the middle, the Z disks move closer. Check the length readout: filaments do not shrink.'],
   ['Ca2+ pumped away','Ca2+ is pumped back into the SR, tropomyosin covers the sites again, and the muscle relaxes.']],
  build(G){
    const mk=side=>{ const g=new THREE.Group(); g.add(M(Box(.2,3.6,3.6),mat(C.dark,.55)));
      const fil=[], sites=[];
      [[.95,.95],[.95,-.95],[-.95,.95],[-.95,-.95]].forEach(([y,z])=>{
        for(let k=0;k<12;k++){ const b=M(Sph(.16,10),mat(C.pink),side*(.25+k*.3),y,z); g.add(b); if(k%3===1) sites.push(b); }
        const tm=new THREE.Group(); tm.add(M(Cyl(.06,3.5,8),mat(0x3a3a3a))); tm.children[0].rotation.z=Math.PI/2;
        [.7,1.8,2.9].forEach(xx=>tm.add(M(Sph(.12,8),mat(C.yellow,1,.2),side*(xx-1.75),0,0)));
        tm.position.set(side*1.9,y+.18*Math.sign(y),z); tm.userData.base=[side*1.9,y,z]; g.add(an(tm)); fil.push(tm); });
      return {g,fil,sites}; };
    const Lf=mk(1), Rf=mk(-1); an(Lf.g); an(Rf.g); G.add(Lf.g,Rf.g);
    const my=M(Cyl(.32,5.2,16),mat(C.dark)); my.rotation.z=Math.PI/2; G.add(my);
    const heads=[]; [-2,-1.2,-.4,.4,1.2,2].forEach(x=>[[1,1],[1,-1],[-1,1],[-1,-1]].forEach(([y,z])=>{ const h=M(Sph(.17,10),mat(C.purple),x,y*.55,z*.55); h.userData.x=x; G.add(h); heads.push(h); }));
    const ca=[]; for(let i=0;i<14;i++){ const o=M(Sph(.11,8),mat(C.yellow,1,.4),rnd(-4,4),rnd(-1.6,1.6),rnd(-1.6,1.6)); o.visible=false; G.add(o); ca.push(o); }
    L(G,'Z disk',-5,2.4,0,{size:.75}); L(G,'Z disk',5,2.4,0,{size:.75}); L(G,'actin (thin)',-3,-1.9,1.4,{size:.7}); L(G,'myosin (thick)',0,.1,2.2,{size:.7}); L(G,'tropomyosin +\ntroponin',3,1.9,1.3,{size:.7});
    const len=L(G,'Z to Z: 10.0   actin length: same',0,3.4,0,{size:.85});
    return {
      go(i){ const Z=i===2?3.6:5; to(Lf.g,-Z,0,0); to(Rf.g,Z,0,0);
        const ex=i===1||i===2; [Lf,Rf].forEach(f=>{ f.fil.forEach(tm=>{ const [x,y,z]=tm.userData.base; to(tm,x,ex?y:y+.18*Math.sign(y),ex?z+.24*Math.sign(z):z); }); f.sites.forEach(b=>{ b.material.color.setHex(ex?C.red:C.pink); b.material.emissiveIntensity=ex?.4:0; }); });
        ca.forEach(o=>o.visible=ex); len.set(`Z to Z: ${(2*Z).toFixed(1)}   actin length: same`); },
      tick(dt,t){ heads.forEach((h,k)=>{ h.position.x=h.userData.x+(step===2?Math.sin(t*7+k)*.14:0); }); ca.forEach((o,k)=>{ if(o.visible) o.position.y+=Math.sin(t*3+k)*.004; }); }
    }; }},

{ id:'gp', name:'G protein switch', lec:'Lecture 5', cam:[3,2.5,12], tgt:[0,-.5,0],
  notice:'Follow the small token on Gα: grey = GDP (off), orange = GTP (on). Purple beads are cAMP.',
  trap:'The receptor acts as a GEF (it lets GDP out so GTP can get in); it does not hand Gα energy. Either Gα-GTP or Gβγ can carry the signal (Gβγ opens the heart K+ channel). If Gα cannot hydrolyze GTP (cholera toxin, non-hydrolyzable GTP), the signal never turns off.',
  steps:[['OFF','Gα holds GDP and sits bound to Gβγ. No ligand, nothing happening.'],
   ['Ligand binds','The hormone binds the 7-pass receptor, which changes shape and grabs the G protein. The receptor acts as a GEF.'],
   ['GDP out, GTP in','Gα lets go of GDP, and GTP (far more plentiful in the cytosol) jumps in.'],
   ['Split and signal','Gα-GTP separates from Gβγ and switches on adenylyl cyclase, which makes cAMP. Gβγ is free too and can signal on its own.'],
   ['Timer runs out','Gα hydrolyzes its own GTP to GDP + Pi, leaves the cyclase and rejoins Gβγ. Signal off.']],
  toggles:[{id:'cholera',label:'Add cholera toxin'}],
  build(G){
    G.add(M(Box(12,1.4,6),mat(C.mem,.3)));
    L(G,'OUTSIDE',-5,2.6,0,{size:.75}); L(G,'CYTOSOL',-5,-2.6,0,{size:.75});
    const hel=[]; for(let k=0;k<7;k++){ const a=k/7*Math.PI*2; const h=an(M(Cyl(.22,2),mat(C.teal),-3+Math.cos(a)*.75,0,Math.sin(a)*.75)); hel.push([h,a]); G.add(h); }
    L(G,'GPCR (7 passes)',-3,1.9,1.5,{size:.7});
    const lig=an(M(new THREE.IcosahedronGeometry(.45,1),mat(C.amber),-3,4.2,0)); G.add(lig); L(G,'hormone',-1.7,4.3,0,{size:.65});
    const ga=an(M(Sph(.65),mat(C.teal),-1.6,-1.3,0)); G.add(ga);
    const tok=M(Sph(.22,12),mat(C.slate),0,.55,.35); ga.add(tok);
    const gal=label('Gα·GDP',{size:.7}); gal.position.set(0,1.1,0); ga.add(gal);
    const gbg=new THREE.Group(); gbg.add(M(Sph(.45),mat(C.soft),0,0,.25),M(Sph(.42),mat(C.soft),.35,-.05,-.3)); gbg.position.set(-.45,-1.35,0); G.add(gbg);
    const bgl=L(G,'Gβγ',-.3,-2.2,0,{size:.7});
    const cyc=[M(Cyl(.35,1.9),mat(C.slate),2.9,0,.4),M(Cyl(.35,1.9),mat(C.slate),3.5,0,-.3)]; G.add(...cyc); L(G,'adenylyl cyclase',3.3,1.8,0,{size:.7});
    const camp=[]; for(let i=0;i<16;i++){ const o=M(Sph(.12,8),mat(C.purple,1,.3)); o.visible=false; G.add(o); camp.push(o); }
    const gdp=an(M(Sph(.2,10),mat(C.slate),-1.6,-1.3,0)); gdp.visible=false; G.add(gdp);
    let on=false;
    return {
      go(i){ const ch=tog.cholera && i===4;
        to(lig,-3,i>=1&&!(i===4&&!ch)?1.25:4.2,0);
        hel.forEach(([h,a])=>rot(h,(i>=1&&i<=3)||ch?Math.sin(a)*.18:0,0,(i>=1&&i<=3)||ch?Math.cos(a)*.18:0));
        const gtp = (i>=2 && i<=3) || ch;
        tok.material.color.setHex(gtp?C.orange:C.slate); tok.material.emissive.setHex(gtp?C.orange:C.slate); tok.material.emissiveIntensity=gtp?.4:0;
        gal.set(gtp?'Gα·GTP':(i===4?'Gα·GDP (+ Pi)':'Gα·GDP'));
        if(i===1) to(ga,-2.3,-1.3,0); else if(i===3||ch) to(ga,2.4,-1.35,0); else to(ga,-1.6,-1.3,0);
        on = i===3 || ch; cyc.forEach(c=>{ c.material.color.setHex(on?C.teal:C.slate); c.material.emissive.setHex(on?C.teal:0); c.material.emissiveIntensity=on?.3:0; });
        bgl.set(i===3||ch?'Gβγ (free, can signal too)':'Gβγ');
        gdp.visible=i===2; if(i===2){ gdp.position.set(-2.1,-1.1,.4); to(gdp,-3.5,-3.2,1.2); }
        camp.forEach(o=>{ o.position.set(3.2+rnd(-.4,.4),-1,rnd(-.4,.4)); o.visible=on; });
        $('cap').classList.toggle('alert',ch);
        if(ch) $('cap').textContent='Cholera toxin has ADP-ribosylated Gαs, so it cannot hydrolyze GTP. The timer never runs out: Gα stays on the cyclase and cAMP keeps pouring out (in gut cells: water loss, severe diarrhea).'; },
      toggle(){ this.go(step); },
      tick(dt){ camp.forEach(o=>{ if(!o.visible) return; o.position.y-=dt*1.3; o.position.x+=dt*.3; if(o.position.y<-3.6){ o.position.set(3.2+rnd(-.4,.4),-1,rnd(-.4,.4)); } }); }
    }; }},

{ id:'opto', name:'Optogenetics: ChR2 vs halorhodopsin', lec:'Lecture 7', cam:[0,3,12], tgt:[0,0,0],
  notice:'Left: ChR2, a channel. Right: halorhodopsin, a pump. The bar on the right is the membrane potential.',
  trap:'ChR2 is the channel itself (not a GPCR, even with 7 helices and retinal). Halorhodopsin is a pump: light drives Cl- into the cell, which hyperpolarizes and silences the neuron. Firing = cations in; silencing = Cl- in (HR) or H+ out (bacteriorhodopsin).',
  steps:[['Dark','No light: ChR2 is closed, halorhodopsin is idle. The neuron rests near -70 mV.'],
   ['Blue light on ChR2','Blue light (about 470 nm) flips ChR2\'s retinal from all-trans to 13-cis. The pore opens, cations (mostly Na+) flood in, the membrane depolarizes and the neuron fires.'],
   ['Light on halorhodopsin','Light drives halorhodopsin to pump Cl- into the cell. Negative charge in makes the inside more negative: the neuron hyperpolarizes and is silenced.']],
  build(G){
    G.add(M(Box(12,1.4,6),mat(C.mem,.3))); L(G,'OUTSIDE',-5,2.6,-2,{size:.7}); L(G,'NEURON CYTOSOL',-4.6,-2.6,-2,{size:.7});
    const chr=[]; for(let k=0;k<4;k++){ const a=k*Math.PI/2+Math.PI/4; const o=an(M(Cyl(.38,2),mat(C.teal),-2.5+Math.cos(a)*.55,0,Math.sin(a)*.55)); o.userData.a=a; chr.push(o); G.add(o); }
    L(G,'ChR2 (channel)',-2.5,1.9,1.4,{size:.75});
    const hr=M(Sph(.85,28),mat(C.green)); hr.scale.set(1,1.35,1); hr.position.set(2.5,0,0); G.add(hr); L(G,'halorhodopsin (pump)',2.5,1.9,1.4,{size:.75});
    const coneB=M(new THREE.ConeGeometry(1.3,3.2,32,1,true),mat(C.blue,.25,.6),-2.5,3,0); coneB.rotation.x=Math.PI; G.add(coneB);
    const coneY=M(new THREE.ConeGeometry(1.3,3.2,32,1,true),mat(C.amber,.25,.6),2.5,3,0); coneY.rotation.x=Math.PI; G.add(coneY);
    const bar=M(Box(.5,1,.5),mat(C.teal)); G.add(bar); const mv=L(G,'-70 mV',5.6,-2.4,0,{size:.75});
    const cat=[]; for(let i=0;i<14;i++){ const o=M(Sph(.15,10),mat(C.purple,1,.2),rnd(-5,-.5),rnd(1.3,3),rnd(-2.5,2.5)); o.userData.ph='out'; G.add(o); cat.push(o); }
    const cl=[]; for(let i=0;i<10;i++){ const o=M(Sph(.15,10),mat(C.green,1,.3),rnd(1,5),rnd(1.3,3),rnd(-2.5,2.5)); o.userData.ph='out'; G.add(o); cl.push(o); }
    L(G,'cations',-4.3,3.3,-1,{size:.6}); L(G,'Cl-',4.4,3.3,-1,{size:.6});
    let v=-70, vt=-70, acc=0, pump=0;
    return {
      go(i){ coneB.visible=i===1; coneY.visible=i===2; chr.forEach(o=>{ const r=i===1?.8:.55; to(o,-2.5+Math.cos(o.userData.a)*r,0,Math.sin(o.userData.a)*r); }); vt=i===2?-95:-70; },
      tick(dt,t){
        if(step===1) vt=(t%0.6<.12)?35:-45;
        v+=(vt-v)*Math.min(1,dt*10);
        const h=Math.max(.2,(v+100)/40); bar.scale.y=h; bar.position.set(5.6,-1.9+h/2,0); bar.material.color.setHex(v>-60?C.orange:v<-80?C.green:C.teal);
        acc+=dt; if(acc>.15){ acc=0; mv.set(`${Math.round(v)} mV${step===1?' (firing)':step===2?' (silenced)':''}`); }
        cat.forEach((o,j)=>{ const u=o.userData; if(u.ph==='out'){ if(step===1){ const tg=new THREE.Vector3(-2.5,1.3,0); o.position.lerp(tg,dt*(.7+j%4*.2)); if(o.position.distanceTo(tg)<.35) u.ph='in'; } }
          else { o.position.y-=dt*3; o.position.x+=(-2.5-o.position.x)*.1; if(o.position.y<-3){ o.position.set(rnd(-5,-.5),rnd(1.5,3),rnd(-2.5,2.5)); u.ph='out'; } } });
        pump+=dt; cl.forEach((o,j)=>{ const u=o.userData; if(u.ph==='out'){ if(step===2){ const tg=new THREE.Vector3(2.5,1.3,0); o.position.lerp(tg,dt*(.6+j%3*.2)); if(o.position.distanceTo(tg)<.4 && pump>.35){ pump=0; o.position.set(2.5,-1.3,0); u.ph='in'; } } }
          else { o.position.y-=dt*1.5; if(o.position.y<-3){ o.position.set(rnd(1,5),rnd(1.5,3),rnd(-2.5,2.5)); u.ph='out'; } } });
      }
    }; }},

{ id:'met', name:'Benign vs malignant: the basal lamina', lec:'Lecture 9', cam:[0,3,14], tgt:[0,-1,0],
  notice:'Yellow sheet = basal lamina. The red cell is the one that turns malignant. The tube below is a blood vessel.',
  trap:'Size does not decide benign vs malignant. Crossing the basal lamina does. Fewer than 1 in 1000 cells that enter the blood survive to form a metastasis, yet metastasis causes about 90% of cancer deaths.',
  steps:[['Normal epithelium','One tidy layer of epithelial cells sits on the basal lamina.'],
   ['Benign tumor','Cells divide too much and pile up, but stay ABOVE the basal lamina, in one local mass.'],
   ['Malignant: break through','One cell loses cell-cell adhesion and breaks through the basal lamina into the tissue below. This is invasion, the defining feature of cancer.'],
   ['Into the blood','The cell enters a blood vessel and travels. Most cells die on this trip.'],
   ['Colonize','A rare survivor sticks to a vessel wall far away, exits, and grows into a new tumor: a metastasis.']],
  build(G){
    const bl=M(Box(12,.12,4),mat(C.yellow,.85),0,-.06,0); G.add(bl); L(G,'basal lamina',-5,-.5,2.3,{size:.75});
    G.add(M(Box(12,3.2,4),mat(C.pink,.12),0,-1.8,0)); L(G,'connective tissue',-4.6,-3.1,2.2,{size:.7});
    const ves=M(Cyl(.85,13,28),mat(C.blood,.3),0,-3.2,0); ves.rotation.z=Math.PI/2; G.add(ves); L(G,'blood vessel',4.6,-4.3,0,{size:.7});
    for(let i=0;i<11;i++) G.add(M(Box(.9,.9,.9),mat(C.soft),-5+i,.5,0));
    const pile=[]; [[-1,1.5],[0,1.5],[1,1.5],[-.5,2.5],[.5,2.5],[0,3.5]].forEach(([x,y])=>{ const o=an(M(Box(.9,.9,.9),mat(C.amber)),0); o.position.set(x,y,0); o.userData.tp.set(x,y,0); sc(o,.001); snap(o); G.add(o); pile.push(o); });
    const hole=M(new THREE.TorusGeometry(.6,.1,10,30),mat(C.orange,1,.4),0,-.06,0); hole.rotation.x=Math.PI/2; hole.visible=false; G.add(hole);
    const bad=an(M(Box(.8,.8,.8),mat(C.red,1,.2),0,1.5,0)); G.add(bad);
    const col=[]; for(let i=0;i<5;i++){ const o=an(M(Box(.55,.55,.55),mat(C.red,1,.15))); const p=[4.6+rnd(-.6,.6),-1.4+rnd(-.4,.4),rnd(-.6,.6)]; o.position.set(...p); o.userData.tp.set(...p); sc(o,.001); snap(o); G.add(o); col.push(o); }
    const note=L(G,'',-3.6,3,0,{size:.8}); note.visible=false;
    let travel=0;
    return {
      go(i){ pile.forEach(o=>sc(o,i>=1?1:.001)); bad.visible=i>=1; hole.visible=i>=2; travel=0;
        if(i<=1) to(bad,0,1.5,0); else if(i===2) to(bad,0,-1.3,0); else if(i===3) to(bad,0,-3.2,0); else to(bad,4.6,-1.4,0);
        col.forEach(o=>sc(o,i===4?1:.001)); note.visible=i>=3; note.set(i===3?'fewer than 1 in 1000 survive the trip':'metastasis: about 90% of cancer deaths'); },
      tick(dt){ if(step===3){ travel=Math.min(travel+dt*.9,1); bad.userData.tp.set(-4+travel*8.6,-3.2,0); } }
    }; }}
];

