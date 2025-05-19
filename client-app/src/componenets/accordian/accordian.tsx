import { useState } from 'react';
import './accordian.scss';

export default function Accordion() {
    const [display_html, setDisplayHtml] = useState(false);
    const [display_css, setDisplayCss] = useState(false);
    const [display_js, setDisplayJs] = useState(false);

    return (
      <div className="accordion-container">
        <div className="accordion-item">
          <div className="accordion-header" onClick={() => {setDisplayHtml(!display_html)}}>
            HTML{' '}
            <span
              aria-hidden={true}
              className="accordion-icon"
            />
          </div>
          { display_html &&
            <div className="accordion-content">
            The HyperText Markup Language or HTML is the
            standard markup language for documents designed to
            be displayed in a web browser.
          </div>
          }
          
        </div>
        <div className="accordion-item">
          <div className="accordion-header" onClick={() => {setDisplayCss(!display_css)}}>
            CSS{' '}
            <span 
              aria-hidden={true}
              className="accordion-icon"
            />
          </div>
          { display_css &&
            <div className="accordion-content">
              Cascading Style Sheets is a style sheet language
              used for describing the presentation of a document
              written in a markup language such as HTML or XML.
            </div>
          }
        </div>
        <div className="accordion-item">
          <div className="accordion-header" onClick={() => {setDisplayJs(!display_js)}}>
            JavaScript{' '}
            <span
              aria-hidden={true}
              className="accordion-icon"
            />
          </div>
          { display_js &&
            <div className="accordion-content">
              JavaScript, often abbreviated as JS, is a
              programming language that is one of the core
              technologies of the World Wide Web, alongside HTML
              and CSS.
            </div>
          }
        </div>
      </div>
    );
  }