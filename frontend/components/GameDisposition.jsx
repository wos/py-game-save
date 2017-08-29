import { DragDropContext } from 'react-dnd';
import HTML5Backend from 'react-dnd-html5-backend';
import React, {Component} from 'react';

import GameCard from './GameCard.jsx';
import Player from './Player.jsx';


class GameDisposition extends Component {

    constructor(props) {
        super(props);
        this.state = {
            cards:[],
            players:[]
        };
    }

    componentWillMount() {
        $.get('/cards', {}, (response, tmp) => {
            this.setState({cards: response.cards, players: response.players});
        },
        'json');
    }

    render () {
        let players = this.state.players.map((player) => {
            return <Player key={player.id} player={player} />;
        });
        let cards = this.state.cards.map((item) => {
            return <GameCard key={item.id} {...item} />;
        });
        return (<div className="demo-card-wide mdl-grid">
            {players}
            {cards}
        </div>)
    }
}

GameDisposition.displayName = 'GameDisposition';

export default DragDropContext(HTML5Backend)(GameDisposition);