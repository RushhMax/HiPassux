import React from 'react';
import Lobby from './Lobby';
import Register from './Register'
import Post from './Post'
import { Route, Routes } from "react-router-dom";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Lobby />} />
      <Route path="/register" element={<Register />} />
      <Route path="/posts" element={<Post />} />
    </Routes>
  );
};

export default App;
