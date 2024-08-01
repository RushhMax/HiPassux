import React from 'react';
import apiFetch from '../services/api-fetch'; // Asegúrate de tener este servicio para hacer fetch

export const Header = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await apiFetch('users/login', {
        method: 'POST',
        body: JSON.stringify({ username: username, password: password }),
        headers: { 'Content-Type': 'application/json' }
      });

      if (response.access_token) {
        // Guardar el token en el local storage o en el estado global de la app
        localStorage.setItem('access_token', response.access_token);
        setError(null);
        // Redirigir al usuario o actualizar la UI según sea necesario
      } else {
        setError('Invalid username or password');
      }
    } catch (error) {
      setError('Failed to login. Please try again.');
    }
  };

  return (
    <header>
      <div className="container">
        <h1>PASSUX</h1>
        <div className="login-form">
          <input
            type="text"
            placeholder="Usuario"
            className="input-username"
            value={username}
            onChange={handleUsernameChange}
          />
          <input
            type="password"
            placeholder="Contraseña"
            className="input-password"
            value={password}
            onChange={handlePasswordChange}
          />
          <button className="login-btn" onClick={handleLogin}>Login</button>
          {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
      </div>
    </header>
  );
};


const Footer = () => {
  return (
    <footer>
      <div className="container">
        <div className="links">
          <div>
            <h3>About Us</h3>
            <ul>
              <li>Our Story</li>
              <li>Blog</li>
              <li>Careers</li>
              <li>Press</li>
            </ul>
          </div>
          <div>
            <h3>Support</h3>
            <ul>
              <li>Help Center</li>
              <li>Community Guidelines</li>
              <li>Safety Tips</li>
              <li>Contact Us</li>
            </ul>
          </div>
          <div>
            <h3>Legal</h3>
            <ul>
              <li>Privacy Policy</li>
              <li>Terms of Service</li>
              <li>Cookie Policy</li>
              <li>Accessibility</li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
