// TextUpdaterNode.js

import { useCallback } from 'react';

function TextUpdaterNode({ data }) {

  const onChange = useCallback((evt) => {
    console.log(evt.target.value);
  }, []);

  return (
    <div 
      className="text-updater-node"
      style={{width: '80%', height: '16%'}} 
    >
      <div className="input">
        <label>Text:</label> 
        <input onChange={onChange} />
      </div>
      {/* take actual id */}
      <div className="bottom">
        <div className="id">ABC</div> 
        <div className="workers">5</div>  
        <div className="random">0.423</div> 
      </div>
    </div>
  );
}

export default TextUpdaterNode;