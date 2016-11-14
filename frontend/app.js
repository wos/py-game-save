(function(){
    global.$ = require('jquery');
    global.React = require('react');
    global.ReactDOM = require('react-dom');

    let cards = [];


    const GameDisposition = require('./components/GameDisposition.jsx');
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
