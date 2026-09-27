from pathlib import Path
p=Path('/tmp/afk-v4/style.css')
s=p.read_text()
# palette replacement
s=s.replace('--bg:#e7e7e3;--paper:#f3f3ef;--ink:#0b0d0e;--muted:#70736f;--line:#b8bbb7;--steel:#697078;--dark:#111518;--white:#f4f4ef;--accent:#c7ff2a;', '--bg:#e3e7e9;--paper:#f3f5f5;--ink:#081016;--muted:#68757d;--line:#b5c0c6;--steel:#71828c;--dark:#081117;--white:#f4f7f8;--accent:#7da8ba;')
# replace lime-specific occurrences
s=s.replace('color:var(--accent);','color:var(--accent);')
s=s.replace('background:var(--accent);','background:#dbe4e8;')
s=s.replace('border-color:#596f1d','border-color:#82939b')
# Remove old V3 layer from marker onward, append fresh layer
marker='/* ==========================================================\n   V3 MOTION / TECHNICAL INTERFACE LAYER'
base=s.split(marker)[0]
layer=r'''/* ==========================================================
   V4 — STEEL / BLUEPRINT MOTION SYSTEM
   ========================================================== */
:root{--electric:#83b6c9;--electric-soft:#aacbd7;--blueprint:#5f8798;--motion:cubic-bezier(.16,1,.3,1)}
html{scroll-behavior:smooth}body{cursor:none;background:var(--bg)}
/* Moving blueprint atmosphere */
.tech-overlay{position:fixed;inset:0;pointer-events:none;z-index:9999;overflow:hidden;opacity:1}
.tech-grid{position:absolute;inset:-10%;opacity:.23;background-image:linear-gradient(rgba(72,94,104,.16) 1px,transparent 1px),linear-gradient(90deg,rgba(72,94,104,.16) 1px,transparent 1px);background-size:72px 72px;transform:perspective(900px) rotateX(62deg) translateY(18%);transform-origin:center bottom;animation:gridDrift 18s linear infinite}
.tech-grid:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,transparent 0%,rgba(131,182,201,.14) 48%,transparent 52%);transform:translateX(-100%);animation:gridScan 7s linear infinite}
.scanlines{position:absolute;inset:0;background:repeating-linear-gradient(to bottom,transparent 0,transparent 7px,rgba(7,17,23,.025) 8px);opacity:.45}
.noise{position:absolute;inset:-50%;opacity:.035;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.6'/%3E%3C/svg%3E");animation:noise .22s steps(2) infinite}
.corner{position:absolute;width:34px;height:34px;border-color:rgba(72,101,113,.48);border-style:solid;animation:cornerPulse 3s ease-in-out infinite}.corner-tl{top:92px;left:24px;border-width:1px 0 0 1px}.corner-tr{top:92px;right:24px;border-width:1px 1px 0 0}.corner-bl{bottom:24px;left:24px;border-width:0 0 1px 1px}.corner-br{bottom:24px;right:24px;border-width:0 1px 1px 0}
.hud{position:absolute;top:91px;font:700 7px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:#66757c;display:flex;gap:12px}.hud-left{left:34px}.hud-left b{color:var(--electric)}.hud-right{right:34px}.scroll-progress{position:absolute;left:0;bottom:0;height:2px;width:0;background:var(--electric);box-shadow:0 0 14px rgba(131,182,201,.65)}
.cursor-ring,.cursor-dot{position:fixed;left:0;top:0;border-radius:50%;transform:translate3d(-100px,-100px,0);pointer-events:none}.cursor-ring{width:38px;height:38px;margin:-19px 0 0 -19px;border:1px solid rgba(71,96,106,.65);transition:width .35s var(--motion),height .35s var(--motion),margin .35s var(--motion),border-color .35s,background .35s}.cursor-dot{width:5px;height:5px;margin:-2.5px 0 0 -2.5px;background:var(--ink);box-shadow:0 0 10px rgba(131,182,201,.65)}.cursor-active .cursor-ring{width:66px;height:66px;margin:-33px 0 0 -33px;border-color:var(--electric);background:rgba(131,182,201,.06)}
/* Boot sequence */
.boot-loader{position:fixed;inset:0;background:#071016;color:#eef5f7;z-index:10000;display:grid;place-items:center;transition:opacity .8s var(--motion),visibility .8s}.boot-loader.done{opacity:0;visibility:hidden}.boot-inner{width:min(520px,72vw);position:relative}.boot-inner:before{content:"";position:absolute;left:-32px;top:-32px;width:18px;height:18px;border-left:1px solid var(--electric);border-top:1px solid var(--electric);animation:bootCorner 1.2s ease-in-out infinite alternate}.boot-mark{font:900 82px/.8 var(--display);letter-spacing:-.06em;margin-bottom:36px;animation:bootMark 1.1s var(--motion) both}.boot-mark span{color:var(--electric)}.boot-line{height:1px;background:#2c3b42;overflow:hidden;position:relative}.boot-line i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--electric),#eaf7fb);box-shadow:0 0 18px rgba(131,182,201,.75);transition:width .1s}.boot-meta{display:flex;justify-content:space-between;margin-top:12px;font-size:7px;letter-spacing:.16em;color:#87979e}.boot-meta:after{content:"BIM / QS / DRAFTING / ESTIMATION";position:absolute;left:0;top:calc(100% + 30px);font-size:6px;letter-spacing:.2em;color:#52666f}
/* Global page reveal */
.reveal{opacity:0;transform:translate3d(0,70px,0) scale(.985);filter:blur(5px);clip-path:inset(10% 0 0 0);transition:opacity 1s var(--motion) var(--reveal-delay),transform 1.05s var(--motion) var(--reveal-delay),filter 1s var(--motion) var(--reveal-delay),clip-path 1.1s var(--motion) var(--reveal-delay)}.reveal.is-visible{opacity:1;transform:none;filter:none;clip-path:inset(0);}
/* Hero entrance */
.hero .kicker,.hero h1,.hero .lead,.hero .actions,.portrait,.hero-top,.ticker{animation:heroIn 1.05s var(--motion) both}.hero-top{animation-delay:.85s}.hero .kicker{animation-delay:1s}.hero h1{animation-delay:1.08s}.hero .lead{animation-delay:1.18s}.hero .actions{animation-delay:1.28s}.portrait{animation-delay:1.12s}.ticker{animation-delay:1.45s}.hero h1{perspective:800px}.hero h1 span{display:inline-block;animation:nameGlitch 7s ease-in-out 2.2s infinite}.hero-word{animation:wordFloat 10s ease-in-out infinite alternate;transform-origin:center}
/* Text / card interactions */
.project-card,.skill-card,.work-row,.contact-grid a,.discipline-grid a{will-change:transform}.project-card{transition:transform .55s var(--motion),filter .55s,opacity .8s}.project-card:hover{filter:contrast(1.04)}.project-card .visual{transition:transform .7s var(--motion),box-shadow .7s var(--motion)}.project-card:hover .visual{transform:translateY(-10px) scale(.992);box-shadow:0 22px 50px rgba(8,16,22,.13)}
.visual{isolation:isolate}.visual:before{transition:transform .9s var(--motion),inset .9s var(--motion),border-color .4s}.visual:after{transition:transform .9s var(--motion),box-shadow .6s}.project-card:hover .visual:before{transform:rotate(0) scale(.96);inset:8%;border-color:rgba(255,255,255,.85)}.project-card:hover .visual:after{transform:rotate(0) scale(1.12);box-shadow:0 0 30px rgba(131,182,201,.2)}.visual small{transition:letter-spacing .4s,color .4s}.project-card:hover .visual small{letter-spacing:.28em;color:#fff}
.skill-card{position:relative;overflow:hidden;transition:padding .55s var(--motion),background .45s,transform .45s var(--motion)}.skill-card:after{content:"";position:absolute;left:0;top:0;height:1px;width:0;background:var(--electric);box-shadow:0 0 12px rgba(131,182,201,.7);transition:width .7s var(--motion)}.skill-card:hover{padding-left:22px;background:linear-gradient(90deg,rgba(131,182,201,.08),transparent);transform:translateX(5px)}.skill-card:hover:after{width:100%}.skill-card h3{transition:letter-spacing .5s var(--motion),transform .5s var(--motion)}.skill-card:hover h3{letter-spacing:.015em;transform:translateX(3px)}
.discipline-grid a{position:relative;overflow:hidden}.discipline-grid a:before{content:"";position:absolute;left:0;bottom:0;width:100%;height:2px;background:var(--electric);transform:scaleX(0);transform-origin:left;transition:transform .7s var(--motion)}.discipline-grid a:hover:before{transform:scaleX(1)}
/* Project / tool visual scan */
.big-placeholder,.tool-placeholder>div{overflow:hidden}.big-placeholder:after,.tool-placeholder>div:after,.portrait-placeholder:after{content:"";position:absolute;left:0;top:-15%;width:100%;height:2px;background:linear-gradient(90deg,transparent,var(--electric),transparent);box-shadow:0 0 18px rgba(131,182,201,.55);animation:scanVertical 4.2s ease-in-out infinite}.big-placeholder:before,.tool-placeholder>div:before{transition:inset .8s var(--motion),transform .8s var(--motion),border-color .5s}.big-placeholder:hover:before,.tool-placeholder>div:hover:before{inset:18px;transform:scale(.985);border-color:rgba(131,182,201,.55)}
/* Buttons become mechanical / magnetic */
.btn{position:relative;overflow:hidden;transition:transform .4s var(--motion),background .35s,box-shadow .35s}.btn:before{content:"";position:absolute;inset:0;background:linear-gradient(100deg,transparent 25%,rgba(255,255,255,.18) 48%,transparent 72%);transform:translateX(-120%);transition:transform .7s var(--motion)}.btn:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(8,16,22,.18)}.btn:hover:before{transform:translateX(120%)}.under{transition:letter-spacing .45s var(--motion)}.under:hover{letter-spacing:.2em}
/* Navigation */
nav a{transition:color .3s,letter-spacing .4s}.site-header:after{content:"";position:absolute;left:0;bottom:-1px;height:1px;width:100%;background:linear-gradient(90deg,transparent,var(--electric),transparent);transform:scaleX(.15);animation:navLine 4s ease-in-out infinite}
/* Floating geometry */
.hero:before{content:"";position:absolute;width:280px;height:280px;border:1px solid rgba(79,109,121,.18);border-radius:50%;right:15%;top:26%;animation:orbit 16s linear infinite}.hero:after{content:"01 / 08 — TECHNICAL PORTFOLIO";position:absolute;right:5vw;top:50%;writing-mode:vertical-rl;font-size:7px;letter-spacing:.18em;color:#66757c;opacity:.72}
.page-hero:after,.project-detail-hero:after,.tool-hero:after{content:"ENGINEERING / VISUAL SYSTEM";position:absolute;right:5vw;font-size:7px;letter-spacing:.18em;color:#66757c;opacity:.6;animation:microBlink 3s ease-in-out infinite}.page-hero,.project-detail-hero,.tool-hero{position:relative}
.section-head h2,.hero h1,.page-hero h1,.project-detail-hero h1,.tool-hero h1,.contact-page h1{transition:letter-spacing .7s var(--motion),transform .7s var(--motion)}.section-head h2:hover,.hero h1:hover,.page-hero h1:hover,.project-detail-hero h1:hover,.tool-hero h1:hover,.contact-page h1:hover{letter-spacing:-.075em;transform:translateX(3px)}
/* Contact no longer lime */
.contact-page{background:#dbe4e8;color:var(--ink)}.contact-grid{border-color:#8b9ca4}.contact-grid a{border-color:#8b9ca4;transition:padding .5s var(--motion),background .4s}.contact-grid a:hover{padding-left:15px;background:rgba(255,255,255,.25)}
/* motion keyframes */
@keyframes gridDrift{from{transform:perspective(900px) rotateX(62deg) translate3d(0,18%,0)}to{transform:perspective(900px) rotateX(62deg) translate3d(-72px,22%,0)}}
@keyframes gridScan{to{transform:translateX(100%)}}
@keyframes noise{0%{transform:translate(0,0)}25%{transform:translate(2%,-1%)}50%{transform:translate(-1%,2%)}75%{transform:translate(1%,1%)}100%{transform:translate(0,0)}}
@keyframes cornerPulse{0%,100%{opacity:.4;transform:scale(1)}50%{opacity:.95;transform:scale(1.05)}}
@keyframes bootMark{from{opacity:0;transform:translateY(20px);filter:blur(8px);letter-spacing:.1em}to{opacity:1;transform:none;filter:none;letter-spacing:-.06em}}
@keyframes bootCorner{from{transform:translate(0,0)}to{transform:translate(8px,8px)}}
@keyframes heroIn{from{opacity:0;transform:translateY(55px);filter:blur(9px)}to{opacity:1;transform:none;filter:none}}
@keyframes wordFloat{from{transform:translate3d(-1%,0,0) scale(1)}to{transform:translate3d(2%,2%,0) scale(1.025)}}
@keyframes nameGlitch{0%,92%,100%{transform:none;filter:none}94%{transform:translateX(3px);filter:blur(.5px)}96%{transform:translateX(-2px);filter:none}}
@keyframes scanVertical{0%,18%{top:-15%;opacity:0}25%{opacity:1}72%{opacity:1}82%,100%{top:115%;opacity:0}}
@keyframes navLine{0%,100%{transform:scaleX(.12)}50%{transform:scaleX(.55)}}
@keyframes orbit{from{transform:rotate(0deg) translateX(8px) rotate(0deg)}to{transform:rotate(360deg) translateX(8px) rotate(-360deg)}}
@keyframes microBlink{0%,100%{opacity:.35}50%{opacity:.8}}
@keyframes wipe{0%{transform:translateY(100%)}100%{transform:translateY(0)}}
.page-wipe{position:fixed;inset:0;background:#071016;transform:translateY(100%);z-index:10001;pointer-events:none}.page-wipe.go{animation:wipe .55s cubic-bezier(.76,0,.24,1) forwards}
/* Mobile */
@media(max-width:850px){body{cursor:auto}.cursor-ring,.cursor-dot{display:none}.hud{display:none}.corner{display:none}.hero:after,.page-hero:after,.project-detail-hero:after,.tool-hero:after{display:none}.tech-grid{background-size:48px 48px;opacity:.14;transform:perspective(700px) rotateX(58deg) translateY(15%)}.site-header{z-index:10002}nav.open{display:flex;position:absolute;left:0;right:0;top:65px;background:rgba(227,231,233,.98);padding:20px 5vw;flex-direction:column;gap:5px;border-bottom:1px solid var(--line)}nav.open a{padding:12px 0}.menu-btn.is-open{transform:rotate(90deg)}.boot-mark{font-size:58px}.hero:before{width:160px;height:160px;right:-40px;top:35%}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.001ms!important;transition-duration:.001ms!important;scroll-behavior:auto!important}.reveal{opacity:1;transform:none;filter:none;clip-path:none}.tech-overlay{display:none}body{cursor:auto}}
'''
p.write_text(base+layer)
