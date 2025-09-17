from nicegui import ui

from components.navbar import show_navbar
from components.footer import show_footer 

@ui.page("/not_found")
def show_not_found_page():
    show_navbar()
    with ui.column().classes("w-[60rem] h-full items-center justify-center flex flex-col ml-60"):
        ui.image("/assets/undraw_page_not_found_su7k 1.svg")

        ui.label("OOPS!").classes('text-2xl text-bold')
        ui.label("We can’t seem to find the page you are looking for").classes("text-gray-700")

        ui.button('Back to Hompage', on_click=lambda: ui.navigate.to('http://127.0.0.1:8080/home')).classes('bg-violet w-[200px]')

    show_footer()