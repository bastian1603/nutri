import { useEffect, useState } from "react";
import { DayPicker } from "react-day-picker";
import "react-day-picker/style.css";

import InputFood from "../components/InputFood";


import Layout from "../components/Layout";

const Home = () => {
    const [ date_picked, set_date_picked ] = useState((new Date().toDateString()));
    const [ food_data, set_food_data ] = useState({
       food_name: "asdasdasd",
       calories: "" 
    });

    async function add_food(){
        const body = JSON.stringify({
            food_name: food_data.food_name, 
            calories: food_data.calories,
            datetime: (new Date()).toISOString().slice(0, 19).replace('T', ' ')
        });
        
        await fetch("http://127.0.0.1:8000/daily_consumption", {
            method: "POST",
            body: body,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('token')
            }
        }).then(response => response.json())
        .then(response => {
            console.log(response)
        });
    }

    function update_food_data(e){
        const {name, value} = e.target;

        console.log(name)
        set_food_data(prev => ({...prev, [name]: value}))
    }
    
    function refresh_display(items){
        console.log(items)
        const container = document.getElementById('daily_food');
        
        container.innerHTML = items.map(item => `<li>${item.food_name}</li>`);
        
    }

    async function get_day_comp(){

        await fetch('http://127.0.0.1:8000/daily_consumption/', {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('token')
            }
        }).then(response => response.json())
        .then(response => {
            refresh_display(response.results)
        });

    }

    useEffect(() => {
        console.log('dsfsfd')

        get_day_comp();

        console.log('asdasd')

    }, [date_picked]);


    return (
        <>

        <Layout>
                <div>
                    {date_picked}
                    <br />
                    {food_data.food_name}
                    <br />
                    {food_data.calories}
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

                <div className="max-w-md border rounded-sm ring ring-teal-400 p-2 ">   
                    <h1 className="text-lg pl-2">Add Food</h1>

                    <InputFood className="my-2" id="food_name" name="food_name" placeholder="Sudah makan apa anda hari ini" input_change={update_food_data}/>
                    <InputFood className="my-2" id="calories" name="calories" placeholder="Berapa Jumlah kalori makanan tersebut?" input_change={update_food_data}/>
                    
                    <button className="px-2 rounded-md border border-teal-500 bg-teal-400 text-white" onClick={add_food}>Add</button>

                </div>

                <br />
                <br />
                <ul id="daily_food">

                </ul>
            </Layout>
        </>
    );
}

export default Home;