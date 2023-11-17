var i;
const hint=document.querySelector('.hint');
const exit=document.querySelector('.exit');
const notification=document.querySelector('.warn')
exit.style.cursor='pointer';
exit.onclick=()=>{
    hint.classList.add('hidden');
}
notification.onclick=()=>{
    console.log(hint)
    if(hint.classList.contains('hidden')){
        hint.classList.remove('hidden')
    }
    else{
        hint.classList.add('hidden')
    }
}
