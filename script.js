(() => {
  const $ = (s, r=document) => r.querySelector(s);
  const $$ = (s, r=document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- Technical HUD ----------
  const overlay = document.createElement('div');
  overlay.className = 'tech-overlay';
  overlay.innerHTML = `
    <div class="tech-grid"></div><div class="scanlines"></div><div class="noise"></div>
    <div class="corner corner-tl"></div><div class="corner corner-tr"></div>
    <div class="corner corner-bl"></div><div class="corner corner-br"></div>
    <div class="hud hud-left"><span>AFK / SYSTEM</span><b>ONLINE</b></div>
    <div class="hud hud-right"><span class="coords">X 000 / Y 000</span><span>2026.09</span></div>
    <div class="scroll-progress"></div><div class="cursor-ring"></div><div class="cursor-dot"></div>
  `;
  document.body.appendChild(overlay);

  // ---------- Boot / loading sequence ----------
  const loader = document.createElement('div');
  loader.className = 'boot-loader';
  loader.innerHTML = `<div class="boot-inner"><div class="boot-mark">AFK<span>.</span></div><div class="boot-line"><i></i></div><div class="boot-meta"><span>INITIALIZING PORTFOLIO</span><span class="boot-percent">00%</span></div></div>`;
  document.body.prepend(loader);

  let p = 0;
  const timer = setInterval(() => {
    p += Math.floor(Math.random() * 13) + 7;
    if (p >= 100) { p = 100; clearInterval(timer); setTimeout(() => loader.classList.add('done'), 380); }
    $('.boot-percent').textContent = String(p).padStart(2,'0') + '%';
    $('.boot-line i').style.width = p + '%';
  }, 85);

  // ---------- Mobile menu ----------
  const menu = $('.menu-btn'), nav = $('nav');
  if (menu && nav) menu.addEventListener('click', () => {
    nav.classList.toggle('open'); menu.classList.toggle('is-open');
  });

  // ---------- Cursor with inertia ----------
  const ring = $('.cursor-ring'), dot = $('.cursor-dot'), coords = $('.coords');
  let mx = innerWidth/2, my = innerHeight/2, rx = mx, ry = my;
  addEventListener('mousemove', e => {
    mx = e.clientX; my = e.clientY;
    if (coords) coords.textContent = `X ${String(Math.round(mx)).padStart(3,'0')} / Y ${String(Math.round(my)).padStart(3,'0')}`;
    if (dot) dot.style.transform = `translate3d(${mx}px,${my}px,0)`;
  }, {passive:true});
  function cursorLoop(){
    rx += (mx-rx)*.09; ry += (my-ry)*.09;
    if (ring) ring.style.transform = `translate3d(${rx}px,${ry}px,0)`;
    requestAnimationFrame(cursorLoop);
  }
  if (!reduce) cursorLoop();

  $$('a,button,.project-card,.skill-card,.discipline-grid a,.contact-grid a').forEach(el => {
    el.addEventListener('mouseenter', () => document.body.classList.add('cursor-active'));
    el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-active'));
  });

  // ---------- Scroll progress ----------
  const progress = $('.scroll-progress');
  const updateProgress = () => {
    const h = document.documentElement.scrollHeight - innerHeight;
    if (progress) progress.style.width = (h > 0 ? scrollY / h * 100 : 0) + '%';
  };
  addEventListener('scroll', updateProgress, {passive:true}); updateProgress();

  // ---------- Deep reveal: blur + lift + clipping ----------
  const revealTargets = $$('section,.project-card,.skill-card,.timeline-large article,.contact-grid a,.work-row,.fact-grid > div,.org,.thesis-big,.tool-placeholder,.detail-visual');
  revealTargets.forEach((el,i) => { el.classList.add('reveal'); el.style.setProperty('--reveal-delay', Math.min(i%6,5)*70+'ms'); });
  if (!reduce && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => entries.forEach(entry => {
      if(entry.isIntersecting){ entry.target.classList.add('is-visible'); io.unobserve(entry.target); }
    }), {threshold:.12, rootMargin:'0px 0px -70px'});
    revealTargets.forEach(el => io.observe(el));
  } else revealTargets.forEach(el => el.classList.add('is-visible'));

  // ---------- High quality 3D tilt ----------
  if (!reduce) {
    $$('.project-card,.portrait-placeholder,.big-placeholder,.tool-placeholder>div').forEach(card => {
      card.addEventListener('mousemove', e => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
        const strength = card.classList.contains('project-card') ? 5 : 2.8;
        card.style.transform = `perspective(1100px) rotateX(${(-y*strength).toFixed(2)}deg) rotateY(${(x*strength).toFixed(2)}deg) translateZ(6px)`;
      });
      card.addEventListener('mouseleave', () => { card.style.transform=''; });
    });
  }

  // ---------- Magnetic buttons / links ----------
  if (!reduce) {
    $$('.btn,.header-cta').forEach(el => {
      el.addEventListener('mousemove', e => {
        const r=el.getBoundingClientRect(), x=e.clientX-(r.left+r.width/2), y=e.clientY-(r.top+r.height/2);
        el.style.transform=`translate(${x*.10}px,${y*.10}px)`;
      });
      el.addEventListener('mouseleave',()=>el.style.transform='');
    });
  }

  // ---------- Mouse-reactive hero parallax ----------
  const hero = $('.hero'), heroWord=$('.hero-word'), portrait=$('.portrait');
  if (hero && !reduce) {
    hero.addEventListener('mousemove', e => {
      const r=hero.getBoundingClientRect(), x=e.clientX/r.width-.5, y=e.clientY/r.height-.5;
      if(heroWord) heroWord.style.margin=`${y*14}px 0 0 ${x*18}px`;
      if(portrait) portrait.style.translate=`${x*7}px ${y*5}px`;
    });
    hero.addEventListener('mouseleave',()=>{if(heroWord)heroWord.style.margin='';if(portrait)portrait.style.translate='';});
  }

  // ---------- Scroll parallax for oversized type ----------
  addEventListener('scroll', () => {
    if (heroWord) heroWord.style.transform = `translate3d(${scrollY*.018}px,${scrollY*.055}px,0)`;
  }, {passive:true});

  // ---------- Smooth anchor scroll ----------
  $$('a[href^="#"]').forEach(a => a.addEventListener('click', e => {
    const id=a.getAttribute('href'); if(!id || id==='#') return;
    const target=$(id); if(target){e.preventDefault(); target.scrollIntoView({behavior:'smooth',block:'start'});}
  }));

  // ---------- Page transition ----------
  const wipe = document.createElement('div'); wipe.className='page-wipe'; document.body.appendChild(wipe);
  $$('a[href$=".html"],a[href="index.html"]').forEach(a => a.addEventListener('click', e => {
    const url = new URL(a.href, location.href);
    if(url.origin !== location.origin || url.pathname === location.pathname || e.metaKey || e.ctrlKey || e.shiftKey) return;
    e.preventDefault(); wipe.classList.add('go'); setTimeout(()=>location.href=url.href,480);
  }));

  // ---------- Small navigation feedback ----------
  $$('nav a').forEach(a=>a.addEventListener('mouseenter',()=>{ if(!reduce) a.animate([{transform:'translateY(0)'},{transform:'translateY(-3px)'},{transform:'translateY(0)'}],{duration:450,easing:'cubic-bezier(.16,1,.3,1)'}); }));
})();
