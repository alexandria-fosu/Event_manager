from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer





@ui.page("/event")
def show_event_page():
    show_navbar()
    with ui.column().classes("bg-[url(assets/2661d4f20d55464672c777fe2598b4a832227655.jpg)] w-full h-screen bg-center bg-cover flex gap-20 "):
        #ui.image("").classes("w-full h-full rounded-lg mb-4 ")
        with ui.row().classes('flex flex-col p-30 ml-30 w-full h-full bg-black/30 gap-30 justify-betweeen '):

            with ui.column().classes('ml-20 mt-60'):
                ui.label('Dream World Wide in').classes("text-6xl text-white text-bold")
                ui.label('Jakatra').classes("text-6xl text-white text-bold ")
                ui.label('IIIT Sonepat').classes('text-white text-bold text-2xl')

                ui.label('DesignHub organized a 3D Modeling Workshop using Blender on 16th February').classes("text-white")
                ui.label('at 5 PM. The workshop taught participants the magic of creating stunning 3D models and ').classes("text-white")
                ui.label("animations using Blender. It was suitable for both beginners and experienced users.").classes("text-white")
                ui.label("The event was followed by a blender-render competition, which added to the excitement.").classes("text-white")

            with ui.card().classes("w-[300px] h-[300px] mx-auto p-6 bg-white shadow-xl mt-10 items-center  mt-60"):
                ui.label('Date & Time').classes('text-blue text-bold text-2xl')
                ui.label('sunday 16th November 9:30pm').classes("text-gray-600")
                ui.label('Add to callender').classes("text-gray-600")
                ui.button("Book Now").classes('bg-black')
                ui.button('Programe Prompter').classes('bg-black')
                ui.label('No Refund').classes("text-gray-600")

    with ui.grid(columns=2).classes("gap-20"):
        with ui.column().classes('ml-10 mt-10'):
            ui.label('Description').classes('text-bold text-2xl')
            ui.label('DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender.').classes('text-gray-600')
            ui.label('It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement.').classes('text-gray-600')
            ui.label('DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender. ').classes('text-gray-600')
            ui.label('It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement.').classes('text-gray-600')
            ui.label("Hours").classes("text-bold text-2xl")
            with ui.row():
                ui.label("Weekdays hour:").classes('text-gray-600')
                ui.label("7pm-10pm").classes('text-blue text-bold')
            with ui.row():    
                ui.label("Sunday hour:").classes('text-gray-600')
                ui.label("7pm-10pm").classes('text-blue text-bold')
            ui.label("Organizer Contact").classes("text-bold text-2xl") 
            ui.label("Please go to www.sneakypeeks.com and refer the FAQ section for more detail").classes('text-gray-600')

        with ui.column().classes("mt-10 mr-10"):
            ui.label("Event Location").classes('text-bold text-2xl') 
            with ui.card().classes("w-[400px] h-[300px] mx-auto p-6 bg-white shadow-xl item-center "): 
                ui.image('assets/9f9c575c5abfed8372ef0cd7d36dbfb7f9fbbe6f.png').classes("w-[300px] h-[350px]")

                ui.label("Dream World Wide in Jakatra").classes("text-bold text-2xl")
                ui.label("Dummy location generation model by RSU ... Our approach generates more realistic dummy locations ").classes('text-gray-600')


    with ui.grid(columns=3).classes("w-full mt-20"):
        for i in range(6):
            with ui.card().classes("w-[30rem] h-[25rem]"):
                ui.image("assets/2661d4f20d55464672c777fe2598b4a832227655.jpg")

                ui.label("Bestseller Book Bootcamp-write, Market & Publish your books-Lucknow").classes('text-bold text-2xl')
                ui.label("Sunday 16 November").classes("text-blue")
                ui.label("online-event: join anywhere").classes('text-gray-700')
         
    show_footer()