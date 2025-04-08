import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import '../styles/Header.css';

const Header = () => {
  const [dropdownOpen, setDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setDropdownOpen(!dropdownOpen);
  };

  return (
    <div className="header">
      <h1>Ruin Event</h1>
      <div className="menu-icon" onClick={toggleDropdown}>
        <div></div>
        <div></div>
        <div></div>
      </div>
      {dropdownOpen && (
        <div className="dropdown-menu">
          <Link to="/">Главная</Link>
          <Link to="/affiche">Афиша</Link>
          <Link to="/donate">Донат</Link>
          <Link to="/gallery">Галерея</Link>
          <Link to="/profile">Профиль</Link>
          <Link to="/vk" title="VK канал">VK канал</Link>
          <Link to="/telegram" title="Telegram канал">Telegram канал</Link>
          <Link to="/registration">Регистрация</Link>
        </div>
      )}
    </div>
  );
};

export default Header;