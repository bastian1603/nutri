import { useState, useEffect } from "react"
import Layout from "../components/Layout"
import { TabItem, Tabs } from "flowbite-react";
import { HiAdjustments, HiClipboardList, HiUserCircle } from "react-icons/hi";
import { MdDashboard } from "react-icons/md";

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
                "Content-Type": "application/json",
                "Authorization": "Bearer " + localStorage.getItem("token")
            }
        }).then(response => response.json())
        .then(response => {
            console.log(response)
            set_username(response.username);
            set_email(response.email);
            set_password(response.password);

            console.log(response)
        })
    }

    useEffect(() => {
        get_user();
    }, []);

    return (
        <>

            <Layout>
                

                <div className="bg-teal-100 md:w-3xl md:p-10">
                    <div className="bg-black md:bg-red-100 mx-auto sm:mx-0 my-10 w-full h-60 border border-gray-100 flex items-center p-5">
                        <img className="rounded-full bg-white w-50 h-50" src="" alt="" />

                    </div>

                    
                        <Tabs aria-label="Default tabs" variant="default">
                        <TabItem active title="Profile" icon={HiUserCircle}>
                            <div className=" rounded-2xl border border-gray-500 w-md bg-red-100 md:bg-yellow-500 md:w-full px-10 py-5">
                                <h1 className="text-xl text-center">Data Akun</h1>
                                <br />
                                <h3>Username: {username}</h3>
                                <h3>Email: {email} </h3>
                                <h3>password: {password}</h3>        
                            </div>  
                        </TabItem>
                        <TabItem title="Health" icon={MdDashboard}>
                            <div className="w-md bg-red-100 sm:text-left text-center md:w-full">
                                <h1>Data Pribadi</h1>
                                <h3>Berat: {username}</h3>
                                <h3>Tinggi: {email} </h3>
                                <h3>password: {password}</h3>        
                            </div>
                        </TabItem>
                        <TabItem title="Account" icon={HiAdjustments}>
                            This is <span className="font-medium text-gray-800 dark:text-white">Settings tab's associated content</span>.
                            Clicking another tab will toggle the visibility of this one for the next. The tab JavaScript swaps classes to
                            control the content visibility and styling.
                        </TabItem>
                        </Tabs>

  

                    <div className="sm:hidden block">asdasd</div>

                    <br />


                    <br />   
                </div>
                
            </Layout>
           
        </>
    )
}

export default Profile