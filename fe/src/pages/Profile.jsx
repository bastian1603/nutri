import { useState, useEffect } from "react"

const Profile = () => {
    
    const [ username , set_username] = useState("guest")
    const [ email, set_email] = useState("guest")
    const [ password, set_password] = useState("password")

    async function get_user() {
        console.log(localStorage.getItem("token"));
        
        const body = JSON.stringify({
            "access_token": localStorage.getItem("token"),
            "token_type": "Bearer"
        });

        await fetch("http://127.0.0.1:8000/user/get_profile", {
            method: "POST",
            body: body,
            headers: {
                "Content-Type": "application/json"
            }
        }).then(response => response.json())
        .then(response => {
            set_username(response.username);
            set_email(response.email);
            set_password(response.password);

            console.log(response)
        })
    }

    // useEffect(() => {
    //     console.log(localStorage.getItem("token"));
    //     const body = JSON.stringify({
    //         "access_token": localStorage.getItem("token"),
    //         "token_type": "Bearer"
    //     });

    //     fetch("http://127.0.0.1:8000/user/get_profile", {
    //         method: "POST",
    //         body: body,
    //         headers: {
    //             "Content-Type": "application/json"
    //         }
    //     }).then(response => response.json())
    //     .then(response => {
    //         console.log(response)
    //     })
    // }, [username, email, password]);


    return (
        <>
        <h3>nama: {username}</h3>
        <h3>email: {email} </h3>
        <h3>password: {password}</h3>    
        
        <button onClick={get_user}>get_user</button>
        </>
    )
}

export default Profile