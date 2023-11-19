import { useCallback, useState } from 'react';
import ReactFlow, { Background, addEdge, applyEdgeChanges, applyNodeChanges } from 'reactflow';
import 'reactflow/dist/style.css';
import background from './etc/axis.svg'
import TextUpdaterNode from './etc/TextUpdaterNode.js';

import './etc/TextUpdaterNode.css';

const rfStyle = {
  backgroundColor: '#B8CEFF',
};

const initialNodes = [
  { id: 'baa', type: 'textUpdater', position: { x: 0, y: 0 }, data: { value: 123, random: 999 } },
  { id: 'bab', type: 'textUpdater', position: { x: 100, y: 200 }, data: { value: 124, random: 123} },
];
// we define the nodeTypes outside of the component to prevent re-renderings
// you could also use useMemo inside the component
const nodeTypes = { textUpdater: TextUpdaterNode };

function App() {
  const [nodes, setNodes] = useState(initialNodes);
  const [edges, setEdges] = useState([]);

  const onNodesChange = useCallback(
    (changes) => setNodes((nds) => applyNodeChanges(changes, nds)),
    [setNodes]
  );
  const onEdgesChange = useCallback(
    (changes) => setEdges((eds) => applyEdgeChanges(changes, eds)),
    [setEdges]
  );
  const onConnect = useCallback(
    (connection) => setEdges((eds) => addEdge(connection, eds)),
    [setEdges]
  );

  return (
    <ReactFlow
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      nodeTypes={nodeTypes}
      fitView
      style={rfStyle}
      >

      <Background
        // color = '#fff'
        style={{ backgroundImage: `url(${background})` }}
      />
    </ReactFlow>


);
}

export default App;
