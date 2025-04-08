import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/LoginPage.css';

const LoginPage = () => {
  return (
    <div className="page-container">
      <Header />
      <div className="content">
        <h2>Войти</h2>
        <p>При входе в профиль вы можете отслеживать участие в прогулках, получать обновления и просматривать одобренные вами мероприятия.</p>
        <form>
          <label htmlFor="name">ваше имя*</label>
          <input type="text" id="name" name="name" required />
          <label htmlFor="phone">телефон*</label>
          <input type="text" id="phone" name="phone" required />
          <label htmlFor="email">e-mail*</label>
          <input type="email" id="email" name="email" required />
          <button type="submit">Отправить заявку</button>
        </form>
        <p>У вас нет аккаунта? <a href="/registration">Зарегистрироваться</a></p>
        <div className="contacts">
          <h3>Наши контакты</h3>
          <p><a href="/vk" title="VK канал">VK канал</a></p>
          <p><a href="/telegram" title="Telegram канал">Telegram канал</a></p>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default LoginPage;