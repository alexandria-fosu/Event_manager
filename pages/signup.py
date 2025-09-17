from nicegui import ui,html




@ui.page("/signup")
def show_signup_page():
    
    with ui.grid(columns=2).classes("w-full h-sreen m-0 p-5 gap-10"):
        with ui.column().classes("bg-[url(/assets/6f9b55ff5c1ea52234a91587b326344fd76b83a9.jpg)] w-full h-screen bg-center bg-cover flex flex-col justify-center items-center"):
         ui.label("welcome Back").style("font-size:20px; font-weight:bold; color:#fff;")
         ui.label("To keep connected with us provide us with your information").style("color:#fff")
         ui.button("sign in").style(" color:#fff").classes("bg-gray-700")

        
        with ui.column().classes("justify-center items-center p-10 w-full h-screen"):
           with ui.row().classes("items-center"):
            ui.label("Event").style("font-size:30px;")
            ui.label("Hive").style("font-size:30px; color:#5fa8d3;")  
           with ui.column().classes("items-center"):
            ui.label("Sign Up to Event Hive").style("font-size:40px; font-weight:bold; Align-items:center; padding:left;").classes("items-center")

           with ui.column().classes("justify-center items-start p-10 w-full h-screen"):
            ui.label("YOUR NAME").classes("text-semibold text-xl text-left")
            name = ui.input('Your Name').props('outlined').classes('w-[35rem]')
            ui.label("YOUR NAME").classes("text-semibold text-xl text-left")
            name = ui.input('Your Name').props('outlined').classes('w-[35rem]')
            ui.label("PASSWORD").classes("text-semi-bold text-xl items-start")
            password = ui.input('Password').props('outlined').classes('w-[35rem]')
            ui.label("CONFIRM PASSWORD").classes("text-semi-bold text-xl items-star")
            cpassword = ui.input('Confirm Password').props('outlined').classes('w-[35rem]')

            with ui. column().classes("items-center justify-center"):
                    ui.button("sign up").style("width: 150px;").classes("bg-violet-600")
                    ui.label("or")
                    ui.button("sign up with Google").classes("bg-white text-black w-[15rem]")




  
            


        #    ui.label("YOUR NAME")
        #    ui.input(placeholder="name").style("width:100%; padding:15p; backgroun-color:#fff")
        #    ui.label("YOUR NAME")
        #    ui.input(placeholder="name").style("width:100%; padding:15p; backgroun-color:#fff")
        #    ui.label("PASSWORD")
        #    ui.input(placeholder="password").style("width:100%; padding:15p; backgroun-color:#fff")
        #    ui.label("CONFIRM PASSWORD")
        #    ui.input(placeholder="password").style("width:100%; padding:15p; backgroun-color:#fff")

        #    
        
       

