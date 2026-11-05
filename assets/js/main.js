(()=>{const d=document,q=s=>[...d.querySelectorAll(s)],h=d.querySelector('.hd'),rm=matchMedia('(prefers-reduced-motion:reduce)').matches,D=window.I18N,L=['az','en','ru'];
let ly=0;const pb=d.querySelector('.pgb'),sc=()=>{const y=scrollY;h.classList.toggle('sc',y>40);h.classList.toggle('hide',y>600&&y>ly&&!d.body.classList.contains('mo'));ly=y;pb.style.transform=`scaleX(${scrollY/Math.max(1,d.documentElement.scrollHeight-innerHeight)})`};addEventListener('scroll',sc,{passive:true});sc();
/* counters + line reveals */
const run=el=>{const t=el.dataset.since?new Date().getFullYear()-+el.dataset.since:+el.dataset.n,s=el.dataset.s||'';if(rm){el.textContent=t+s;return}let st;const f=ts=>{st=st||ts;const p=Math.min((ts-st)/1800,1);el.textContent=Math.round(t*(1-Math.pow(1-p,4)))+s;p<1&&requestAnimationFrame(f)};requestAnimationFrame(f)};
const io=new IntersectionObserver(e=>e.forEach(x=>{if(!x.isIntersecting)return;x.target.matches('b')?run(x.target):x.target.classList.add('in');io.unobserve(x.target)}),{threshold:.4});
q('.stats b').forEach(e=>io.observe(e));q('.fe,.sv').forEach(e=>io.observe(e));
/* accordion */
q('.pr button').forEach(b=>b.addEventListener('click',()=>{const li=b.parentElement,open=!li.classList.contains('o');q('.pr').forEach(p=>{p.classList.remove('o');p.querySelector('button').setAttribute('aria-expanded','false')});if(open){li.classList.add('o');b.setAttribute('aria-expanded','true');const k=[...li.parentNode.children].indexOf(li);q('.pimg img').forEach((m,i)=>m.classList.toggle('on',i===k))}}));
/* mobile menu */
const bg=d.querySelector('.bg'),tg=v=>{d.body.classList.toggle('mo',v);bg.setAttribute('aria-expanded',v);d.body.style.overflow=v?'hidden':''};
bg.addEventListener('click',()=>tg(!d.body.classList.contains('mo')));q('.mm a').forEach(a=>a.addEventListener('click',()=>tg(false)));addEventListener('keydown',e=>e.key==='Escape'&&tg(false));
/* hero pointer parallax */
const hero=d.querySelector('.hero'),rt=d.querySelector('.rt');
if(!rm&&matchMedia('(hover:hover)').matches)hero.addEventListener('pointermove',e=>{const r=hero.getBoundingClientRect();rt.style.setProperty('--px',((e.clientX-r.left)/r.width-.5).toFixed(3));rt.style.setProperty('--py',((e.clientY-r.top)/r.height-.5).toFixed(3))});
if(rm&&rt.pauseAnimations)rt.pauseAnimations();
/* in-place language switch */
const lg=d.querySelector('.lg'),meta=n=>d.querySelector(n);let cur='az',st=0;
const apply=l=>{q('[data-t]').forEach(e=>{const v=D[l][e.dataset.t];if(v!=null)e.textContent=v});d.documentElement.lang=l;meta('meta[name=description]').content=D[l].desc;meta('meta[property="og:title"]').content=D[l].title;meta('meta[property="og:description"]').content=D[l].desc;lg.style.setProperty('--i',L.indexOf(l));q('.lg button').forEach(b=>b.classList.toggle('on',b.dataset.l===l));try{localStorage.setItem('lang',l)}catch(e){}cur=l;st&&ScrollTrigger.refresh()};
const go=l=>{if(l===cur)return;lg.style.setProperty('--i',L.indexOf(l));history.replaceState(null,'',(l==='az'?location.pathname:'?lang='+l)+location.hash);
 if(rm){apply(l);return}
 const els=q('[data-t]').filter(e=>e.tagName!=='TITLE'&&e.style.opacity!=='0'&&D[l][e.dataset.t]!=null),out=els.map((e,i)=>e.animate({opacity:[1,0]},{duration:160,delay:i*6,fill:'forwards'}));
 Promise.all(out.map(x=>x.finished)).then(()=>{apply(l);els.forEach((e,i)=>{e.animate({opacity:[0,1]},{duration:420,delay:i*8,easing:'cubic-bezier(.2,.7,.2,1)',fill:'backwards'});out[i].cancel()})}).catch(()=>apply(l))};
q('.lg button').forEach(b=>b.addEventListener('click',()=>go(b.dataset.l)));
let sv;try{sv=localStorage.getItem('lang')}catch(e){}
const nl=(navigator.language||'az').slice(0,2),init=new URLSearchParams(location.search).get('lang')||sv||(L.includes(nl)?nl:'az');
if(L.includes(init)&&init!=='az')apply(init);
/* cookie consent: analytics loads only after accept */
const ck=d.querySelector('.ck'),gt=()=>{if(window.gtag)return;const s=d.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id=G-Y4Q75NFZE0';d.head.appendChild(s);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config','G-Y4Q75NFZE0')};
let c;try{c=localStorage.getItem('ck')}catch(e){}
if(c==='y')gt();else if(!c)setTimeout(()=>ck.classList.add('show'),2000);
ck.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;try{localStorage.setItem('ck',b.dataset.c)}catch(e){}ck.classList.remove('show');b.dataset.c==='y'&&gt()});
/* GSAP scroll animations */
if(window.gsap&&window.ScrollTrigger&&!rm){const g=gsap,ST=ScrollTrigger;g.registerPlugin(ST);st=1;
const hs={trigger:'.hero',start:'top top',end:'bottom top',scrub:true};
g.to('.ht',{yPercent:-14,opacity:.1,ease:'none',scrollTrigger:hs});g.to('.rt',{'--sy':'-90px',ease:'none',scrollTrigger:hs});g.to('.hbg',{yPercent:14,ease:'none',scrollTrigger:hs});
g.to('.mt',{xPercent:-38,ease:'none',scrollTrigger:{trigger:'.mq',start:'top bottom',end:'bottom top',scrub:.8}});
q('.sec h2,.cta h2').forEach(el=>g.from(el,{y:70,opacity:0,clipPath:'inset(0 0 100% 0)',duration:1.2,ease:'power4.out',clearProps:'clipPath,transform,opacity',scrollTrigger:{trigger:el,start:'top 88%',once:true}}));
const rv='.lead,.mu,.fe,.pr,.sv,.cta p,.cc>*,.sg>div,.fg2>div';g.set(rv,{y:50,opacity:0});
ST.batch(rv,{start:'top 92%',once:true,onEnter:els=>g.to(els,{y:0,opacity:1,duration:1,stagger:.12,ease:'power3.out',clearProps:'transform,opacity',overwrite:true})});
if(matchMedia('(hover:hover)').matches)q('.btn.pr1,.btn.sm,.btn.gh').forEach(b=>{b.style.transition='background .35s,color .35s,border-color .35s';const x=g.quickTo(b,'x',{duration:.5,ease:'power3'}),y=g.quickTo(b,'y',{duration:.5,ease:'power3'});b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();x((e.clientX-r.left-r.width/2)*.25);y((e.clientY-r.top-r.height/2)*.35)});b.addEventListener('pointerleave',()=>{x(0);y(0)})});
addEventListener('load',()=>{q('.ph.ok,.pimg.ok').forEach(f=>{g.from(f,{clipPath:'inset(0 100% 0 0)',duration:1.4,ease:'power4.inOut',clearProps:'clipPath',scrollTrigger:{trigger:f,start:'top 88%',once:true}});if(f.classList.contains('ph'))g.fromTo(f.querySelector('img'),{yPercent:-6,scale:1.12},{yPercent:6,scale:1,ease:'none',scrollTrigger:{trigger:f,start:'top bottom',end:'bottom top',scrub:true}})});
const gt=d.querySelector('.gt');if(gt&&d.querySelector('.gal.ok'))g.to(gt,{x:()=>-(gt.scrollWidth-innerWidth+80),ease:'none',scrollTrigger:{trigger:'.gal',start:'top bottom',end:'bottom top',scrub:.7,invalidateOnRefresh:true}});ST.refresh()});
d.fonts&&d.fonts.ready.then(()=>ST.refresh())}
})();
