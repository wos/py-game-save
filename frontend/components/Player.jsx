import { Items } from '../Constants.js';
import { DropTarget } from 'react-dnd';

import React from 'react';


const _colors = ['red', 'green', 'blue', 'lime', 'yellow'];


const cardTarget = {
  drop(props) {
    alert(`drop to player ${props.player.name}`)
  }
};

function collect(connect, monitor) {
  return {
    connectDropTarget: connect.dropTarget(),
    isOver: monitor.isOver()
  };
}

class Player extends React.Component {
    constructor(props) {
        super(props);
    }

    onDrop(data) {
        console.log(data);
    }

    render() {
        const {connectDropTarget, isOver } = this.props;

        let color = Math.round(Math.random() * 5);
        return  connectDropTarget(<div style={{height: 100, width: 100, backgroundColor: _colors[color]}}>
                {this.props.player.name}
            </div>);
    }
}


export default DropTarget(Items.CARD, cardTarget, collect)(Player);
