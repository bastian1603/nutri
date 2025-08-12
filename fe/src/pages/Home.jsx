import { useEffect, useState } from "react";
import { DayPicker } from "react-day-picker";
import "react-day-picker/style.css";

import InputFood from "../components/InputFood";


import Layout from "../components/Layout";

const Home = () => {
    const [ date_picked, set_date_picked ] = useState(((new Date()).setHours(0, 0, 0, 0)));
    const [ food_data, set_food_data ] = useState({
       food_name: "asdasdasd",
       calories: "" 
    });

    const [ food_list, set_food_list ] = useState([]);


    // pakai food_data untuk add food
    async function add_food(){
        const body = JSON.stringify({
            food_name: food_data.food_name, 
            calories: food_data.calories,
            // datetime: (new Date()).toISOString().slice(0, 19).replace('T', ' ')
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
            console.log(response);
        });
    }

    // pakai food_data untuk ubah data food
    function update_food_data(e){
        const {name, value} = e.target;

        console.log(name)
        set_food_data(prev => ({...prev, [name]: value}))
    }

    function inputOnChange(index, e){
        const {name, value} = e.target;
        const new_food_list = [...food_list];
        console.log(name, value)
        new_food_list[index][name] = value;
        console.log(new_food_list)
        set_food_list(new_food_list);
    }

    async function get_day_comp(){
        console.log(date_picked)

        await fetch(`http://127.0.0.1:8000/daily_consumption/${date_picked}`, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('token')
            }
        }).then(response => response.json())
        .then(response => {
            console.log(response)
            console.log(response.results)
            set_food_list(response.results);
     
            console.log(food_list)
        });
    }

    useEffect(() => {
        get_day_comp();

        console.log('asdasd')

    }, [date_picked]);

    async function delete_food(id){

        await fetch(`http://127.0.0.1:8000/daily_consumption/${id}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Authorization':  'Bearer ' + localStorage.getItem('token')
            }
        }).then(response => response.json())
        .then(response => {
            console.log(response)
        });
    }
    
    async function update_food(id){
        const body = JSON.stringify({
            "food_name": "makanan",
            "calories": 9000,
        });

        await fetch(`http://127.0.0.1:8000/daily_consumption/2`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('token')
            },
            body: body
        }).then(response => response.json())
        .then(response => {
            console.log(response)
        });

    }

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
                        console.log(e);
                        set_date_picked(() => e.getTime());
                        console.log(date_picked)
                    }}
                    footer={
                        date_picked ? `Selected: ${date_picked}` : "Pick a day."
                    } onDayClick={(e) => {
                        console.log(e)
                    }}
                    disabled={new Date(date_picked)}>
                    
                </DayPicker>

                <div className="max-w-md border rounded-sm ring ring-teal-400 p-2 ">   
                    <h1 className="text-lg pl-2">Add Food</h1>

                    <InputFood className="my-2" id="food_name" name="food_name" placeholder="Sudah makan apa anda hari ini" input_change={update_food_data}/>
                    <InputFood className="my-2" id="calories" name="calories" placeholder="Berapa Jumlah kalori makanan tersebut?" input_change={update_food_data}/>
                    
                    <button className="px-2 rounded-md border border-teal-500 bg-teal-400 text-white" onClick={add_food}>Add</button>

                </div>

                <br />
                <br />
                <ul>
                                        {food_list.map((food, index) => 
                    {

                        return <li key={food.id}>
                            <input type="text" id={`name${food.id}`} name="food_name" value={food.food_name} onChange={(e) => {
                                inputOnChange(index, e)
                            }}/>
                            <input type="number" id={`calories${food.id}`} name="calories" value={food.calories} onChange={(e) => {
                                inputOnChange(index, e)
                            }}/>   


                            <button className="m-2 border-1" onClick={() => {
                                update_food(food.id)
                            }}>update_food</button>

                            <button className="m-2 border-1" onClick={() => {
                                delete_food(food.id)
                            }}>delete</button>
                        </li>}
                    )}
                </ul>
            </Layout>
        </>
    );
}

export default Home;