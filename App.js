import { useCallback, useState } from 'react';
import ReactFlow, { Background, addEdge, applyEdgeChanges, applyNodeChanges } from 'reactflow';
import 'reactflow/dist/style.css';
// import BackgroundNode from './etc/bgNode.js';

import TextUpdaterNode from './etc/TextUpdaterNode.js'; 
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
const readnodes = Readthenodes();  
function App() {

  
  const [nodes, setNodes] = useState(readnodes);  
  const [edges, setEdges] = useState([]); 
 
  const onNodesChange = useCallback(
    (changes) => 
    {
    	setNodes((nds) => applyNodeChanges(changes, nds));
    	if(changes[0].type == "position")
    	 if(changes[0].dragging)
    	   updatetheNodes(changes[0].id,changes[0].position.x,changes[0].position.y);	 
    },
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
      {/* <BackgroundNode/> */}

      <Background
        // color = '#fff'
        // style={{ backgroundImage: `url(${background})` }}
      />
    </ReactFlow>


); 
}

export default App;
