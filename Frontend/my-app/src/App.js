import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import AffichePage from './pages/AffichePage';
import DonatePage from './pages/DonatePage';
import GalleryPage from './pages/GalleryPage';
import ProfilePage from './pages/ProfilePage';
import VKPage from './pages/VKPage';
import TelegramPage from './pages/TelegramPage';
import RegistrationPage from './pages/RegistrationPage';
import LoginPage from './pages/LoginPage';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/affiche" component={AffichePage} />
        <Route path="/donate" component={DonatePage} />
        <Route path="/gallery" component={GalleryPage} />
        <Route path="/profile" component={ProfilePage} />
        <Route path="/vk" component={VKPage} />
        <Route path="/telegram" component={TelegramPage} />
        <Route path="/registration" component={RegistrationPage} />
        <Route path="/login" component={LoginPage} />
        <Route path="/" component={HomePage} />
      </Switch>
    </Router>
  );
}

export default App;