from nicegui import ui




@ui.page("/signin")
def show_signin_page():
    
    with ui.grid(columns=2).classes("w-full h-sreen m-0 p-5 gap-10"):
        with ui.column().classes("justify-center items-center p-10 w-full h-screen"):
           with ui.row().classes("items-center"):
            ui.label("Event").style("font-size:30px;")
            ui.label("Hive").style("font-size:30px; color:#5fa8d3;")  
           with ui.column().classes("items-center"):
            ui.label("Sign in to Event Hive").style("font-size:40px; font-weight:bold; Align-items:center; padding:left;").classes("items-center")

           with ui.column().classes("justify-center items-start p-10 w-full h-screen"):
            ui.label("YOUR EMAIL").classes("text-semibold text-xl text-left")
            email = ui.input('Enter your mail').props('outlined').classes('w-[35rem]')
            ui.label("PASSWORD").classes("text-semibold text-xl text-left")
            password = ui.input('Enter your password').props('outlined').classes('w-[35rem]')
            
            with ui. column().classes("items-center justify-center self-center"):
                ui.button("sign in").style("width: 250px;").classes("bg-violet-600")
                ui.label("or")
                ui.button("sign up with Google").classes("bg-white text-black w-[15rem]")

        with ui.column().classes("bg-[url(assets/a47bcf2b868b30d314da78c676d20a8f38d6f116.jpg)] w-full h-screen bg-center bg-cover flex flex-col justify-center items-center"):
         ui.label("Hello Friend").style("font-size:20px; font-weight:bold; color:#fff;")
         ui.label("To keep connected with us provide us with your information").style("color:#fff")
         ui.button("sign in").style(" color:#fff").classes("bg-gray-400")







    