import { useState } from "react";

const Login = () => {

    function handle_form_submit(e) {
        e.preventDefault();
        const form = e.target;

        const body = JSON.stringify({
           'identity': form.identity.value,
           'password': form.password.value 
        });
        

        fetch('http://127.0.0.1:8000/token', {
            method: "POST",
            body: body,
            headers: {
                'Content-Type': 'application/json'
            }

        }).then(response => response.json())
        .then(response => {console.log(response)});
    }

    return (
        <>
            <form onSubmit={(e) => {handle_form_submit(e)}} className="max-w-sm mx-auto mt-10 p-4 bg-white rounded-lg shadow-md">
            <div className="mb-4">
                <label htmlFor="identity" className="block mb-1 text-sm font-medium text-gray-700">
                Nama
                </label>
                <input
                type="text"
                id="identity"
                name="identity"
                //   value={formData.name}
                // onChange={handle_form_data}
                className="w-full border border-gray-300 rounded-lg p-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Masukkan nama"
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
                // onChange={handle_form_data}

                className="w-full border border-gray-300 rounded-lg p-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Masukkan password"
                />
            </div>
            <button
                type="submit"
                // onClick={submitting}
                className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition"
            >
                Kirim
            </button>
            </form>

        </>
    );
}

export default Login