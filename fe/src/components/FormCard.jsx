import { Card } from "flowbite-react";

const FormCard = ({children, class_name}) => {
    return (<>
        <form className={class_name}>
            {children}
        </form>
    
    </>)
}

export default FormCard;