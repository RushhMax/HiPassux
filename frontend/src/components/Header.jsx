import React from 'react';

export const Header = () => {
  return (
    <header>
      <div className="container">
        <h1>PASSUX</h1>
        <div className="login-form">
          <input type="email" placeholder="Correo" className="input-email" />
          <input type="password" placeholder="Contraseña" className="input-password" />
          <button className="login-btn" >Login</button>
        </div>
      </div>
    </header>
  );
};

export const HeaderLobby = () => {
  const handleLoginClick = () => {
    window.location.href = `/register.html`;
  };
  return (
    <header>
      <div className="container">
        <img src="src/static/img/perfil.png" alt="Logoo" className="logo" />
        <img src="src/static/img/welcome.png" alt="welcome" className="welcome" />
        <nav>
          <a>Contact</a>
          <button className="sign-in">Sign in</button>
          <button className="register" onClick={handleLoginClick}>Register</button>
        </nav>
      </div>
    </header>
  );
};
