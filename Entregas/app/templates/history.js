// Obtener la fecha, pregunta y respuesta de tu API
var fecha = obtenerFechaDesdeAPI();
var pregunta = obtenerPreguntaDesdeAPI();
var respuesta = obtenerRespuestaDesdeAPI();

document.getElementById('date').textContent = fecha;
document.getElementById('question').textContent = pregunta;
document.getElementById('answer').textContent = respuesta;

// Obtener el historial de preguntas y respuestas de tu API
var historial = obtenerHistorialDesdeAPI();
for (var i = 0; i < historial.length; i++) {
  var li = document.createElement("li");
  li.textContent = historial[i];
  document.getElementById('history').appendChild(li);
}