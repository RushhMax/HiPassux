import React from 'react';

const Header = () => {
  return (
    <header>
      <div className="container">
        <h1>PASSUX</h1>
        <div className="login-form">
          <input type="email" placeholder="Correo" className="input-email" />
          <input type="password" placeholder="Contraseña" className="input-password" />
          <button className="login-btn">Login</button>
        </div>
      </div>
    </header>
  );
};

export default Header;
