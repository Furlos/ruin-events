import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import '../styles/HomePage.css';

const HomePage = () => {
  return (
    <div className="page-container">
      <Header />
      <div className="content">
        <h2>Добро пожаловать на Ruin Event</h2>
        <p>Организовываем и проводим уникальные мероприятия! Присоединяйтесь к нам, чтобы наслаждаться незабываемыми моментами.</p>
      </div>
      <Footer />
    </div>
  );
};

export default HomePage;