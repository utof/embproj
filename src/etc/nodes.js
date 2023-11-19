//nodes.js
export const initialNodes = [
    { id: 'axis', type: 'AxisNode', position: { x: 0, y: 0 }, selectable: false, draggable: false, isConnectable: false}, //https://stackoverflow.com/questions/71586417/react-flow-can-you-pass-props-to-a-custom-node-in-react-flow
    { id: 'baa', type: 'textUpdater', position: { x: -100, y: -100 }, data: { value: 123, random: 999 } },
    { id: 'bab', type: 'textUpdater', position: { x: 100, y: 200 }, data: { value: 124, random: 123} },
  ];