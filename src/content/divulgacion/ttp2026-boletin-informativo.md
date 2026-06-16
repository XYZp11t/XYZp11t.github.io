---
titulo: "Teacher Training Programme (TTP) 2026 en Morelia"
descripcion: "Morelia fue sede del Teacher Training Programme (TTP) 2026 de la Unión Astronómica Internacional"
autor: "Dr. Mario Rodríguez Martínez"
fecha: 2026-03-24
imagen: "/TTP2026/IAU_SP.png"
etiquetas: ["astronomía", "eventos", "entrenamiento"]
destacado: true
galeria:
  ruta: "/TTP2026/imagenes"
  titulo: "Galería del Evento TTP 2026"
---

<style>
.ttp-logos {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin: 0.2rem 0 1.5rem 0; /* Margen superior reducido */
  padding: 0.5em 0.5rem;
  background: #f8f6f3;
  border-radius: 8px;
}
.ttp-logos a {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 0 0 auto;
  transition: transform 0.2s ease, opacity 0.2s ease;
}
.ttp-logos a:hover {
  transform: scale(1.08);
  opacity: 0.85;
}
.ttp-logos img {
  height: 80px;
  width: auto;
  max-width: 110px;
  object-fit: contain;
  border-radius: 0 !important;
  box-shadow: none !important;
}
.ttp-title-header {
  margin-bottom: 0.1rem; /* Reducción de espacio con los logos */
}
.ttp-table-wrapper {
  overflow-x: auto;
  margin: 1.5rem 0;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.10);
}
.ttp-table {
  width: 100%;
  min-width: 700px;
  border-collapse: collapse;
  font-size: 0.88rem;
  line-height: 1.45;
}
.ttp-table th,
.ttp-table td {
  border: 1px solid #c8c4be;
  padding: 0.55rem 0.7rem;
  vertical-align: top;
}
.ttp-title-row td {
  background: #1a3c1a;
  color: #fff;
  text-align: center;
  font-weight: 700;
  font-size: 0.95rem;
  padding: 0.7rem;
  letter-spacing: 0.02em;
}
.ttp-table th {
  text-align: center;
  font-weight: 700;
  font-size: 0.9rem;
  color: #fff;
}
.th-hora { background: #3e3e3e; }
.th-jue { background: #2e7d32; }
.th-vie { background: #1565c0; }
.th-sab { background: #e65100; }
.td-hora {
  background: #eeece8;
  text-align: center;
  font-weight: 700;
  font-size: 0.82rem;
  white-space: nowrap;
  color: #333;
}
.td-jue { background: #c8e6c9; }
.td-vie { background: #bbdefb; }
.td-sab { background: #fff3e0; }
.td-break {
  text-align: center;
  font-style: italic;
  font-weight: 600;
  color: #555;
}
.td-inaug {
  background: #ff8f00 !important;
  color: #fff;
  font-weight: 700;
}
.td-llegada {
  text-align: center;
  vertical-align: middle;
  font-weight: 700;
  font-size: 1rem;
}
.td-regreso {
  text-align: center;
  vertical-align: middle;
  font-weight: 600;
  font-style: italic;
}
.td-empty {
  background: #f5f3f0;
}
@media (max-width: 768px) {
  .ttp-logos {
    flex-wrap: wrap;
    gap: 0.75rem;
    padding: 1rem;
  }
  .ttp-logos img {
    height: 45px;
    max-width: 90px;
  }
}

/* ============================================================
   Carrusel de entrevistas (lista de reproducción TTP 2026)
   ============================================================ */
.ttp-videos-section {
  margin: 2rem auto 1.25rem;
  max-width: 640px;
}
.ttp-videos-intro {
  color: #444;
  font-size: 0.95rem;
  line-height: 1.55;
  margin: 0 0 1rem 0;
}
.ttp-videos-intro a {
  color: #1565c0;
  text-decoration: underline;
  text-underline-offset: 2px;
  font-weight: 600;
}
.ttp-videos-intro a:hover { color: #0d47a1; }

.ttp-carousel {
  position: relative;
}
.ttp-carousel-viewport {
  position: relative;
  overflow: hidden;
  border-radius: 10px;
  background: #1a1a1a;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.12);
  aspect-ratio: 16 / 9;
}
.ttp-carousel-track {
  display: flex;
  width: 100%;
  height: 100%;
  transition: transform 0.5s ease;
}
.ttp-carousel-slide {
  flex: 0 0 100%;
  position: relative;
  height: 100%;
}
.ttp-thumb {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
  border: 0;
  padding: 0;
  margin: 0;
  cursor: pointer;
  background: #1a1a1a;
  overflow: hidden;
}
.ttp-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  border-radius: 0 !important;
  box-shadow: none !important;
  margin: 0 !important;
}
.ttp-thumb::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(0,0,0,0) 50%, rgba(0,0,0,0.35) 100%);
  pointer-events: none;
}
.ttp-thumb:hover .ttp-play-icon,
.ttp-thumb:focus-visible .ttp-play-icon {
  transform: translate(-50%, -50%) scale(1.1);
}
.ttp-thumb:focus-visible {
  outline: 3px solid #f57f17;
  outline-offset: -3px;
}
.ttp-play-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 60px;
  height: auto;
  filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.55));
  transition: transform 0.25s ease;
  pointer-events: none;
}
.ttp-carousel-slide iframe {
  width: 100%;
  height: 100%;
  border: 0;
  display: block;
}

.ttp-carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 0;
  background: rgba(255, 255, 255, 0.92);
  color: #1a1a1a;
  font-size: 1.4rem;
  line-height: 1;
  font-weight: 700;
  cursor: pointer;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  transition: background 0.2s ease, transform 0.2s ease;
}
.ttp-carousel-btn:hover {
  background: #fff;
  transform: translateY(-50%) scale(1.08);
}
.ttp-carousel-btn:focus-visible {
  outline: 3px solid #f57f17;
  outline-offset: 2px;
}
.ttp-carousel-btn.ttp-prev { left: 8px; }
.ttp-carousel-btn.ttp-next { right: 8px; }

.ttp-carousel-dots {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: 0.8rem;
  padding: 0;
}
.ttp-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  border: 0;
  padding: 0;
  background: #c8c4be;
  cursor: pointer;
  transition: background 0.2s ease, transform 0.2s ease;
}
.ttp-dot:hover { background: #888; }
.ttp-dot:focus-visible {
  outline: 2px solid #f57f17;
  outline-offset: 2px;
}
.ttp-dot[aria-selected="true"] {
  background: #1a3c1a;
  transform: scale(1.25);
}

.ttp-carousel-counter {
  text-align: center;
  font-size: 0.78rem;
  color: #6a6a6a;
  margin-top: 0.35rem;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.03em;
}

@media (max-width: 480px) {
  .ttp-carousel-btn { width: 34px; height: 34px; font-size: 1.2rem; }
  .ttp-play-icon { width: 48px; }
}

@media (prefers-reduced-motion: reduce) {
  .ttp-carousel-track,
  .ttp-play-icon,
  .ttp-carousel-btn,
  .ttp-dot { transition: none !important; }
}
</style>


<h3 class="ttp-title-header"><strong>Morelia fue sede del Teacher Training Programme (TTP) 2026 de la Unión Astronómica Internacional</strong></h3>

<div class="ttp-logos">
  <a href="https://www.enesmorelia.unam.mx/" target="_blank" rel="noopener" title="ENES Morelia – UNAM">
    <img src="/TTP2026/UNAM-ENES.png" alt="ENES Morelia – UNAM">
  </a>
  <a href="https://astro4edu.org/" target="_blank" rel="noopener" title="OAE – IAU">
    <img src="/TTP2026/OAE.png" alt="OAE – IAU">
  </a>
  <a href="https://www.irya.unam.mx/web/es/" target="_blank" rel="noopener" title="IRyA – UNAM">
    <img src="/TTP2026/IRyA.png" alt="IRyA – UNAM">
  </a>
  <a href="https://igum.geofisica.unam.mx/" target="_blank" rel="noopener" title="IGUM – UNAM">
    <img src="/TTP2026/IGUM.png" alt="IGUM – UNAM">
  </a>
  <a href="https://www.inaoep.mx/" target="_blank" rel="noopener" title="INAOE">
    <img src="/TTP2026/INAOE.png" alt="INAOE">
  </a>
  <a href="https://icti.michoacan.gob.mx/" target="_blank" rel="noopener" title="ICTI Michoacán">
    <img src="/TTP2026/ICTI.png" alt="ICTI Michoacán">
  </a>
  <a href="https://www.gob.mx/presidencia/documentos/plan-michoacan-por-la-paz-y-la-justicia-palacio-nacional-412391" target="_blank" rel="noopener" title="Plan Michoacán por la Paz y la Justicia">
    <img src="/TTP2026/PLAN_MICH.png" alt="Plan Michoacán por la Paz y la Justicia">
  </a>
  <a href="https://icti.michoacan.gob.mx/convocatoria-comparte-tus-ideas/" target="_blank" rel="noopener" title="Comparte tus ideas">
    <img src="/TTP2026/IDEAS.png" alt="Comparte tus ideas">
  </a>
  
</div>

<p>La <strong>Escuela Nacional de Estudios Superiores, Unidad Morelia (ENES Morelia) de la Universidad Nacional Autónoma de México (UNAM)</strong> fue sede del <strong>Teacher Training Programme (TTP) 2026</strong>, una iniciativa de la <strong>Unión Astronómica Internacional (IAU)</strong> a través de su Oficina para la Enseñanza para la Astronomía (OAE) orientada a fortalecer la enseñanza de la astronomía en niveles educativos previos a la educación superior. Cabe mencionar que este año México contó con el apoyo para organizar el TTP en dos sedes: la ENES Morelia y el INAOE (del 26 al 28 de febrero de 2026).</p>

<p>Este encuentro académico se llevó a cabo del <strong>19 al 21 de marzo de 2026</strong> y reunió a docentes, investigadores y especialistas en astronomía y educación científica provenientes de diversas instituciones del país, entre ellas el Instituto de Radioastronomía y Astrofísica (IRyA-UNAM), el Instituto de Geofísica (IGUM-UNAM), el Instituto Nacional de Astrofísica, Óptica y Electrónica (INAOE), así como profesores de educación media superior de distintas regiones de México.</p>

<p>El TTP formó parte de los esfuerzos internacionales de la IAU para impulsar la formación docente en astronomía, promoviendo el desarrollo de herramientas pedagógicas, el intercambio de experiencias y la vinculación entre la investigación científica y la práctica educativa. En México, esta iniciativa se articuló con la creación de la <strong>Red de Docentes por la Enseñanza de la Astronomía</strong>, cuyo objetivo es consolidar una comunidad académica que fortalezca la enseñanza de esta disciplina en el aula.</p>

<p>Durante los tres días de actividades, el programa contempló una combinación de <strong>sesiones académicas, talleres prácticos y actividades de observación astronómica</strong>, diseñadas para proporcionar a los docentes herramientas conceptuales y didácticas aplicables en sus contextos educativos. Entre los temas que se abordaron destacaron los fundamentos del Sistema Solar, cosmología, estructura de la galaxia, leyes fundamentales de la física, clima espacial y el uso de datos en ciencias espaciales.</p>

<p>Asimismo, el taller incluyó actividades prácticas como la <strong>observación del cielo con telescopios</strong>, el uso de software educativo y el desarrollo de estrategias de enseñanza adaptadas a distintos entornos escolares. Estas experiencias permitieron a los participantes no solo fortalecer sus conocimientos, sino también obtener las bases para replicar estas actividades en sus propias instituciones.</p>

<p>Un componente central del TTP 2026 fue la <strong>interacción entre docentes y especialistas</strong>, lo cual fomentó el diálogo entre la investigación astronómica y la práctica educativa. Este enfoque buscó generar un impacto a largo plazo mediante la formación de docentes multiplicadores capaces de impulsar vocaciones científicas entre estudiantes de nivel medio superior.</p>

<p>En este sentido, la realización de este taller en Michoacán también se alineó con los principios del <strong>Plan Michoacán por la Paz y la Justicia 2025</strong>, al promover la educación científica como una herramienta de transformación social. Iniciativas como el TTP contribuyeron a generar entornos educativos más equitativos, fortalecer el pensamiento crítico y ofrecer a las y los jóvenes alternativas de desarrollo académico y profesional.</p>

<p>La culminación de este evento posicionó a la ENES Morelia como un nodo estratégico para el desarrollo de la educación científica en el país y reafirmó el compromiso de la UNAM y de las instituciones participantes con la formación de comunidades educativas sólidas en el ámbito de la astronomía.</p>

<p>Con el cierre del TTP, la Unión Astronómica Internacional y las instituciones mexicanas participantes contribuyeron de manera significativa a <strong>acercar la ciencia a las aulas, fortalecer la cultura científica y motivar a nuevas generaciones a explorar el universo</strong>.</p>

<h3><strong>PROGRAMA (Resumen de actividades concluidas)</strong></h3>

<div class="ttp-table-wrapper">
<table class="ttp-table">
  <tr class="ttp-title-row">
    <td colspan="4">Teacher Training Programme (TTP) — Taller de Formación Docente en Astronomía de la IAU 2026</td>
  </tr>
  <tr>
    <th class="th-hora">Hora / Día</th>
    <th class="th-jue">Jueves 19</th>
    <th class="th-vie">Viernes 20</th>
    <th class="th-sab">Sábado 21</th>
  </tr>
  <tr>
    <td class="td-hora">8:00 – 9:00</td>
    <td class="td-jue td-llegada" rowspan="3">Llegada</td>
    <td class="td-vie td-break">Desayuno</td>
    <td class="td-sab td-break">Desayuno</td>
  </tr>
  <tr>
    <td class="td-hora">9:00 – 10:30</td>
    <td class="td-vie">Fundamentos del Sistema Solar. Actividad: escalas del Sistema Solar / software aplicado (<strong>Dra. Giovanna, ENESM</strong>)</td>
    <td class="td-sab">Cosmología (<strong>Dr. Erik Aquino Ortiz, IRyA</strong>)</td>
  </tr>
  <tr>
    <td class="td-hora">10:30 – 12:00</td>
    <td class="td-vie">Nuestro sol y visita al telescopio solar (<strong>Dr. Mario Rodríguez, ENESM, Mateo</strong>)</td>
    <td class="td-sab">LSST (<strong>Dra. Rosa Amelia, IRyA</strong>)<br>Introducción a Astroedu y otros recursos en línea (<strong>Diana/Raúl M/Mario/Rogelio, ENESM e INAOE</strong>)</td>
  </tr>
  <tr>
    <td class="td-hora">12:00 – 12:30</td>
    <td class="td-jue td-break">Receso</td>
    <td class="td-vie td-break">Receso</td>
    <td class="td-sab td-break">Receso</td>
  </tr>
  <tr>
    <td class="td-hora">12:30 – 14:00</td>
    <td class="td-jue td-empty"></td>
    <td class="td-vie">Nuestra galaxia y otras galaxias (<strong>Dr. Javier Ballesteros, IRyA</strong>)</td>
    <td class="td-sab">Discusión y acuerdos sobre la Red</td>
  </tr>
  <tr>
    <td class="td-hora">14:00 – 16:00</td>
    <td class="td-jue td-break">Comida</td>
    <td class="td-vie td-break">Comida</td>
    <td class="td-sab td-break">Comida</td>
  </tr>
  <tr>
    <td class="td-hora">16:00 – 16:30</td>
    <td class="td-inaug"><strong>INAUGURACIÓN</strong> (Dra. Yunuen, Tapia, Dir. ENESM, Dra. Alejandra Ochoa, Dir. ICTI, Dr. Luis Zapata, Dir. IRyA)</td>
    <td class="td-vie" rowspan="2">Leyes fundamentales: Leyes de Kepler y Ley de Gravitación Universal / Asteroides (<strong>Dr. Raúl Gutiérrez, IGUM</strong>)</td>
    <td class="td-sab td-regreso" rowspan="2">Regreso a casa</td>
  </tr>
  <tr>
    <td class="td-hora">16:30 – 18:00</td>
    <td class="td-jue">Bienvenida. Introducción a la OAE y los NAECs. Astronomía en los programas educativos en México (<strong>Diana/Raúl M/Mario/Rogelio, INAOE y ENESM</strong>)</td>
  </tr>
  <tr>
    <td class="td-hora">18:00 – 18:30</td>
    <td class="td-jue td-break">Receso</td>
    <td class="td-vie td-break">Receso</td>
    <td class="td-sab td-empty" rowspan="5"></td>
  </tr>
  <tr>
    <td class="td-hora" rowspan="2">18:30 – 20:00</td>
    <td class="td-jue" rowspan="2">Telescopios de nueva generación (NgVLA) en radioastronomía (<strong>Dr. Eric Jiménez-Andrade, IRyA</strong>)</td>
    <td class="td-vie">Clima Espacial y red e-Callisto: uso de datos en las Ciencias Espaciales (<strong>Dr. Ernesto Aguilar, IGUM</strong>)</td>
  </tr>
  <tr>
    <td class="td-vie">Modelado numérico del magnetismo solar en el bachillerato: un aprendizaje para otras estrellas (<strong>Dr. José Juan Avilés, ENESM</strong>)</td>
  </tr>
  <tr>
    <td class="td-hora">20:00 – 21:00</td>
    <td class="td-jue td-break">Cena</td>
    <td class="td-vie td-break">Cena</td>
  </tr>
  <tr>
    <td class="td-hora">21:00 – 23:00</td>
    <td class="td-jue">Práctica de observación con telescopios (<strong>LACIGE-ENESM, Mateo/Mario</strong>)</td>
    <td class="td-vie">Sesión actividades (<strong>Profesores bachillerato/Planetarios</strong>)</td>
  </tr>
</table>
</div>

<section class="ttp-videos-section" aria-labelledby="ttp-videos-heading">

<h3 id="ttp-videos-heading" class="ttp-title-header"><strong>Entrevistas a participantes</strong></h3>

<p class="ttp-videos-intro">Como parte de la documentación del taller se realizaron entrevistas a docentes, investigadores y especialistas asistentes. También puedes consultar la <a href="https://www.youtube.com/playlist?list=PL_rLqyjE0nMuiBmcruzQ-vQ6qR_QFIuXn" target="_blank" rel="noopener noreferrer">lista de reproducción completa en YouTube</a>.</p>

<div class="ttp-carousel" id="ttp-carousel" aria-roledescription="carrusel" aria-label="Entrevistas TTP 2026">
  <div class="ttp-carousel-viewport">
    <div class="ttp-carousel-track">
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="1 de 13">
        <button type="button" class="ttp-thumb" data-video-id="wLVzurRN2UE" aria-label="Reproducir entrevista 1 de 13">
          <img src="https://i.ytimg.com/vi/wLVzurRN2UE/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="2 de 13">
        <button type="button" class="ttp-thumb" data-video-id="DdlEGZa3zhI" aria-label="Reproducir entrevista 2 de 13">
          <img src="https://i.ytimg.com/vi/DdlEGZa3zhI/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="3 de 13">
        <button type="button" class="ttp-thumb" data-video-id="GT7K89WJTUg" aria-label="Reproducir entrevista 3 de 13">
          <img src="https://i.ytimg.com/vi/GT7K89WJTUg/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="4 de 13">
        <button type="button" class="ttp-thumb" data-video-id="Xw9LKi2j4do" aria-label="Reproducir entrevista 4 de 13">
          <img src="https://i.ytimg.com/vi/Xw9LKi2j4do/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="5 de 13">
        <button type="button" class="ttp-thumb" data-video-id="Vu0DNNFhnyM" aria-label="Reproducir entrevista 5 de 13">
          <img src="https://i.ytimg.com/vi/Vu0DNNFhnyM/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="6 de 13">
        <button type="button" class="ttp-thumb" data-video-id="893VUgFNGD8" aria-label="Reproducir entrevista 6 de 13">
          <img src="https://i.ytimg.com/vi/893VUgFNGD8/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="7 de 13">
        <button type="button" class="ttp-thumb" data-video-id="sqgoF00sDdI" aria-label="Reproducir entrevista 7 de 13">
          <img src="https://i.ytimg.com/vi/sqgoF00sDdI/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="8 de 13">
        <button type="button" class="ttp-thumb" data-video-id="jjqfcQyRQtU" aria-label="Reproducir entrevista 8 de 13">
          <img src="https://i.ytimg.com/vi/jjqfcQyRQtU/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="9 de 13">
        <button type="button" class="ttp-thumb" data-video-id="rOzk3aMXDIg" aria-label="Reproducir entrevista 9 de 13">
          <img src="https://i.ytimg.com/vi/rOzk3aMXDIg/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="10 de 13">
        <button type="button" class="ttp-thumb" data-video-id="W07G37k22U8" aria-label="Reproducir entrevista 10 de 13">
          <img src="https://i.ytimg.com/vi/W07G37k22U8/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="11 de 13">
        <button type="button" class="ttp-thumb" data-video-id="6ja5e6l_Etk" aria-label="Reproducir entrevista 11 de 13">
          <img src="https://i.ytimg.com/vi/6ja5e6l_Etk/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="12 de 13">
        <button type="button" class="ttp-thumb" data-video-id="sZBIPxtaA9o" aria-label="Reproducir entrevista 12 de 13">
          <img src="https://i.ytimg.com/vi/sZBIPxtaA9o/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
      <div class="ttp-carousel-slide" role="group" aria-roledescription="diapositiva" aria-label="13 de 13">
        <button type="button" class="ttp-thumb" data-video-id="GwYpX2DHgX8" aria-label="Reproducir entrevista 13 de 13">
          <img src="https://i.ytimg.com/vi/GwYpX2DHgX8/hqdefault.jpg" alt="" loading="lazy">
          <svg class="ttp-play-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.546 15.568V8.432L15.818 12l-6.272 3.568z" fill="#cc0000"/></svg>
        </button>
      </div>
    </div>
    <button type="button" class="ttp-carousel-btn ttp-prev" aria-label="Video anterior">‹</button>
    <button type="button" class="ttp-carousel-btn ttp-next" aria-label="Siguiente video">›</button>
  </div>
  <div class="ttp-carousel-dots" role="tablist" aria-label="Selección de video"></div>
  <p class="ttp-carousel-counter" aria-live="polite"><span class="ttp-current">1</span> / <span class="ttp-total">13</span></p>
</div>

<script>
(function () {
  const root = document.getElementById('ttp-carousel');
  if (!root || root.dataset.init === '1') return;
  root.dataset.init = '1';

  const track = root.querySelector('.ttp-carousel-track');
  const slides = Array.from(root.querySelectorAll('.ttp-carousel-slide'));
  const prevBtn = root.querySelector('.ttp-prev');
  const nextBtn = root.querySelector('.ttp-next');
  const dotsBox = root.querySelector('.ttp-carousel-dots');
  const counterCur = root.querySelector('.ttp-current');
  const total = slides.length;
  const AUTOPLAY_MS = 6000;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  let current = 0;
  let timer = null;

  const originalHTML = slides.map(s => s.innerHTML);

  slides.forEach((s, i) => {
    s.setAttribute('aria-hidden', i === 0 ? 'false' : 'true');
  });

  const dots = [];
  for (let i = 0; i < total; i++) {
    const d = document.createElement('button');
    d.type = 'button';
    d.className = 'ttp-dot';
    d.setAttribute('role', 'tab');
    d.setAttribute('aria-label', 'Ir al video ' + (i + 1) + ' de ' + total);
    d.setAttribute('aria-selected', i === 0 ? 'true' : 'false');
    d.addEventListener('click', () => { goTo(i); restart(); });
    dotsBox.appendChild(d);
    dots.push(d);
  }

  function resetSlide(idx) {
    const s = slides[idx];
    if (s.querySelector('iframe')) {
      s.innerHTML = originalHTML[idx];
      attachThumb(s);
    }
  }

  function attachThumb(slide) {
    const btn = slide.querySelector('.ttp-thumb');
    if (!btn) return;
    btn.addEventListener('click', () => {
      const id = btn.dataset.videoId;
      const iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0&modestbranding=1';
      iframe.title = btn.getAttribute('aria-label') || 'Video de YouTube';
      iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share');
      iframe.setAttribute('allowfullscreen', '');
      iframe.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
      slide.innerHTML = '';
      slide.appendChild(iframe);
      stop();
    });
  }

  slides.forEach(attachThumb);

  function goTo(idx) {
    resetSlide(current);
    current = ((idx % total) + total) % total;
    track.style.transform = 'translateX(-' + (current * 100) + '%)';
    slides.forEach((s, i) => s.setAttribute('aria-hidden', i === current ? 'false' : 'true'));
    dots.forEach((d, i) => d.setAttribute('aria-selected', i === current ? 'true' : 'false'));
    counterCur.textContent = String(current + 1);
  }

  function next() { goTo(current + 1); }
  function prev() { goTo(current - 1); }

  function start() {
    if (reduceMotion) return;
    stop();
    timer = window.setInterval(next, AUTOPLAY_MS);
  }
  function stop() {
    if (timer) { window.clearInterval(timer); timer = null; }
  }
  function restart() { stop(); start(); }

  prevBtn.addEventListener('click', () => { prev(); restart(); });
  nextBtn.addEventListener('click', () => { next(); restart(); });

  root.addEventListener('mouseenter', stop);
  root.addEventListener('mouseleave', start);
  root.addEventListener('focusin', stop);
  root.addEventListener('focusout', () => {
    if (!root.contains(document.activeElement)) start();
  });

  document.addEventListener('visibilitychange', () => {
    if (document.hidden) stop(); else start();
  });

  root.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft')  { e.preventDefault(); prev(); restart(); }
    if (e.key === 'ArrowRight') { e.preventDefault(); next(); restart(); }
  });

  start();
})();
</script>

</section>
