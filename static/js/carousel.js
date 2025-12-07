// A non-sliding carousel: fades between hero items and applies a slow zoom (Ken Burns) with pause on hover
window.addEventListener('DOMContentLoaded', ()=>{
const items = Array.from(document.querySelectorAll('.hero-item'));
if(!items.length) return;
let idx = 0;
items[idx].classList.add('active');
let timer = setInterval(next, 6000);
function next(){
items[idx].classList.remove('active');
idx = (idx+1) % items.length;
items[idx].classList.add('active');
}
const hero = document.getElementById('hero-container');
hero.addEventListener('mouseenter', ()=> clearInterval(timer));
hero.addEventListener('mouseleave', ()=> timer = setInterval(next, 6000));
});