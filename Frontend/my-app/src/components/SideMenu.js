import React from 'react';
import '../styles/SideMenu.css';

const SideMenu = ({ closeMenu }) => {
  return (
    <div id="sideMenu" className="side-menu">
      <a href="javascript:void(0)" className="close-btn" onClick={closeMenu}>&times;</a>
      <a href="homepage.html">Главная</a>
      <a href="affiche.html">Афиша</a>
      <a href="donate.html">Донат</a>
      <a href="gallery.html">Галерея</a>
      <a href="profile.html">Профиль</a>
      <div className="social-links">
        <a href="#" title="VK канал">VK</a>
        <a href="#" title="Telegram канал">TG</a>
      </div>
      <a href="registry.html" className="register-btn">Регистрация</a>
    </div>
  );
};

export default SideMenu;