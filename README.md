# kilian99.github.io
github pages
# CR7 es el mejor

# belligol

---
layout: default
title: Inicio
---

<h1>Bienvenido a mi sitio web</h1>

<p>Este es el contenido de la página de inicio.</p>

<!-- Ejemplo de acceso a datos JSON -->
<h2>Tabla de Datos</h2>
<table id="tabla-datos">
    <!-- Los datos se cargarán aquí mediante JavaScript -->
</table>

<script>
    fetch('/_data/datos.json')
        .then(response => response.json())
        .then(data => {
            const tabla = document.getElementById('tabla-datos');
            tabla.innerHTML = `
                <tr>
                    <th>Nombre</th>
                    <th>Edad</th>
                </tr>
                ${data.map(item => `
                    <tr>
                        <td>${item.nombre}</td>
                        <td>${item.edad}</td>
                    </tr>
                `).join('')}
            `;
        })
        .catch(error => console.error('Error al cargar los datos:', error));
</script>
