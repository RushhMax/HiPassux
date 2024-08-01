import React from 'react';
import {HeaderLobby} from './components/Header.jsx';
import {MainLobby,AnuncioLobby} from './components/Main.jsx';
import Footer from './components/Footer.jsx';
import './static/stylesLobby.css';

const Lobby = () => {
  return (
    <div>
      <HeaderLobby />
      <MainLobby />
      <AnuncioLobby/>
      <Footer />
    </div>
  );
};

export default Lobby;
