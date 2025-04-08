import React from 'react';
import Header from '../components/Header';
import '../styles/HomePage.css';

const HomePage = () => {
  return (
    <div>
      <Header />
      <div className="content">
        <h2>Добро пожаловать на Ruin Event</h2>
        <p>Организовываем и проводим уникальные мероприятия! Присоединяйтесь к нам, чтобы наслаждаться незабываемыми моментами.</p>
      </div>
    </div>
  );
};

export default HomePage;