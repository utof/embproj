import React from 'react';
import axis from './axis.svg'
import axis_node from './axisnode.css'
const AxisNode = ({ data }) => {
  return (
    <div className={axis_node}>
      <img src={axis} alt="axis" style={{dragging: false, width: 1500, height: 1500}} /> 
    </div>
  );// why style not working????
};

export default AxisNode;