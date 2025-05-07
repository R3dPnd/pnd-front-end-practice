import { LeftNavButton } from "./left-nav-btn-config";
import "./left-nav-btn.scss";

export default function LeftNavButtonComponent({label, href}: LeftNavButton){
    return (
        <a href={href} className="pnd-left-nav-btn">
            {label}
        </a>
    )
}