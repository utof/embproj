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

function updatetheNodes(i,x,y){
    const request = new XMLHttpRequest(); 
    request.open('POST', '/apipos', false); 
    request.setRequestHeader("Content-type", "application/json;charset=UTF-8"); 
    request.send(JSON.stringify({"id":i-1,"pos":{"x":x,"y":y}})); 
    if (request.status !== 200) {
      // handle an error here
      console.log(request.status);
      return null;
    }
    
}

export { Readthenodes , updatetheNodes };
