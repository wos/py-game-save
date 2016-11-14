const GameCard = require('./GameCard.jsx');
const Player = require('./Player.jsx');
const GameDisposition = React.createClass({
    getInitialState() {
        return {
            cards:[],
            players:[]
        };
    },
    componentWillMount() {
        $.get('/cards', {}, (response, tmp) => {
            this.setState({cards: response.cards, players: response.players});
        },
        'json');
  
    },

    render () {
        let players = this.state.players.map((player) => {
            return <Player key={player.id} player={player} />;
        });
        let cards = this.state.cards.map((item) => {
            return <GameCard {...item} />;
        });
        return (<div className="demo-card-wide mdl-grid">
            {players}
            {cards}
        </div>)
        }
});

module.exports = GameDisposition;