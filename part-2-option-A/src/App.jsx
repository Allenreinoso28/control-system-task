// App.js
import './App.css';
import React, { useEffect, useState } from 'react';
import ArmGroup from './compenents/armGroup';
import WheelGroup from './compenents/wheelGroup';
import BarChart from './compenents/barChart';
import MyImage from './images/rover.svg'
import CommandList from './compenents/commandList'; // Import the CommandList component


function App() {
  const [commands, setCommands] = useState([]);
  const [armCommands, setArmCommand] = useState([]);
  const [armCommandsElbow, setElbowCommand] = useState([]);
  const [armCommandsWristR, setWristRCommand] = useState([]);
  const [armCommandsWristL, setWristLCommand] = useState([]);
  const [armCommandsClaw, setClawCommand] = useState([]);
  const [armCommandsGantry, setGantryCommand] = useState([]);
  const [armCommandsShoulder, setShoulderCommand] = useState([]);

  const [driveCommands, setDriveCommand] = useState([]);
  const [driveCommandsRight, setRightCommand] = useState([]);
  const [driveCommandsLeft, setLeftCommand] = useState([]);

  const [displayList, setDisplayList] = useState('commands');

  const addToFrontIfDifferent = (number, list, setList) => {
    // Check if the list is empty or the first element is different from the number
    if (list.length === 0 || list[0] !== number) {
      setList(prevCommands => [number, ...prevCommands]); // Update the state with the new list
    }
  };

  const getCurrentDisplayList = () => {
    if (displayList === 'arm') return armCommands;
    if (displayList === 'drive') return driveCommands;
    if (displayList === 'driveLeft') return driveCommandsLeft;
    if (displayList === 'driveRight') return driveCommandsRight;
    if (displayList === 'elbow') return armCommandsElbow;
    if (displayList === 'wristRight') return armCommandsWristR;
    if (displayList === 'wristLeft') return armCommandsWristL;
    if (displayList === 'claw') return armCommandsClaw;
    if (displayList === 'gantry') return armCommandsGantry;
    if (displayList === 'shoulder') return armCommandsShoulder;
    return commands;
  };
  
  useEffect(() => {
    const socket = new WebSocket('ws://localhost:8765');

    socket.onopen = () => {
      console.log('Connected to WebSocket server');
    };

    socket.onmessage = (event) => {
      const message = event.data;
      const parsed = message.split('_').slice(1);
      setCommands(prevCommands => [message, ...prevCommands]);

      if (message.startsWith('A_')) {
        setArmCommand(prevArmCommand => [message, ...prevArmCommand]);
        //update elbow
        addToFrontIfDifferent(parsed[0], armCommandsElbow, setElbowCommand)
        //update wristR
        addToFrontIfDifferent(parsed[1], armCommandsWristR, setWristRCommand)
        //update wristL
        addToFrontIfDifferent(parsed[2], armCommandsWristL, setWristLCommand)
        //update claw
        addToFrontIfDifferent(parsed[3], armCommandsClaw, setClawCommand)
        //update gantry
        addToFrontIfDifferent(parsed[4], armCommandsGantry, setGantryCommand)
        //update shoulder
        addToFrontIfDifferent(parsed[5], armCommandsShoulder, setShoulderCommand)

      } else if (message.startsWith('D_')) {
        setDriveCommand(prevDriveCommand => [message, ...prevDriveCommand]);
        //update wheels right
        addToFrontIfDifferent(parsed[0], driveCommandsRight, setRightCommand)
        //update wheels left
        addToFrontIfDifferent(parsed[3], driveCommandsLeft, setLeftCommand)
      }
    };

    socket.onclose = () => {
      console.log('WebSocket connection closed');
      alert('WebSocket has been closed')
    };

    socket.onerror = (error) => {
      console.error('WebSocket error:', error);
      alert('WebSocket error:', error)
      };

    return () => {
      socket.close();
    };
  }, []); //empty array so that connection is only made once

  return (
    <div className='app_container'>

          <div className="left">
            <div className='rover-visual-container'>
              <div className='rover-visual-title'>∗Drive System</div>
              <div className='rover-visual-content'> 
                <BarChart commands={driveCommands} name="h" id="3"/>
                <img className='rover-svg' src={MyImage} alt="rover"/>
                <BarChart commands={driveCommands} name="h" id="0"/>
              </div>
            </div>
            <div className="command-current">
              <div className='command-span'>Current:</div>
              <div className='command-value'>{driveCommands[0]}</div>
            </div>
            <WheelGroup commands={driveCommands}/>
          </div>

      <div class="right">
          <div className="top-right">
            <ArmGroup commands={armCommands}/>
            <div className="command-current">
              <div className='command-span'>Current:</div>
              <div className='command-value'>{armCommands[0]}</div>
            </div>
          </div>
          <div className="bottom-right">
            <div className='terminal-container'>
              <div className='terminal-tab-bar'>
                <button className={displayList === 'commands' ? 'active' : ''} onClick={() => setDisplayList('commands')}> General</button>
                <button className={displayList === 'drive' ? 'active' : ''} onClick={() => setDisplayList('drive')}>Drive Commands</button>
                <button className={displayList === 'driveLeft' ? 'active' : ''} onClick={() => setDisplayList('driveLeft')}>L</button>
                <button className={displayList === 'driveRight' ? 'active' : ''} onClick={() => setDisplayList('driveRight')}>R</button>
                <button className={displayList === 'arm' ? 'active' : ''} onClick={() => setDisplayList('arm')}>Arm Commands</button>
                <button className={displayList === 'elbow' ? 'active' : ''} onClick={() => setDisplayList('elbow')}>E</button>
                <button className={displayList === 'wristRight' ? 'active' : ''} onClick={() => setDisplayList('wristRight')}>WR</button>
                <button className={displayList === 'wristLeft' ? 'active' : ''} onClick={() => setDisplayList('wristLeft')}>WL</button>
                <button className={displayList === 'claw' ? 'active' : ''} onClick={() => setDisplayList('claw')}>C</button>
                <button className={displayList === 'gantry' ? 'active' : ''} onClick={() => setDisplayList('gantry')}>G</button>
                <button className={displayList === 'shoulder' ? 'active' : ''} onClick={() => setDisplayList('shoulder')}>S</button>
              </div>
              <div className='terminal-content'><CommandList commands={getCurrentDisplayList()}/></div>
            </div>
          </div>
      </div>
      
    </div>
    
  );
}

export default App;
