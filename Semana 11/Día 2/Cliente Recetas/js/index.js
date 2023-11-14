

async function cargarRecetas(elemento){
    const config = {
        method: 'GET'
    };

    const response = await fetch('http://127.0.0.1:5000/api/recetas', config);
    const datos = await response.json();
    const tBody = document.querySelector('.recetas');

    for(let i = 0; i < datos.length; i ++){
        tBody.innerHTML += `
            <tr>
                <td> ${datos[i].nombre} </td>
                <td> ${datos[i].menos_30} </td>
                <td> ${datos[i].instrucciones} </td>
                <td> ${datos[i].descripcion} </td>
            </tr>                    
        `
    }
}

async function agregarReceta(evento){
    evento.preventDefault();

    const nuevaReceta = {
        "descripcion": document.querySelector('#descripcion').value,
        "fecha_coccion": document.querySelector('#fecha_coccion').value,
        "id_usuario": 1,
        "instrucciones": document.querySelector('#instrucciones').value,
        "menos_30": 1,
        "nombre": document.querySelector('#nombre').value
    }

    const config = {
        method: 'POST',
        body: JSON.stringify(nuevaReceta),
        headers: {
            'Content-type': 'application/json'
        }
    }

    const response = await fetch('http://127.0.0.1:5000/api/nueva/receta', config);
    const datos = await response.json();
    console.log(datos);

}