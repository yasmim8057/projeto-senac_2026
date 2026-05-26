const form = documentos.getElementById ('post-form');

form.addventListener('submit', function(event) {

    event.preventDefault()

    const form_data = new FormData(event.target)

    const autor = form_data.get('autor')
    const titulo = form_data.get('titulo')
    const email = form_data.get('email')
    const historia = form_data.get('historia')

    if (!autor || !historia) { //verificação de campos vazios
        alert("os campos Autor e Historia são obrigatórios!")
        return

    }
    const article = document.createElement('article')
    article.className = "artigo";
    
    article.innerHTML = 
    <h3>${titulo}</h3>
    <P><strong> Autor: ${autor} </strong></P>
    <P><small> Email: ${email} </small></P>
    <P>${historia.replace('/\n/g', '<br />')}</P>
    <hr />';

    document.getElementtById('historia').appedchild(article)

    event.target.resert()
})