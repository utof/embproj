// TextUpdaterNode.js

import { useCallback } from 'react';

function TextUpdaterNode({ data }) {

  const onChange = useCallback((evt) => {
    console.log(evt.target.value);
  }, []);

  return (
    <div 
      className="text-updater-node"
      style={{width: '100%', height: '16%'}} 
    >
      <div className="input">
        <label>Name:</label> 
        <input onChange={onChange} />
      </div>
      {/* take actual id */}
      <div className="bottom">
        <div className="id">{data["\ufeffName"]}</div> 
        <div className="id">{data.customer}</div> 
        <div className="id">{data.responsible}</div>  
        <div className="id">{data.stage}</div> 
      </div>
    </div>
  );
}

export default TextUpdaterNode;
