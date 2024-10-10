import React from 'react';
import { Routes, Route } from 'react-router-dom';
import App from './App';
import Home from './Home';

const AppRoutes = () => {
    return (
        <Routes>
            {/* <Route path="/" element={<App />} /> */}
            <Route path="/home" element={<Home />} />
        </Routes>
    );
};

export default AppRoutes;
