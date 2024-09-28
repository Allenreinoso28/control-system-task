import React from 'react';
import { FixedSizeList as List } from 'react-window';

const CommandList = ({ commands }) => {
  const heightInVW = 16.8; // Example height in viewport width units without the 'vw' string
  const fontSizeInVW = 2; // Example font size in viewport width units

  return (
    <div>
      <List
        // Calculate height based on viewport width
        height={(heightInVW / 100) * window.innerWidth} 
        itemCount={commands.length}
        // Calculate item size based on viewport width
        itemSize={(fontSizeInVW / 100) * window.innerWidth}
        width={'100%'}
      >
        {({ index, style }) => (
          <div style={style} key={index}>
            {commands[index]}
          </div>
        )}
      </List>
    </div>
  );
};

export default CommandList;
