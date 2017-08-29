import GameDisposition from './components/GameDisposition.jsx';
import React from 'react';
import ReactDOM from 'react-dom';

(function(){
    global.$ = require('jquery');

    let cards = [];

    let app = {
        init: function(){
            let host = document.getElementById('app-block');
            let node = document.createElement('div');
            ReactDOM.render(<GameDisposition />, node);
            $(host).append(node);
        }

    };



    window.app = app;
})();
