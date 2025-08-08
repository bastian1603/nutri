import { TextInput } from "flowbite-react";


const InputFood = ({id, label="", name="", type="", value=null, placeholder="", required = false, className="", input_change = () => {}}) => {

    return (
        <>
            <div className={`max-w-md ${className}`}>

            <label htmlFor={id}>{label}</label>
            <input className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2 w-xs" type={type} name={name} id={id} placeholder={placeholder} required={required} onChange={(e) => {
                input_change(e)
            }}/>
        
            </div>
        </>
    )

}

export default InputFood;