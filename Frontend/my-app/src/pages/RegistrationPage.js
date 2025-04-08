import React from 'react';
import Header from '../components/Header';
import '../styles/RegistrationPage.css';

const RegistrationForm = () => {
  return (
    <div className="container">
      <h1>Регистрация</h1>
      <p>При регистрации вы получаете информацию о прогулках по историческим местам, оплату участия в них и возможность смотреть выбранные нами заявки.</p>
      <form>
        <label htmlFor="name">ваше имя*</label>
        <input type="text" id="name" name="name" required />
        <label htmlFor="phone">телефон</label>
        <input type="text" id="phone" name="phone" />
        <label htmlFor="email">e-mail*</label>
        <input type="email" id="email" name="email" required />
        <label htmlFor="age">возраст</label>
        <input type="text" id="age" name="age" />
        <label>
          <input type="checkbox" name="consent" required />
          я даю согласие на обработку персональных данных
        </label>
        <button type="submit">Отправить заявку</button>
      </form>
    </div>
  );
};

const RegistrationPage = () => {
  return (
    <div>
      <Header />
      <div className="content">
        <RegistrationForm />
      </div>
    </div>
  );
};

export default RegistrationPage;