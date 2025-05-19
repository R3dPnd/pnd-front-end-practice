import Accordion from "../../componenets/accordian/accordian";

export default function CompPractice() {
    let accordianContent = {
        title: "Accordian",
        content: [
            {
                title: "Accordian 1",
                content: "This is the content for the accordian"
            },
            {
                title: "Accordian 2",
                content: "This is the content for the accordian"
            }
        ]
    }
    return (
        <div>
            <Accordion/>
        </div>
    )
}