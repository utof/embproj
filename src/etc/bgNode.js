// BackgroundNode.js

import { Handle, useReactFlow } from 'reactflow';
import bg from './axis.svg'

import { useRef, useEffect } from 'react'; 

const BackgroundNode = () => {

  const svgRef = useRef(null);

  useEffect(() => {
    const handleTransform = () => {
        if (!svgRef.current) {
            return; 
        }
        
        const { x, y, zoom } = svgRef.current.parentElement.__rf.viewport;
        
        svgRef.current.style.transform = `translate(${x}px, ${y}px) scale(${zoom})`;
    };
    
    const reactFlow = svgRef.current.parentElement.__rf;

    reactFlow.on('viewportChange', handleTransform);

    handleTransform();

    return () => reactFlow.off('viewportChange', handleTransform);

  }, []);

  return (
    <svg ref={svgRef}>
      // bg image
    </svg>
  );

};

export default BackgroundNode;