import React from 'react';
import '../styles/ProfilePage.css';

const Profile = () => {
    const openMenu = () => {
        document.getElementById("sideMenu").style.width = "250px";
    };

    const closeMenu = () => {
        document.getElementById("sideMenu").style.width = "0";
    };

    return (
        <div>
            <div className="header">
                <h1>Ruin Event</h1>
                <div className="menu-icon" onClick={openMenu}>
                    <div></div>
                    <div></div>
                    <div></div>
                </div>
            </div>
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
            <div className="content">
                <div className="profile-info">
                    <h2>Профиль</h2>
                    <p><strong>Имя:</strong> Иван Иванов</p>
                    <p><strong>Email:</strong> ivan@example.com</p>
                    <p><strong>Возраст:</strong> 28</p>
                    <p><strong>Мероприятия:</strong> Участник 5 мероприятий</p>
                </div>
                <div className="upcoming-events">
                    <h2>Предстоящие мероприятия</h2>
                    <div className="event">
                        <h3>Путешествие по Мещерскому краю</h3>
                        <p><strong>Дата:</strong> 12 апреля</p>
                        <p><strong>Место:</strong> Граница Мещерского края</p>
                    </div>
                    <div className="event">
                        <h3>Археологический раскоп</h3>
                        <p><strong>Дата:</strong> 13 апреля</p>
                        <p><strong>Место:</strong> Долина реки Клязьмы</p>
                    </div>
                </div>
            </div>
            <div className="footer">
                <p>&copy; 2025 Ruin Event. Все права защищены.</p>
            </div>
        </div>
    );
}

export default Profile;