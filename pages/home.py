from nicegui import ui
import requests
from utils.api import base_url
from components.event_card import show_event_card
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/")
def show_home_page():
    show_navbar()
    with ui.element("div").style("background-image:url(assets/0721c014bef6a57cfe90dd36280fedc78d278575.jpg) ").classes("h-screen w-screen flex flex-col bg-no-repeat bg-cover bg-center"):

        with ui.column().classes("items center h-[30rem] flex flex-col justify-center self-center text-center"):
            ui.label("Made For Those").classes("text-bold items-center self-center text-white uppercase").style("font-size:4rem;")
            ui.label("Who Do").classes("text-bold items-center self-center text-white uppercase").style("font-size: 4rem;")

    

    with ui.row().classes("bg-blue-800 p-4 no-gap items-center justify-center w-[90rem] -mt-10 self-center rounded").style("border-radius:10px;"):
        with ui.column():
            ui.label("Looking for").classes("text-white text-semi-bold")
            ui.select([1,2,3]).classes("w-60 bg-white").props("outlined")

        with ui.column():
            ui.label("Location").classes("text-white text-semi-bold")
            ui.select([1,2,3]).classes("w-60 bg-white").props("outlined")
        
        with ui.column():
           ui.label("when").classes("text-white text-semi-bold")
           choose=ui.select([1,2,3]).classes("w-60 bg-white").props("outlined")
        
    with ui.row().classes('w-full px-20 py-20 justify-between flex flex-row items-center'):
            with ui.row():      
                ui.label("Upcoming").classes('text-bold text-4xl')
                ui.label("Events").classes('text-bold text-blue text-4xl')
            
            with ui.row().classes("justify-end p-4 gap-x-5 items-end").style("paddinf-right:100px"):
                ui.select(["Weekdays"]).classes("w-48 h-10 bg-white").props("outlined")
                ui.select(["Event type"]).classes("w-48  h-10 bg-white").props("outlined")
                ui.select(["Any Category"]).classes("w-48  h-10 bg-white").props("outlined")
        
    with ui.grid(columns=3).classes("w-full "):
        response = requests.get(f"{base_url}/events?limit=6")
        json_data = response.json()
        for event in  json_data ["data"]:
            show_event_card(event)

    with ui.column().classes("items center self-center"):
        ui.button("Load More.....").classes("w-full items-center mt-5 justify-center")    

    ui.separator().classes("h-10 bg-white")

    with ui.column().classes("bg-[#03045e] w-full h-[300px] mt-20 gap-10"):

        with ui.grid(columns=2).classes("w-full h-full"):
            with ui.column().classes("relative"):
                ui.image("assets/2e076d64385642e5d482db14204739d55ac435fa (1).png").classes("w-[700px] absolute bottom-0")

            with ui.column().classes("gap-10 items-center mt-20"):
                ui.label("Make Your Own Event").classes("text-white text-bold text-4xl")
                ui.label("create your own exprience,start from here").classes("text-white text-xl")
                ui.button("Create Events").classes("bg-[#0077b6] text-white text-bold")

#font awesome
    ui.image("assets/Brand.png")
        

    with ui.row().classes(' mt-10 '):
            ui.label("Trending").classes('text-bold text-4xl')
            ui.label("Colleges").classes('text-bold text-blue text-3xl')

    with ui.grid(columns=3).classes("w-full "):
        for i in range(3):
            with ui.card().classes("w-[30rem] h-[25rem]"):
                ui.image("assets/d024fa95f3edc7f29200e31fe1eea04ac694603c.png")

                ui.label("Stanford University").classes('text-bold text-2xl')
                ui.label("Stanford califonia").classes("text-xl")
    with ui.column().classes("items center self-center"):
        ui.button("Load More.....").classes("self center items-center mt-5 justify-center")

    with ui.row().classes(' mt-10 '):
            ui.label("Our").classes('text-bold text-4xl')
            ui.label("Blogs").classes('text-bold text-blue text-3xl')

    with ui.grid(columns=3).classes("w-full mb-50"):
        for i in range(3):
            with ui.card().classes("w-[30rem] h-[25rem]"):
                with ui.column().style("background-image:url(assets/2661d4f20d55464672c777fe2598b4a832227655.jpg)").classes("w-full h-full"):                   
                    ui.badge("free").classes("bg-white text-blue text-xl ml-2 mt-2")

                
                with ui.column():
                    ui.label("Bestseller Book Bootcamp-write, Market & Publish your books-Lucknow").classes('text-bold text-2xl')
                    ui.label("Sunday 16 November").classes("text-blue")
                    ui.label("online-event: join anywhere").classes('text-gray-700')

            
                
    



    show_footer ()  