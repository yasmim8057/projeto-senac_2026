document.addEventListener('DOMContentLoaded',funcion()

const token = localStorage.getItem('authtoken');
 
conts links = document.querySelectorAll9('.link-do-cabecalho');

links.forEach(link => {
     
    if (link.geTAttrbute('href') === '.auth.html') {

        if (token) {
            link.setAttribute('href','./form.html');
        }
 

        
    }
}






)
