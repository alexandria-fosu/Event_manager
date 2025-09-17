from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer



@ui.page('/create_event')
def show_create_event_page():
    ui.query(".nicegui-content").classes('m-0 p-0 gap-0')
    show_navbar()
    with ui.element("div").classes("w-full h-full items-center flex flex-col bg-slate-100"):
        # "Create Event" section
        ui.label("Create Event").classes("font-bold text-3xl mb-4 mt-10") # Reduced top margin
        with ui.card().classes("font-bold shadow-xl w-3/5"):
            ui.label("Event Title").classes("text-slate-500 font-normal text-sm")
            ui.input(placeholder="Enter your title").props("outlined").classes("w-full")
            ui.label("Event Venue").classes("text-slate-500 font-normal text-sm")
            ui.input(placeholder="Enter your venue").props("outlined").classes("w-full")
            
            # Start and End Time section with time inputs
            with ui.row().classes("w-full justify-between gap-4"):
                with ui.element('div').classes("flex flex-col grow"):
                    ui.label("Start time").classes("text-slate-500 font-normal text-sm")
                    ui.input().props("outlined type=time").classes("w-full")
                with ui.element('div').classes("flex flex-col grow"):
                    ui.label("End time").classes("text-slate-500 font-normal text-sm")
                    ui.input().props("outlined type=time").classes("w-full")

            # Start and End Date section with date inputs
            with ui.row().classes("w-full justify-between gap-4"):
                with ui.element('div').classes("flex flex-col grow"):
                    ui.label("Start date").classes("text-slate-500 font-normal text-sm")
                    ui.input().props("outlined type=date").classes("w-full")
                with ui.element('div').classes("flex flex-col grow"):
                    ui.label("End date").classes("text-slate-500 font-normal text-sm")
                    ui.input().props("outlined type=date").classes("w-full")
    
    with ui.element("div").classes("w-full items-center flex flex-col bg-slate-100 mt-10"): # Added a positive margin for separation
        # "Event Description" section
        ui.label("Event Description").classes("font-bold text-3xl mb-4")
        with ui.card().classes("font-bold shadow-xl mb-8 w-3/5"):
            ui.label("Event Image").classes("text-slate-500 font-normal text-sm")
            # Image upload component
            ui.upload(label="Click or drop an image to upload").classes("w-full h-48 bg-slate-200 rounded")
            ui.label("Event Description").classes("text-slate-500 font-normal text-sm mt-4")
            ui.input(placeholder="Type here...").props("outlined type=textarea").classes("w-full h-32")

        ui.button("Create Event").classes("w-3/5 h-12 mb-20 bg-purple-700 hover:bg-purple-800")
    show_footer()

    