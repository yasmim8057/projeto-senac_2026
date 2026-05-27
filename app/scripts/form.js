import { openStoryModal } from "./modal.js"

const form = document.getElementById('post-form');

form.addEventListener('submit', function(event) {

        event.preventDefault();

        const form_data = new FormData(event.target)

        const autor = form_data.get('autor')
        const titulo = form_data.get('titulo')
        const email = form_data.get('email')
        const historia = form_data.get('historia')

        if (!autor || !historia) { //verificação de campos vazios
                alert("Os campos `Autor` e `História` são obrigatórios!")
                return
        }

        const article = document.createElement('article');
        article.className = "artigo";

        article.innerHTML =
                `<h3>${titulo}</h3>
                <p><strong> Autor: ${autor} </strong></p>
                <p><small> Email: ${email} </small></p>
                <p>${historia.replace('/\n/g', '<br />')}</p>
                <hr />`;

        article.addEventListener('click', function() {
                openStoryModal(titulo, autor, historia);
        })

        document.getElementById('historias').appendChild(article)

        event.target.reset()
})