import LeftNavButtonComponent from "./left-nav-btn";
import { leftNavButtons } from "./left-nav-btn-config";
import "./left-nav.scss";

interface Props {
  children?: any;
}

const buttons = leftNavButtons.map(button => 
       <LeftNavButtonComponent label={button.label} href={button.href}/>
)

export default function PndLeftNav({ children }: Props) {
  return <div className="left-nav-container">
        {children}
        {buttons}
    </div>;
}
