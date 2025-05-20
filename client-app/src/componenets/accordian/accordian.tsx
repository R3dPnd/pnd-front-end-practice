import { useState } from 'react';

import './accordian.scss';

interface AccordionItem {
  title: string;
  content: string;
  open?: boolean;
}

interface Props {
  items: AccordionItem[];
}

export default function Accordion({ items }: Props) {
  const [expandedItems, setExpandedItems] = useState<Set<string>>(new Set());

  const toggleItem = (item: AccordionItem) => {
    setExpandedItems(prev => {
      const next = new Set(prev);
      if (next.has(item.title)) {
        next.delete(item.title);
      } else {
        next.add(item.title);

      }
      return next;
    });
  };

  return (
    <div className="accordion-container">
      {items.map((item: AccordionItem) => (
        <div key={item.title} className="accordion-item">
          <div 
            className="accordion-header" 
            onClick={() => toggleItem(item)}
          >
            {item.title}
            <span aria-hidden={true} className={expandedItems.has(item.title) ? "accordion-icon--rotated" : "accordion-icon"} />
          </div>
          <div className={`accordion-content ${expandedItems.has(item.title) ? 'accordion-content--expanded' : ''}`}>
            <div className="accordion-content-inner">
              {item.content}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}
