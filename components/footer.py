from nicegui import ui,html
ui.add_head_html('<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin-"anonymous"></script>')

def show_footer():
    with ui.element('footer').classes("bg-[#03045e] text-white p-4 justify-center h-[18rem] rounded-b-lg w-full"):
        with ui.column().classes("items-center"):
            ui.label("Event Hive").classes("text-xl text-bold")
            with ui.grid(columns=2).classes("items-center"):
                email=ui.input("Enter Your e-mail").props("outlined").classes("text-black bg-white rounded w-[250px]")
                ui.button("Subscribe").classes("bg-[#023e8a] h-[2rem]")
              
            
            with ui.row().classes(" text-bottom gap-8 "):
                ui.link("Home").classes("text-white no-underline")
                ui.link("About").classes("text-white no-underline")
                ui.link("Services").classes("text-white no-underline")
                ui.link("Get in touch").classes("text-white no-underline")
                ui.link("FAQs").classes("text-white no-underline")

        ui.html('<hr>').classes("mt-16")  

        with ui.element("div").classes('flex flex-row justify-between text-whiye px-4 py-8 items-center text-center'):
            with ui.row():
                ui.label('English')
                ui.label('French')
                ui.label('Twi')      

            with ui.row().classes('text-white text-xl'):
                ui.html('<i class="fa-brands fa-facebook"></i>').classes('hover:text')
                ui.html('<i class="fa-brands fa-instagram"></i>').classes('hover:text')
                ui.html('<i class="fa-brands fa-linkedin"></i>').classes('hover:text') 

            with ui.row():
                ui.html("<p>Non Copyrighted &copy;2025 upload by Sunny Studio</p>")     

