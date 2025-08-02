import { useState } from "react";
import { Form } from "react-router-dom";

const Register = () => {
    const [form_data, set_form_data] = useState({username: "", email:"", password:"", password_confirmation:""});
    
    function handle_form_data(e) {
        const {name, value} = e.target;

        set_form_data(prev => ({...prev, [name]: value}));
    }

    function submitting(){
        const body = JSON.stringify({
            "username": form_data.username,
            "email": form_data.email,
            "password": form_data.password,
            "password_confirmation": form_data.password_confirmation
        });

        fetch("http://127.0.0.1:8000/register",{
            method: 'POST',
            body: body,
            headers: {
                'Content-Type': 'application/json'

            }
        }).then(response => response.json()).then(response => {console.log(response); return response})
    }

    return (
        <>
            <form className="max-w-sm mx-auto mt-10 p-4 bg-white rounded-lg shadow-md">
            <div className="mb-4">
                <label htmlFor="username" className="block mb-1 text-sm font-medium text-gray-700">
                Nama
                </label>
                <input
                type="text"
                id="username"
                name="username"
                //   value={formData.name}
                onChange={handle_form_data}
                className="w-full border border-gray-300 rounded-lg p-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Masukkan nama"
                />
            </div>
            <div className="mb-4">
                <label htmlFor="email" className="block mb-1 text-sm font-medium text-gray-700">
                Email
                </label>
                <input
                type="email"
                id="email"
                name="email"
                //   value={formData.email}
                //   onChange={handleChange}
                onChange={handle_form_data}

                className="w-full border border-gray-300 rounded-lg p-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Masukkan email"
                />
            </div>
            <div className="mb-4">
                <label htmlFor="password" className="block mb-1 text-sm font-medium text-gray-700">
                password
                </label>
                <input
                type="password"
                id="password"
                name="password"
                //   value={formData.email}
                //   onChange={handleChange}
                onChange={handle_form_data}

                className="w-full border border-gray-300 rounded-lg p-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Masukkan password"
                />
            </div>
            <div className="mb-4">
                <label htmlFor="password" className="block mb-1 text-sm font-medium text-gray-700">
                password confrimation
                </label>
                <input
                type="password"
                id="password_confirmation"
                name="password_confirmation"
                onChange={handle_form_data}
                
                className="w-full border border-gray-300 rounded-lg p-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Masukkan password"
                />
            </div>
            <button
                type="button"
                onClick={submitting}
                className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition"
            >
                Kirim
            </button>
            </form>

        </>
    );
}

export default Register