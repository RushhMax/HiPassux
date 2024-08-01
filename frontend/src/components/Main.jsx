import React from 'react';

export const Main = () => {
  return (
    <main>
      <div className="container">
        <div className="left">
          <img src="src/static/img/network-image.png" alt="Network Diagram" />
        </div>
        <div className="content-right">
          <div className="passux-tittle">
            <h2>Register to PASSUX</h2>
          </div>
          <div className="right">
            <form>
              <label htmlFor="name">Nombre</label>
              <input type="text" id="name" name="name" />
              <label htmlFor="apellido">Apellido</label>
              <input type="text" id="apellido" name="apellido" />
              <label htmlFor="username">Username</label>
              <input type="text" id="username" name="username" />
              <label htmlFor="fecha-nacimiento">Nacimiento</label>
              <input type="date" id="nacimiento" name="nacimiento" />
              <label htmlFor="email">Email</label>
              <input type="email" id="email" name="email" />
              <label htmlFor="password">Contraseña</label>
              <input type="password" id="password" name="password" />
              <button type="submit">Register</button>
            </form>
          </div>
        </div>
      </div>
    </main>
  );
};

export const MainLobby = () => {
  return (
    <main>
      <div className="containerAnuncios">
        <aside aria-label="anuncio" className="img-anuncio">
          <img src="src/static/img/anuncio.png" alt="img-perfil" />
        </aside>
        <div className="img-mensaje">
          <img src="src/static/img/mensajePassux.png" alt="img-perfil" />
        </div>
      </div>
    </main>
  );
};

export const AnuncioLobby = () => {
  return (
    <section className="main-content">
      <img src="src/static/img/mensajeAnuncio.png" alt="mensajeAnuncio" />
    </section>
  );
};
