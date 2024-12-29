
//load

document.addEventListener('DOMContentLoaded', function() {
    
    setTimeout(() => {
        const loader=document.querySelector('.loader-container');
        
        loader.style.opacity = '0';

        setTimeout(() => {
            loader.style.display ='none';
        }, 500);
    }, 1500); 
    //1.5
});
