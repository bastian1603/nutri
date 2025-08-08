import { Navbar, NavbarToggle, NavbarLink, NavbarCollapse } from "flowbite-react";
const Layout = ({ children }) => {
    return (
        <>
    


        <main className="flex flex-col justify-center items-center"> { children } </main>
        
        
        <Navbar className="!bg-teal-300 max-w-screen-lg min-w-lg absolute left-1/2 transform -translate-x-1/2 bottom-0" fluid rounded>
            <NavbarToggle />
            
            <NavbarCollapse className="!bg-yellow-100 min-w-full !flex !justify-evenly">
                <NavbarLink className="!text-black" href="/home">
                    Home
                </NavbarLink>

                <NavbarLink className="!text-black" href="/scan">
                    Scan
                </NavbarLink>
            
                <NavbarLink className="!text-black" href="/profile">
                    Profile
                </NavbarLink>
            </NavbarCollapse>
        </Navbar>    
        </>
    );
}

export default Layout;