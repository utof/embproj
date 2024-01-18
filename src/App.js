import { useCallback, useState, useEffect } from 'react';
import ReactFlow, { Background, addEdge, applyEdgeChanges, applyNodeChanges } from 'reactflow';
import 'reactflow/dist/style.css';
// import BackgroundNode from './etc/bgNode.js';

import TextUpdaterNode from './etc/TextUpdaterNode.js';
import { GetNodes, initialNodes } from './etc/nodes.js';
import AxisNode from './etc/axisnode.js'

import { Readthenodes , updatetheNodes } from './readthenodes.js';
import './etc/TextUpdaterNode.css';

const rfStyle = {
  backgroundColor: '#B8CEFF',
};

// we define the nodeTypes outside of the component to prevent re-renderings
// you could also use useMemo inside the component
const nodeTypes = { textUpdater: TextUpdaterNode,
    AxisNode: AxisNode}; // why cant i add fucking axisnode 
    
function App() {

  const readnodes = Readthenodes(); 
  const [nodes, setNodes] = useState(readnodes);  
  const [edges, setEdges] = useState([]); 
  console.log(nodes);
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
  for(var i in nodes)
  updatetheNodes(i,nodes[i].position.x,nodes[i].position.y);
 
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
      {/* <BackgroundNode/> */}

      <Background
        // color = '#fff'
        // style={{ backgroundImage: `url(${background})` }}
      />
    </ReactFlow>


);
  const onLoad = (reactFlowInstance) => {
    reactFlowInstance.setBackgroundColor('#fff'); 
  }
}

export default App;
