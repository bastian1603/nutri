import { Navbar, NavbarToggle, NavbarLink, NavbarCollapse } from "flowbite-react";



const Layout = ({ children }) => {
    return (
        <>
        <main className="flex flex-col justify-center items-center"> { children } </main>
        
        
        <Navbar className="!bg-teal-300 max-w-screen-lg min-w-lg absolute left-1/2 transform -translate-x-1/2 bottom-4 rounded-full border border-gray-200" fluid rounded>
            <NavbarToggle />
            
            <NavbarCollapse className="min-w-full !flex !justify-evenly">
                <NavbarLink className="!text-black mx-10" href="/home">
                    Home
                </NavbarLink>

                <NavbarLink className="!text-black mx-10" href="/scan">
                    Scan
                </NavbarLink>
            
                <NavbarLink className="!text-black mx-10" href="/profile">
                    Profile
                </NavbarLink>
            </NavbarCollapse>
        </Navbar>    
        </>
    );
}

export default Layout;