import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/DonatePage.css';

const DonatePage = () => {
  return (
    <div className="page-container">
      <Header />
      <div className="content">
        <h2>Помочь сообществу</h2>
        <p>Вы можете поддержать наше сообщество, сделав пожертвование. Ваша помощь позволит нам организовывать больше мероприятий и сохранять историческое наследие.</p>
        <a href="https://ruin-keepers.ru/donate" target="_blank" rel="noopener noreferrer">
          <button className="donate-button">Перейти</button>
        </a>
      </div>
      <Footer />
    </div>
  );
};

export default DonatePage;