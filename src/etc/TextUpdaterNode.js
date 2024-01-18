// TextUpdaterNode.js

import { useCallback } from 'react';
import "./TextUpdaterNode.css";
import QRCode from "react-qr-code";


function TextUpdaterNode({ data }) {
  const showqr = false;
  const onChange = useCallback((evt) => {
    console.log(evt.target.value);
  }, []); 
  if(showqr)
  return (
    <div 
      className="text-updater-node"
      style={{width: '300px', height: '300px'}} 
    >
      <div>
        <label>Name:</label> 
        <input onChange={onChange} />
      </div>
      {/* take actual id */}
      <div className="bottom">
        <table>
        <tr><div className="id">{data["\ufeffName"]}</div> </tr> 
        <tr><QRCode size={200} id="qrcode" value={data.link} /></tr>
        </table>
      </div>
    </div>
  );
  else
  return (
    <div 
      className="text-updater-node"
      style={{width: '300px', height: '300px'}} 
    >
      <div>
        <label>Name:</label> 
        <input onChange={onChange} />
      </div>
      {/* take actual id */}
      <div className="bottom">
        <div className="id">{data["\ufeffName"]}</div>  
        <div className="id">{data["customer"]}</div> 
        <div className="id">{data["responsible"]}</div> 
        <div className="id">{data["stage"]}</div> 
      </div>
    </div>
  );
}

export default TextUpdaterNode;
