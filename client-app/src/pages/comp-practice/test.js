import { useState } from 'react';

export default function Accordion({items}) {
  const [expandedItems, setExpandedItems] = useState(new Set());

  const toggleItem = (title) => {
    setExpandedItems(prev => {
      const next = new Set(prev);
      if (next.has(title)) {
        next.delete(title);
      } else {
        next.add(title);
      }
      return next;
    });
  };

  return (
    <div>
      {items.map((item) => (
        <div key={item.title}>
          <div 
            className="accordion-header" 
            onClick={() => toggleItem(item.title)}
          >
            {item.title}
            <span aria-hidden={true} className="accordion-icon" />
          </div>
          {expandedItems.has(item.title) && (
            <div>
              {item.content}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
