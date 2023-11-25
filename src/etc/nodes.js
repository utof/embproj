// nodes.js

export const initialNodes = [
    { 
      id: 'axis', 
      type: 'AxisNode', 
      position: { x: 0, y: 0 }, 
      selectable: false, 
      draggable: false, 
      isConnectable: false
    },
  
    { 
      id: 'poloski', 
      type: 'textUpdater', 
      position: { x: 1000, y: 500 }, 
      data: { value: 123, random: 999 }
    },
  
    { 
      id: 'transcribe', 
      type: 'textUpdater',  
      position: { x: 700, y: 200 }, 
      data: { value: 124, random: 123}
    },
  
    {
      id: 'autoblood',
      type: 'textUpdater',
      position: { x: 650, y: 900 },
      data: { value: 125, random: 456 }
    },
  
    {
      id: 'cart',
      type: 'textUpdater',  
      position: { x: 300, y: 800 },
      data: { value: 126, random: 789 } 
    },
  
    {
      id: 'cardio-case',
      type: 'textUpdater',
      position: { x: 800, y: 1100 },
      data: { value: 127, random: 159 }
    },
  
    {
     id: 'case-analis',
     type: 'textUpdater',
     position: { x: 500, y: 1100 },  
     data: { value: 128, random: 357 }
    }
  ];