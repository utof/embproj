import { GetNodes, initialNodes } from './etc/nodes.js'; 

function Readthenodes(){ 
	 
    const request = new XMLHttpRequest();
    request.open('GET', '/api', false); 
    request.send(null);
    if (request.status !== 200) {
      // handle an error here
      console.log("problem with the api");
      return null;
    }

    const data = JSON.parse(request.responseText); 
    return GetNodes(data);
}


export default Readthenodes;
