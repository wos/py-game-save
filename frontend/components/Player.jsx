import React from 'react';
import Droppable from 'react-drag-and-drop'


const _colors = ['red', 'green', 'blue', 'lime', 'yellow'];

const Player = React.createClass({
    onDrop(data) {
        console.log(data);
    },
    render() {
        let color = Math.round(Math.random() * 5);
        return <Droppable types={["card"]} onDrop={this.onDrop}>
            <div style={{height: 100, width: 100, backgroundColor: _colors[color]}}>
                {this.props.player.name}
            </div>
        </Droppable>;
    }
});

module.exports = Player;
// Player.propTypes = {
  // knightPosition: PropTypes.arrayOf(
  //   PropTypes.number.isRequired
  // ).isRequired
// };