import { useEffect, useState } from "react";
import {DayPicker} from "react-day-picker";
import "react-day-picker/style.css";

const Home = () => {
    const [ date_picked, set_date_picked ] = useState((new Date().toDateString()));
    

    return (
        <>
            <div>
                {date_picked}
            </div>

            <DayPicker 
            animate
            mode="single"
            selected={date_picked}
            onSelect={(e) => {
                set_date_picked(e.toDateString());
            }}
            footer={
                date_picked ? `Selected: ${date_picked}` : "Pick a day."
            }>

            </DayPicker>
        </>
    );
}

export default Home;