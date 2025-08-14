import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button, TextInput } from "flowbite-react"

import FormCard from "../components/FormCard";

const Register = () => {
    const [form_data, set_form_data] = useState({username: "", email:"", password:"", password_confirmation:""});
    const navigate = useNavigate();

    function handle_form_data(e) {
        const {name, value} = e.target;

        set_form_data(prev => ({...prev, [name]: value}));
    }

    async function login(){
        const body = JSON.stringify({
            "identifier": form_data.username,
            "password": form_data.password 
        });

        await fetch("http://127.0.0.1:8000/auth/login", {
            method: "POST",
            body: body,
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(response => {
            if (response.status){
                localStorage.setItem('token', response.token)
                navigate('/home')
            }
        });
    }

    async function submitting(){
        const body = JSON.stringify({
            "username": form_data.username,
            "email": form_data.email,
            "password": form_data.password,
            "password_confirmation": form_data.password_confirmation
        });

        await fetch("http://127.0.0.1:8000/auth/register",{
            method: 'POST',
            body: body,
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(response => response.json())
        .then(response => {
            console.log(response); 
            if(response.status){
                login()
            }
            return response;
        });
    }

    return (
        <>
            <div className="max-w-screen min-h-screen flex bg-white justify-center items-center">

            <FormCard class_name="max-w-xs bg-black flex flex-col p-20 rounded-xl">

                <h1 className="text-white text-4xl">Register</h1>

                <div className="mb-4">
                    <label htmlFor="username" className="block mb-1 text-sm font-medium text-gray-700 min-w-400">
                    Nama: {form_data.username}
                    </label>
                    <TextInput id="username" type="text" onChange={handle_form_data} name="username" placeholder="Masukkan Username" />

                    {/* // className="w-full border border-gray-300 rounded-lg p-2 focus:ring-blue-500 focus:border-blue-500" */}
                </div>

                <div className="mb-4">
                    <label htmlFor="email" className="block mb-1 text-sm font-medium text-gray-700">
                    Email
                    </label>

                    <TextInput id="email" type="email" onChange={handle_form_data} name="email" placeholder="Masukkan Email " />
                </div>


                <div className="mb-4">
                    <label htmlFor="password" className="block mb-1 text-sm font-medium text-gray-700">
                    password
                    </label>
                
                    <TextInput id="password" type="password" onChange={handle_form_data} name="password" placeholder="Masukkan Password " />
                    
                </div>
                <div className="mb-4">
                    <label htmlFor="password" className="block mb-1 text-sm font-medium text-gray-700">
                    password confrimation
                    </label>

                    <TextInput id="password_confirmation" type="password" onChange={handle_form_data} name="password_confirmation" placeholder="Konfimari Password" />

                </div>

                <Button onClick={submitting} className="bg-gradient-to-r from-cyan-500 to-blue-500 text-white hover:bg-gradient-to-bl focus:ring-cyan-300 dark:focus:ring-cyan-800">
                    Kirim
                </Button>
            </FormCard>
            </div>

        </>
    );
}

export default Register