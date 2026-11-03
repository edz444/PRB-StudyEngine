(function(){
  var lb = document.getElementById('lb'), lbImg = lb.querySelector('img');
  function close(){ lb.hidden = true; lbImg.src = ''; }
  document.querySelectorAll('.slide .zoom').forEach(function(b){
    b.addEventListener('click', function(){ var i = b.querySelector('img'); lbImg.src = i.src; lbImg.alt = i.alt; lb.hidden = false; lb.querySelector('.lb-close').focus(); });
  });
  lb.addEventListener('click', close);
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && !lb.hidden) close(); });
  document.querySelectorAll('.labbtn').forEach(function(b){
    b.addEventListener('click', function(){
      var box = b.nextElementSibling, open = b.getAttribute('aria-expanded') === 'true';
      if(open){ b.setAttribute('aria-expanded','false'); box.hidden = true; box.innerHTML = ''; return; }
      b.setAttribute('aria-expanded','true'); box.hidden = false;
      var f = document.createElement('iframe'); f.title = 'Pathway Lab'; f.loading = 'eager';
      f.src = 'lab.html#' + b.getAttribute('data-lab');
      box.appendChild(f);
      var fit = function(){ try{ var d = f.contentDocument; if(!d || !d.body) return;
          var h = Math.max(d.documentElement.scrollHeight, d.body.scrollHeight); if(h > 200) f.style.height = (h + 4) + 'px'; }catch(e){} };
      f.addEventListener('load', function(){ fit(); try{ if(window.ResizeObserver){ new ResizeObserver(fit).observe(f.contentDocument.body); } }catch(e){} setTimeout(fit, 400); setTimeout(fit, 1500); });
      setTimeout(function(){ b.scrollIntoView({block:'start', behavior:'smooth'}); }, 50);
    });
  });
  var links = Array.prototype.slice.call(document.querySelectorAll('.navin a'));
  var secs = links.map(function(a){ return document.getElementById(a.getAttribute('href').slice(1)); });
  function spy(){
    var y = window.scrollY + 90, cur = 0;
    secs.forEach(function(s, i){ if(s && s.offsetTop <= y) cur = i; });
    links.forEach(function(a, i){ a.classList.toggle('on', i === cur); });
    var on = links[cur]; if(on && on.scrollIntoView && on.parentNode.scrollWidth > on.parentNode.clientWidth){
      var p = on.parentNode, l = on.offsetLeft - p.clientWidth/2 + on.clientWidth/2; p.scrollLeft = l; }
  }
  var rail = Array.prototype.slice.call(document.querySelectorAll('.rail a'));
  var vp = document.querySelector('.vprog'), vpLabel = vp && vp.querySelector('b'), hideT;
  function prog(){
    var top = window.scrollY + 90, vh = window.innerHeight, docH = document.documentElement.scrollHeight, cur = 0;
    secs.forEach(function(s, i){ if(s && s.offsetTop <= top) cur = i; });
    secs.forEach(function(s, i){
      if(!s) return;
      var start = s.offsetTop, end = (secs[i+1] ? secs[i+1].offsetTop : docH);
      var span = Math.max(1, end - start - vh + 90);
      var p = Math.min(1, Math.max(0, (top - start) / span));
      if(window.scrollY + vh >= docH - 2 && i === secs.length - 1) p = 1;
      var pct = Math.round(p * 100) + '%';
      links[i].style.setProperty('--p', pct);
      var r = rail[i]; if(r){ r.style.setProperty('--p', pct); r.querySelector('.rp').textContent = pct;
        r.classList.toggle('on', i === cur); r.classList.toggle('done', p >= 0.99); }
      if(i === cur && vp){ vp.style.setProperty('--p', pct); vpLabel.textContent = links[i].textContent + ' ' + pct; }
    });
  }
  window.addEventListener('scroll', function(){ window.requestAnimationFrame(function(){ spy(); prog(); });
    if(vp){ vp.classList.add('show'); clearTimeout(hideT); hideT = setTimeout(function(){ vp.classList.remove('show'); }, 1400); } }, {passive:true});
  window.addEventListener('resize', prog);
  window.addEventListener('load', prog);
  spy(); prog();
})();
