import Draggable from 'react-drag-and-drop'

const GameCard = React.createClass({
    render () {
        return (<Draggable><div className="demo-card-wide mdl-card mdl-shadow--2dp">
              <div className="mdl-card__title" 
                   style={{ background: this.props.color, color: this.props.side == 'dark' ? '#fff':'#444'}}>
                <h2 className="mdl-card__title-text">{this.props.name}</h2>
              </div>
              <div className="mdl-card__supporting-text">
    
              </div>
              <div className="mdl-card__actions mdl-card--border">
                <a className="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                  Get Started
                </a>
              </div>
              <div className="mdl-card__menu">
                <button className="mdl-button mdl-button--icon mdl-js-button mdl-js-ripple-effect">
                  <i className="material-icons">share</i>
                </button>
              </div>
            </div></Draggable>)
        }
});

module.exports = GameCard;