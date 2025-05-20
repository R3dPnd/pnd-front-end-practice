import Accordion from "../../componenets/accordian/accordian";

export default function CompPractice() {

    let accordianContent = {
        title: "Accordian",
        content: [
            {
                title: "HTML",
                content: "The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser."
            },
            {
                title: "CSS",
                content: "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such HTML or XML."
            },
            {
                title: "JavaScript",
                content: "JavaScript, often abbreviated as JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS."
            }
        ]
    }
    return (
        <div>
            <Accordion items={accordianContent.content}/>
        </div>
    )
}